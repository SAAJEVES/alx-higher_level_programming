#!/usr/bin/node

num = parseInt(process.argv[2]);

let result = 1;

function fac(val) {
  if (isNaN(val) && process.argv.length > 2) {
    console.log(NaN);
  } else {
    for (let i = 1; i <= val; i++) {
      result = result * i;
    }
  }
    console.log(result);
}
fac(num);
