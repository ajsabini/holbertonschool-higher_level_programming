#!/user/bin/node
//inrement and call a function
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}
module.exports = { addMeMaybe };
