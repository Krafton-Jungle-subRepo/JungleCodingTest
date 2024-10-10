const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '100-구현/1417/example.txt';

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n')
  .map(Number);

let num = input.shift();
let dasom = input.shift();

if (num === 1) {
  console.log(0);
} else {
  let max = Math.max(...input);
  let answer = 0;

  while (dasom <= max) {
    input[input.indexOf(max)] -= 1;
    answer++;
    dasom++;
    max = Math.max(...input);
  }
  console.log(answer);
}
