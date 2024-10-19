const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : 'SeungchanHan/Week6/24954.txt';

const input = fs.readFileSync(filePath).toString().trim().split('\n');
const N = input.shift();
const prices = input.shift().split(' ').map(Number);

function solvePotionPurchase(N, prices, discounts) {
  let minCost = Infinity;
  const potions = Array.from({ length: N }, (_, i) => i);

  const permutations = potions.reduce((prev, cur) => {
    if (prev.length === 0) return [[cur]];

    const newPermutations = [];
    prev.forEach((permutation) => {
      for (let i = 0; i <= permutation.length; i++) {
        const newPermutation = [
          ...permutation.slice(0, i),
          cur,
          ...permutation.slice(i),
        ];

        newPermutations.push(newPermutation);
      }
    });
    return newPermutations;
  }, []);

  for (let order of permutations) {
    let totalCost = 0;
    let currentPrices = [...prices];

    for (let potion of order) {
      totalCost += currentPrices[potion];

      for (let [targetPotion, discount] of discounts[potion]) {
        currentPrices[targetPotion] = Math.max(
          1,
          currentPrices[targetPotion] - discount,
        );
      }
    }

    minCost = Math.min(minCost, totalCost);
  }

  return minCost;
}

function transformInput(input) {
  const discounts = [];
  for (let i = 0; i < input.length; ) {
    const count = Number(input[i++]);

    discounts.push(
      Array.from({ length: count }, () =>
        input[i++]
          .split(' ')
          .map((x, j) => (j === 0 ? Number(x) - 1 : Number(x))),
      ),
    );
  }
  return discounts;
}

const result = solvePotionPurchase(+N, prices, transformInput(input));
console.log(result);
