#!/usr/bin/node
// prints the title of the movie for a given id

function getCompleted (body, id) {
  const tasks = JSON.parse(body);
  let count = 0;
  for (const task of tasks) {
    if (task.userId === id && task.completed) {
      count++;
    }
  }
  return count;
}

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const completedDict = {};
    for (let i = 1; i < 11; i++) {
      const completed = getCompleted(body, i);
      if (completed > 0) {
        completedDict[i] = completed;
      }
    }
    console.log(completedDict);
  }
});
