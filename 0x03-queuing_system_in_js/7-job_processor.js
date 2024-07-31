// 7-job_processor.js

import { createQueue } from 'kue';

// we create a kue queue
const queue = createQueue();

// array of blacklisted phoneNumbers
const blacklistedNums = ['4153518780', '4153518781'];

// function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // track job progress
  job.progress(0, 100);

  // check if phoneNumber is blacklisted
  if (blacklistedNums.includes(phoneNumber)) {
    // mark the job as failed
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // we simulate the sending of the notification
  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  // mark job as complete
  job.progress(100, 100);
  done();
}

// process the jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
