/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    let occ = new Object();
    
    for(i = 0; i < sentence.length; i++){
        occ[sentence[i]]++;
    }
    
    return (Object.keys(occ).length === 26)
};