function bubbleSort(array){
    let swapped;
    do{
        swapped =false;
        for(let i = 0; i < array.length; i++){
            if (array[i] > array[i + 1]){
                content = array[i];
                array[i] = array[i + 1];
                array[i + 1] = content;
                swapped = true;
        }
        
    }
    
} while(swapped);

 return array;
  
}

let array = bubbleSort([7, 8, 3, 2, 5, 6, 4, 1]);
console.log(array);