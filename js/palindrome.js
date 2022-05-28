exports.palindrome = function (word) {
  word = String(word).toLocaleLowerCase();
  word = word.replace(/\W/g, "");
  return word === word.split("").reverse().join("") ? true : false;
};
