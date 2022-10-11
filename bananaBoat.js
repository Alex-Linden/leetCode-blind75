"use strict";
const alphabet = "abcdefghijklmonpqrstuvwxyz";
function countSubstrings(str) {
  let count = {};
  let freq = new Array(str.length).fill().map(() => []);

  let l = 0;
  let r = l + 1;

  while (l < str.length) {
    if (alphabet.includes(str[l])) {
      let curr = count[str[l]] || 0;
      count[str[l]] = curr + 1;
      while (alphabet.includes(str[r])) {
        let tmp = str.slice(l, r + 1);
        let tmpCount = count[tmp] || 0;
        count[tmp] = tmpCount + 1;
        r++;
      }
    }
    l++;
    r = l + 1;
  }

  for (let sub in count) {
    let i = count[sub];
    freq[i].push(sub);
  }

  let alphabeticalFreq = freq.map(n => n.sort());

  console.log(alphabeticalFreq);

  let out = "";

  for (let i = alphabeticalFreq.length; i > 0; i--) {
    if (alphabeticalFreq[i]) {
      for (let j = 0; j < alphabeticalFreq[i].length; j++) {
        out += `${i}:${alphabeticalFreq[i][j]}\n`;
      }
    }
  }

  return out;
}