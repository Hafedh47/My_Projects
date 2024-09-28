function factorial(num){
    return num === 0 ? 1 : num * factorial(num - 1);
}

let number=prompt('Enter a number, please');
let result=factorial(number);
alert(result);


console.log('_______________________\n');


function factor(n){
    if(n === 0){
        return 1;
    } else {
        return n * factor(n - 1);
    }
}


let x = prompt('Enter a number');
alert(factor(x));