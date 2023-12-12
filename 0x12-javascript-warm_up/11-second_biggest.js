#!/usr/bin/node

function secondLargest (numList) {
  const newNumList = numList.slice(2);
  for (let i = 0; i < newNumList.length; i++) {
    for (let j = 0; j < newNumList.length - 1; j++) {
      if (newNumList[j] > newNumList[j + 1]) {
        const temp = newNumList[j];
        newNumList[j] = newNumList[j + 1];
        newNumList[j + 1] = temp;
      }
    }
  }
  console.log(parseInt(newNumList[newNumList.length - 2]));
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  secondLargest(process.argv);
}
