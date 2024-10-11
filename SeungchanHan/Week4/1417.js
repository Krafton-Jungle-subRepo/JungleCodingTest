const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : 'SeungchanHan/Week4/1417.txt';

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n')
  .map(Number);

let num = input.shift();
let da = input.shift();

if (num === 1) {
  console.log(0);
} else {
  let max = Math.max(...input);
  let answer = 0;

  while (da <= max) {
    input[input.indexOf(max)] -= 1;
    answer++;
    da++;
    max = Math.max(...input);
  }
  console.log(answer);
}
