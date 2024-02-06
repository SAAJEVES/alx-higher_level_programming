#!/usr/bin/node
/*
script that computes the number of tasks completed by user id.

  -- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
  -- Only print users with completed task
  -- You must use the module request
*/

const nreq = require('request');

nreq(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
