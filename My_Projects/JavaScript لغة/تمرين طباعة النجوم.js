let rows = prompt('Enter a number for the stars?')


for(let row = 1; row <= rows; row++){
    let stars ='';
    for(let j = 0; j < row ; j++){
        stars += '*';
    }
    console.log(stars);
}


console.log("______________________\n\n");


let user = prompt('Enter a number to make a pyramid ')

let Rows = 1;
while(Rows <= user){
    let row = 0;
    let signDollar = '';
    while(row < Rows){
        signDollar += '*';
        row ++;
    }
    console.log(signDollar)
    Rows ++;
}