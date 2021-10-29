// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python


function deepCount(array){
    // let count = 0
    // for(index in array){
    //     if (Array.isArray(array[index])){
    //         count += 1
    //         console.log(array[index], count)
    //         count += deepCount(array[index])
    //     }
    //     else{
    //         count += 1
    //         console.log(array[index], count)
    //     }
    // }
    // return count

    // OTHER SOLUTION
    return array.reduce((a,b) => a + (Array.isArray(b) ? deepCount(b) : 0), array.length)
}

// console.log(deepCount([1,2,3,[4,5,[6]]]))


// https://www.codewars.com/kata/5533c2a50c4fea6832000101/train/javascript

function createDict(keys, values){
  return Object.fromEntries(keys.map((item,idx) => [item,values[[idx]] || null]))
}

console.log(createDict(["a","c","d"],[1,2]))