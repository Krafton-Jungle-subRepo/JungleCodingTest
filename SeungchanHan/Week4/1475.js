const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : 'SeungchanHan/Week4/1475.txt';
const roomNumber = fs.readFileSync(filePath).toString().trim();

let digits = new Array(10).fill(0);
for (let num of roomNumber) {
  digits[parseInt(num)]++;
}
let sixAndNine = Math.ceil((digits[6] + digits[9]) / 2);
digits[6] = sixAndNine;
digits[9] = sixAndNine;

console.log(Math.max(...digits));
