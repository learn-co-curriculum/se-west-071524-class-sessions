import './style.css'

document.querySelector('#app').innerHTML = `
  <div>
    
    <h1>Hello Big O!</h1>
   
  </div>
`

// What is the Big O of these functions?
// - Constant O(1)
// - Linear O(n)
// - Logarithmic O(log n)
// - Quadradtic O(n^2) 

// O(1) Constant
function printFirstItem(items) {
  console.log(items[0]);
}

const laundry = ["shirt", "shorts", "sock", "pants", "underwear"]

// printFirstItem(laundry)

// O(n^2) Quadratic
function printAllPossibleOrderedPairs(items) {
  items.forEach(firstItem => {
    items.forEach(secondItem => {
      console.log(firstItem, secondItem);
    });
  });
}

// printAllPossibleOrderedPairs(laundry)

// n can be the actual input, or the size of the input
// O(n) Linear
function sayHiNTimes(n) {
  for (let i = 0; i < n; i++) {
    console.log('hi');
  }
}

// sayHiNTimes(5)

// O(n) Linear
function printAllItems(items) {
  items.forEach(item => {
    console.log(item);
  });
}


// printAllItems(laundry)

// Drop the contants

// O(2n) => O(n) Linear
function printAllItemsTwice(items) {
  items.forEach(item => {
    console.log(item);
  });

  // Once more, with feeling
  items.forEach(item => {
    console.log(item);
  });
}

// printAllItemsTwice(laundry)

// O(3 + n/2 + 100) => O(n) Linear
function printFirstItemThenFirstHalfThenSayHi100Times(items) {
  console.log(items[0]);

  const middleIndex = Math.floor(items.length / 2);
  let index = 0;

  while (index < middleIndex) {
    console.log(items[index]);
    index++;
  }

  for (let i = 0; i < 100; i++) {
    console.log('hi');
  }
}

// printFirstItemThenFirstHalfThenSayHi100Times(laundry)

// Drop the less significant term

// O(n + n^2 + 2) => O(n^2) Quadratic
function printAllNumbersThenAllPairSums(numbers) {

  console.log('these are the numbers:');
  numbers.forEach(number => {
    console.log(number);
  });

  console.log('and these are their sums:');
  numbers.forEach(firstNumber => {
    numbers.forEach(secondNumber => {
      console.log(firstNumber + secondNumber);
    });
  });
}

const nums = [2, 5, 6, 1, 7, 10, 34, 60]

// printAllNumbersThenAllPairSums(nums)

// Always count the worst case scenario

// O(n) Linear
function contains(haystack, needle) {

  // Does the haystack contain the needle?
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle) {
      return true;
    }
  }

  return false;
}

// Space complexity

// O(1) Constant
// function sayHiNTimes(n) {
//   for (let i = 0; i < n; i++) {
//     console.log('hi');
//   }
// }

// O(n) Linear
function arrayOfHiNTimes(n) {
  const hiArray = [];
  for (let i = 0; i < n; i++) {
    hiArray[i] = 'hi';
  }
  return hiArray;
}

// When measuring space complexity, it's additional space besides the input

// O(1) Constant
function getLargestItem(items) {
  let largest = -Number.MAX_VALUE;
  items.forEach(item => {
    if (item > largest) {
      largest = item;
    }
  });
  return largest;
}

console.log(getLargestItem(nums))
