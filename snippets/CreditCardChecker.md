Title| Tags
-----|-----
validateCredit | array,math,logic,intermediate

  * This function uses the _Luhn Method_ to check whether the credit card number is valid or not.
  * This function takes the credit card number as an array
  * It then uses the _Luhn Method_ to check the array 
  ````
  const validateCredit =(arr)=>{
  let  Credit= arr;
  let sum = 0;
  for(let i=arr.length;i>=0;i--)
    {
        let num = Credit[i];
      // Double every other number
      if(i !==0 && i%2==0)
        {
          num = [i] * 2;
        }
      // if double number is greater than 9
      if(num > 9)
        {
          num-=9;
        }
      sum+=num;
    }  
  if(sum%10===0){
       return true;
     }else {
       return false;
     }
};
`````
  The function will work as
  ``````````
  const valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8];
  const check = validateCredit(valid1); // retruns true
  
  ````````````
