// 8-jobs.js

// import { createQueue } from 'kue';

// create pushNotification function
function createPushNotificationsJobs(jobs, queue) {
  // validate the input
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // iterate over job array and create a job for each item
  jobs.forEach((jobData) => {
    const job = queue
      .create('push_notification_code_3', jobData)
      .save((err) => {
        if (err) {
          console.log(`Notification job failed: ${err}`);
        } else {
          console.log(`Notification job created: ${job.id}`);
        }

      });

    // event listeners for the job status
    job
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
  });
}

// export function
module.exports = createPushNotificationsJobs;
