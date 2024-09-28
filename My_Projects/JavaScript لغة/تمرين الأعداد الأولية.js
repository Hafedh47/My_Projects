function isPrime(num) {
    for(let i = 2; i < num; i++ ){
        if(num % i === 0){
            return false;
        }
        return num > 1;
    }
}

function primes(max) {
    for(let i = 2; i < max; i++ ) {
        if(isPrime(i)) console.log(i);
    }

}

let num=prompt('Enter a number, please');
primes(num);