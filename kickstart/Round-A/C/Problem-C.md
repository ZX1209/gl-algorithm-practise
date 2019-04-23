Problem C. Scrambled Words
This contest is open for practice. You can try every problem as many times as you like, though we won't keep track of which problems you solve. Read the Quick-Start Guide to get started.
Small input
18 points   
Solve C-small
Large input
30 points   
Solve C-large
Problem
Professor Scrmable noticed spelling mistakes in a research paper she was reviewing, but she had no difficulty in reading or understanding the words. Upon doing some research, she found an interesting article as described below:

According to a study at an English University, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the correct place. The rest can be a total mess and you can still read it without a problem. This is because the human mind does not read every letter by itself but the word as a whole.

Or rather ...

Aoccdrnig to a study at an Elingsh uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the corecrt pclae. The rset can be a toatl mses and you can sitll raed it wouthit a porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe.

Professor Scrmable wants to explore this concept further and starts compiling different sentences containing similarly scrambled words to send to a popular publication. Unfortunately, the space key on the professor's keyboard is not working, so she has produced one long string of characters. She has asked you to determine how many of the words in her dictionary appear (at least once) as substrings in the long string of characters, either in their original or scrambled forms. (A scrambled form consists of the same set of letters with the first and last letters in the same places, and the others in any order.)

Note that a dictionary word can appear multiple times in the string (though it should be counted only once since we only need to know whether it shows up at least once). For example, if we had the word this in the dictionary, the possible valid words which would be counted are this (original version) and tihs (scrambled version), whereas tsih, siht and other variations are not valid since they do not start with t and end with s. Also, tis, tiss, and thiss are not scrambled forms, because they are not reorderings of the original set of letters.

Since the professor is extremely busy, she gives this task to you, her favorite and most trusted research assistant. Given a dictionary, can you count the number of words in the dictionary that appear as a substring in the professor's string at least once, in either their scrambled or original forms.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each testcase contains three lines. The first line contains an integer L. The second line contains a list of L words made of lowercase English letters; these make up the dictionary. The third line contains two lowercase English letters S1 and S2, and five integers N, A, B, C and D. S1 and S2 are the first two characters of the professor's string S, N is the length of S, and the other four integers are parameters that you should use to generate the characters of S, as follows:

First we define ord(c) as the decimal value of a character c and char(n) as the character value of a decimal n. For example, ord('a') = 97 and char(97) = 'a'. You can refer to ASCII table for other conversions. 

Now, define x1 = ord(S1), x2 = ord(S2). Then, use the recurrence below to generate xi for i = 3 to N:

xi = ( A * xi-1 + B * xi-2 + C ) modulo D.
We define Si = char(97 + ( xi modulo 26 )), for all i = 3 to N.
Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of words from the dictionary that appear (in their original or scrambled forms, as defined above) as substrings of the given string.

Limits
1 ≤ T ≤ 20.
No two words in the dictionary are the same.
Each word in the dictionary is between 2 and 105 letters long, inclusive.
The sum of lengths of all words in the dictionary does not exceed 105.
S1 and S2 are lowercase English letters.
0 ≤ A ≤ 109.
0 ≤ B ≤ 109.
0 ≤ C ≤ 109.
1 ≤ D ≤ 109.
Small dataset
1 ≤ L ≤ 1000.
2 ≤ N ≤ 1000.
Large dataset
1 ≤ L ≤ 20000.
2 ≤ N ≤ 106.
Sample

Input 
    
Output 
 
1
5
axpaj apxaj dnrbt pjxdn abd
a a 50 1 1 1 30

Case #1: 4

In Sample Case #1, using the generation method, the generated string S is aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt. Scrambled or original occurences of dictionary words are highlighted as follows:
axpaj occurs in its scrambled form as aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt.
apxaj occurs in its scrambled form as aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt. Note that even though apxaj is the scrambled form of another dictionary word axpaj, both should be counted.
dnrbt occurs twice in its original form as aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt, though it should be counted only once.
pjxdn occurs in its scrambled form as aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt. Note this occurence overlaps with occurence of another dictionary word, but still they're counted independently.
abd doesn't occur at all.
Note: We do not recommend using interpreted/slower languages for the Large dataset of this problem.


----


问题
Scrmable教授在她正在审阅的研究论文中发现了拼写错误，但她在阅读或理解这些词语方面没有任何困难。做了一些研究后，她发现了一篇如下所述的有趣文章：

根据英国大学的一项研究，一个单词中的字母的顺序无关紧要，唯一重要的是第一个和最后一个字母位于正确的位置。其余的可能是一团糟，你仍然可以毫无问题地阅读它。这是因为人类思维本身并不是每个字母都读，而是整个单词。

更确切地说 ...

Aoccdrnig在Elingsh uinervtisy进行的一项研究中，它似乎并没有让人感觉更糟糕的是，这个笨拙的iprmoetnt tihng是第一个，而lsat ltteer是在corecrt pclae。 rset可以是一个toatl mses，你可以坐下来讨论它的问题。 Tihs是bcuseae huamn mnid deos不是由istlef攻击ervey lteter，而是作为wlohe的wrod。

Scrmable教授希望进一步探索这个概念，并开始编写包含类似扰乱词的不同句子，以发送给一个受欢迎的出版物。不幸的是，教授键盘上的空格键不起作用，因此她制作了一长串字符。她要求你确定她的字典中有多少单词出现（至少一次）作为长字符串中的子字符串，无论是原始字符还是乱码形式。 （乱码形式由同一组字母组成，其中第一个和最后一个字母位于相同位置，其他字母按任意顺序排列。）

请注意，字典单词可以在字符串中多次出现（尽管它应该只计算一次，因为我们只需要知道它是否至少出现一次）。例如，如果我们在字典中有单词this，那么可能计算的有效单词是（原始版本）和tihs（加扰版本），而tsih，siht和其他变体无效，因为它们不是以t并以s结束。此外，tis，tiss和thiss不是乱码形式，因为它们不是原始字母集的重新排序。

由于教授非常忙碌，她将这项任务交给你，她最喜欢和最值得信赖的研究助理。给定一个字典，你可以计算字典中的字数，这些字在教授的字符串中至少出现一次子字符串，无论是乱码形式还是原始形式。

输入
输入的第一行给出了测试用例的数量，T。T测试用例如下。每个测试用例包含三行。第一行包含整数L.第二行包含由小写英文字母组成的L​​个单词列表;这些构成了字典。第三行包含两个小写的英文字母S1和S2，以及五个整数N，A，B，C和D. S1和S2是教授的字符串S的前两个字符，N是S的长度，另外四个整数是您应该用于生成S字符的参数，如下所示：

首先，我们将ord（c）定义为字符c的十进制值，将char（n）定义为小数n的字符值。例如，ord（'a'）= 97和char（97）='a'。您可以参考ASCII表进行其他转换。

现在，定义x1 = ord（S1），x2 = ord（S2）。然后，使用下面的重复生成i = 3到N的xi：

xi =（A * xi-1 + B * xi-2 + C）模D.
对于所有i = 3到N，我们定义Si = char（97 +（xi modulo 26））。
产量
对于每个测试用例，输出一行包含Case #x：y，其中x是测试用例编号（从1开始），y是出现的字典中的单词数（以原始或加扰形式，如上所定义） ）作为给定字符串的子字符串。