const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const [n, ...arr] = input;
const obj = {};

arr.forEach((el,i) => {
    const [a,b] = el.split(' ');
    console.log(a);
})