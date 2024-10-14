const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : 'SeungchanHan/Week5/11279.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const N = input.shift();

class MaxHeap {
  constructor() {
    this.heap = [];
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  insert(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  bubbleUp() {
    let currentIndex = this.heap.length - 1;

    while (currentIndex > 0) {
      const parentIndex = Math.floor((currentIndex - 1) / 2);
      if (this.heap[parentIndex] >= this.heap[currentIndex]) break;

      this.swap(currentIndex, parentIndex);
      currentIndex = parentIndex;
    }
  }

  getMax() {
    if (this.isEmpty()) return 0;
    if (this.heap.length === 1) return this.heap.pop();

    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.sinkDown(0);

    return max;
  }

  sinkDown(index) {
    const leftIndex = 2 * index + 1;
    const rightIndex = 2 * index + 2;
    let largestIndex = index;

    if (
      leftIndex < this.heap.length &&
      this.heap[leftIndex] > this.heap[largestIndex]
    ) {
      largestIndex = leftIndex;
    }

    if (
      rightIndex < this.heap.length &&
      this.heap[rightIndex] > this.heap[largestIndex]
    ) {
      largestIndex = rightIndex;
    }

    if (largestIndex !== index) {
      this.swap(index, largestIndex);
      this.sinkDown(largestIndex);
    }
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}

function solution() {
  const answer = [];
  const maxHeap = new MaxHeap();

  for (let i = 0; i < +N; i++) {
    const value = +input[i];
    value === 0 ? answer.push(maxHeap.getMax()) : maxHeap.insert(value);
  }

  return answer.join('\n');
}

console.log(solution());
