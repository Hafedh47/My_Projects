let array = ['Hafedh', 3, false, 'Zaki', true, 9];

for (let i = 0; i < array.length; i++){
    if(typeof array[i] === 'string'){
    console.log(array[i]);
    }
}

console.log('_________________________\n\n');

let i = 0;
while (i < array.length){
    if(typeof array[i] === 'string'){
        console.log(array[i]);
        }
    i++;
}

console.log('_________________________\n\n');

for(let i in array){
    if(typeof array[i] === 'string'){
        console.log(array[i]);
        }   
}

console.log('_________________________\n\n');

for(let i of array){
    if(typeof i === 'string'){
        console.log(i);
    }
}

