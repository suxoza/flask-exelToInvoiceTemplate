function some(first, second){  
  var firstArr = first.split("")
  var secondArr = second.split("")
  var len = 0;
  var lnght = firstArr.length
  var obj = {}
  for(var i = 0; i <= lnght - 1; i++)
    obj[firstArr[i]] = (!obj.hasOwnProperty(firstArr[i]))?1:obj[firstArr[i]] + 1;

  for(var i = 0; i <= lnght - 1; i++){
     if(!obj.hasOwnProperty(secondArr[i]))return false;
     obj[secondArr[i]]--;  
  }

  for(var i in obj)if(obj[i] < 0) return false;
  return true;

}