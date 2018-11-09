# leetcode-804-唯一摩尔斯密码词.py
# 国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如: "a" 对应 ".-", "b" 对应 "-...", "c" 对应 "-.-.", 等等。

# 为了方便，所有26个英文字母对应摩尔斯密码表如下：

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# 给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，"cab" 可以写成 "-.-.-....-"，(即 "-.-." + "-..." + ".-"字符串的结合)。我们将这样一个连接过程称作单词翻译。

# 返回我们可以获得所有词不同单词翻译的数量。

# 例如:
# 输入: words = ["gin", "zen", "gig", "msg"]
# 输出: 2
# 解释: 
# 各单词翻译如下:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# 共有 2 种不同翻译, "--...-." 和 "--...--.".
 

# 注意:

# 单词列表words 的长度不会超过 100。
# 每个单词 words[i]的长度范围为 [1, 12]。
# 每个单词 words[i]只包含小写字母。


# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def wordTocode(W):
            tmp = []
            for w in W:
                tmp.append(codes[ord(w)-ord('a')])
            return "".join(tmp)

        ans = set()
        for word in words:
            ans.add(wordTocode(word))

        return len(ans)


执行用时为 36 ms 的范例
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mapList=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphaList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        mapDict={}
        for i in range(26):
            mapDict[alphaList[i]]=mapList[i]
        morseList=[]
        for word in words:
            tmpStr=""
            for alpha in word:
                tmpStr=tmpStr+mapDict[alpha]
            morseList.append(tmpStr)
        return len(set(morseList))