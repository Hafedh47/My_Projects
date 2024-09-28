let numbers = [1,2,3,4,5,6,7,8,9,10];

function reverse(arr){
    let temp = [];
    for (let i in arr){
        temp.unshift(arr[i]);
    }
    return temp;
}
console.log(reverse(numbers));



function Reverse(Arr){
    for(let i in Arr){
        Arr.splice(i, 0, Arr.pop());
    }
    return Arr;
}

console.log(Reverse(numbers))

    