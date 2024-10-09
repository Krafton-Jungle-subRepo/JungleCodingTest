const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : 'SeungchanHan/Week4/11399.txt';
const [n, input] = fs.readFileSync(filePath).toString().trim().split('\n');
const inputArr = input.trim().split(' ').map(Number);

const calculateCumulativeSum = (inputArr) => {
  const sums = inputArr
    .sort((a, b) => a - b)
    .reduce((acc, cur, idx) => {
      const target = acc[idx - 1] || 0;
      acc.push(target + cur);
      return acc;
    }, []);
  const total = sums.reduce((sum, num) => sum + num, 0);
  return total;
};

console.log(calculateCumulativeSum(inputArr));
