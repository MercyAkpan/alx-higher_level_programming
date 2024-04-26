exports.addMeMaybe = function (number, theFunction){
        theFunction(++number); // Pre-increment the number before sending through to function, not post-increment
}
