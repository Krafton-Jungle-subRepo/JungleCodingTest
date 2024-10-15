const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : 'SeungchanHan/Week5/1913.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, target] = input.map(Number);

function createBoard(size) {
  return Array.from({ length: size }, () => Array(size).fill(0));
}

function fillSpiral(board, target) {
  const size = board.length;
  let position = { row: Math.floor(size / 2), col: Math.floor(size / 2) };
  let currentNumber = 1;
  let targetPoint = [];

  function fillCell() {
    const { row, col } = position;

    board[row][col] = currentNumber++;
    if (board[row][col] === target) {
      targetPoint = [row + 1, col + 1];
    }
  }

  function move(rowDelta, colDelta, count) {
    for (let i = 0; i < count; i++) {
      position.row += rowDelta;
      position.col += colDelta;
      fillCell();
    }
  }

  fillCell(); // 중앙 채우기

  for (let currentSize = 3; currentSize <= size; currentSize += 2) {
    position.row--; // 위로 한 칸 이동
    fillCell();

    move(0, 1, currentSize - 2); // 오른쪽
    move(1, 0, currentSize - 1); // 아래
    move(0, -1, currentSize - 1); // 왼쪽
    move(-1, 0, currentSize - 1); // 위
  }

  return targetPoint;
}

function printBoard(board) {
  for (let row of board) {
    console.log(row.join(' '));
  }
}

const board = createBoard(n);

const targetPoint = fillSpiral(board, target);
printBoard(board);
console.log(`${targetPoint[0]} ${targetPoint[1]}`);
