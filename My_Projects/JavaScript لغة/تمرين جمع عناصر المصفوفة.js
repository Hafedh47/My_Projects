let numbers=[20,30,50,100];

{let Total_1 = 0; 
for(let i = 0 ;i < numbers.length; i++){
  
    Total_1 += numbers[i];
}
console.log(Total_1);}


console.log('--------------------\n');


{let Total_2 = 0;
let i = 0;
while(i<numbers.length){
    Total_2 += numbers[i];
    i++;
}
console.log(Total_2);}


console.log('--------------------\n');


{let Total_3 = 0;
for(let i in numbers ){ 
    Total_3 += numbers[i];
}
console.log(Total_3);}


console.log('--------------------\n');


{let Total_4=0;
for(let i of numbers){
    Total_4 += i;
}
console.log(Total_4);}

