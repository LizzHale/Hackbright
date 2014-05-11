var sum = 0;
var x = 1;
while (x < 1000) {
    if (x % 3 === 0 || x % 5 === 0 ) {
        sum += x;
    }
        x++;
}

console.log(sum);
