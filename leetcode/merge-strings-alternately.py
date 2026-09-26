class Solution {
    func mergeAlternately(_ word1: String, _ word2: String) -> String {
        let word1 = Array(word1)
        let word2 = Array(word2)
        var x = 0
        var mergedString = ""
        while x <= word1.count - 1 && x <= word2.count - 1 {
            mergedString += String(word1[x])
            mergedString += String(word2[x])
            x+=1
            
        }   
        if x < word1.count {
           mergedString += word1[x...]
        }

        if x <= word2.count {
           mergedString += word2[x...]
        }

    return mergedString 
    }
    

}