// 9-stock.js

import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// create Redis clients and promisify Redis methods
const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// data for the products
const productsList = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// create function to get item by id
const getItemById = (id) => productsList.find((product) => product.id === id);

// reserve stock by item id
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// get current reserved stock by id
// get current reserved stock by id
const getCurrentReservedStockById = async (itemId) => {
  // Get the reserved stock from Redis using the item id as the key
  const reservedStock = await getAsync(`item.${itemId}`);
  // If the reserved stock is not null, parse it as an integer and return it
  // Otherwise, return null
  return reservedStock !== null ? parseInt(reservedStock, 10) : null;
};

// Create Express app
const app = express();
const port = 1245;

// Route to list all products
app.get('/list_products', (req, res) => {
  const response = productsList.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(response);
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  // Parse the itemId from the request parameters
  const itemId = parseInt(req.params.itemId, 10);
  // Get the product with the specified itemId
  const product = getItemById(itemId);
  // If the product is not found, return a JSON response with status 'Product not found'
  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  // Get the current reserved stock for the product
  const currentQuantity = await getCurrentReservedStockById(itemId);
  // Return a JSON response with the product details
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentQuantity !== null ? currentQuantity : product.stock,
  });
});

// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  const availableStock =
    currentQuantity !== null ? currentQuantity : product.stock;

  if (availableStock <= 0) {
    res.json({ status: 'Not enough stock available', itemId: itemId });
    return;
  }

  await reserveStockById(itemId, availableStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
