function Fibonnaci(max) {
    if (max > 1) {
        var currentFib = 1;
        // console.log("current fib is" + currentFib);
        var fibList = [1];
        // console.log("fiblist is" + fibList);
        while (currentFib < max) {
            fibList.push(currentFib);
            currentFib += fibList[fibList.length - 2];
        }
        return fibList;
    }
    else {
        return [1,1];
    }
}

function even(x) {
    return x % 2 === 0;
}

function filter(condition, list) {
    returnList = [];
    for (var index = 0; index < list.length; index++) {
        if (condition(list[index])) {
            returnList.push(list[index]);
        }
    }
    return returnList;
}
// NOTE: For n in list... n is index need to say list[n]

function sum(list) {
    var total = 0;
    for (var index = 0; index < list.length; index++) {
        total += list[index];
    }
    return total;
}

console.log(sum(filter(even,Fibonnaci(4000000))));