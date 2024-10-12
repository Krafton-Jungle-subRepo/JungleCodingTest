const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : 'SeungchanHan/Week4/1991.txt';
const [n, ...input] = fs.readFileSync(filePath).toString().split('\n');

const tree = {};
for (let i = 0; i < n; i++) {
  const [node, left, right] = input[i].split(' ');
  tree[node] = [left, right];
}

let preResult = '';
const preOrderTraversal = (node) => {
  if (node === '.') return;
  const [left, right] = tree[node];
  preResult += node;
  preOrderTraversal(left);
  preOrderTraversal(right);
};

let inResult = '';
const inOrderTraversal = (node) => {
  if (node === '.') return;
  const [left, right] = tree[node];
  inOrderTraversal(left);
  inResult += node;
  inOrderTraversal(right);
};

let postResult = '';
const postOrderTraversal = (node) => {
  if (node === '.') return;
  const [left, right] = tree[node];
  postOrderTraversal(left);
  postOrderTraversal(right);
  postResult += node;
};

preOrderTraversal('A');
inOrderTraversal('A');
postOrderTraversal('A');

console.log(preResult);
console.log(inResult);
console.log(postResult);
