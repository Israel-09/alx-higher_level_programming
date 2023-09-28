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
    let pre = '{';
    for (let i = 1; i < 11; i++) {
      const completed = getCompleted(body, i);
      if (i === 10 && completed > 0) {
        console.log(`  '${i}': ${completed} }`);
        break;
      }
      if (completed > 0) {
        console.log(`${pre} '${i}': ${completed},`);
        pre = ' ';
      }
    }
  }
});
