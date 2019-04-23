Problem B. Lucky Dip
This contest is open for practice. You can try every problem as many times as you like, though we won't keep track of which problems you solve. Read the Quick-Start Guide to get started.
Small input
10 points   
Solve B-small
Large input
19 points   
Solve B-large
Problem
You are participating in the Grand Kickstart Lucky Dip with many fantastic and amazing prizes (and some not so good ones)!

In this Lucky Dip, there is a bag with N items. The i-th item in the bag has value Vi. You will put your hand into the bag and draw one item at random; all items in the bag have an equal probability of being chosen. The organizers want contestants to feel that they have some element of choice, so after you draw an item, you can either keep it, or "redip" by returning it to the bag and drawing again. (Note that the returned item is now just as likely to be chosen as any of the other items in the bag.) You may only redip a maximum of K times. If you use K redips, you must keep the item that you draw on your (K + 1)-th draw.

If you play optimally to maximize the value of the item you will end the game with, what is the expected value of that item?

Input
The input starts with one line containing one integer T: the number of test cases. T test cases follow.

Each test case consists of two lines. The first line consists of two integers N and K: the number of items in the bag, and the maximum number of times you may redip. The second line consists of N integers Vi, each representing the value of the i-th item.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the expected value described above. Your answer will be considered correct if it is within an absolute or relative error of 10-6 of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.

Limits
1 ≤ T ≤ 100.
1 ≤ Vi ≤ 109.
1 ≤ N ≤ 20000.
Small dataset
0 ≤ K ≤ 1.
Large dataset
0 ≤ K ≤ 50000.
Sample

Input 
    
Output 
 
5
4 0
1 2 3 4
3 1
1 10 1
3 15
80000 80000 80000
1 1
10
5 3
16 11 7 4 1

Case #1: 2.500000
Case #2: 6.000000
Case #3: 80000.000000
Case #4: 10.000000
Case #5: 12.358400


In Sample Case #1, you cannot redip, so the expected value is just the mean of the items in the bag which is (1 + 2 + 3 + 4) / 4 = 2.5.

In Sample Case #2, the best strategy is to keep the item of value 10 if you get it, and redip otherwise. The chance of getting that item (on either the first or second draw) is 1 - (2/3)2 = 5/9, hence the expected value is (5/9 * 10) + (4/9 * 1) = 6.

In Sample Case #3, since all the items have the same value, it does not matter how many times you redip and hence the expected value is 80000.

Note that cases #3 and #5 would not appear in the Small dataset.


问题
您正在参加Grand Kickstart Lucky Dip，其中包括许多精彩绝伦的奖品（还有一些不太好的奖品）！

在这个Lucky Dip中，有一个包含N个物品的袋子。包中的第i个项目具有值Vi。你会把手伸进袋子里随意抽出一件物品;包中的所有物品都有相同的被选择概率。组织者希望参赛者感觉他们有一些选择的元素，所以在你画一个项目之后，你可以保留它，或者通过将它返回到包并再次绘制来“重新”。 （请注意，返回的项目现在可能与包中的任何其他项目一样。）您最多只能重拨K次。如果您使用K红色，则必须保留您在第（K + 1）个平局上绘制的项目。

如果您以最佳方式进行游戏以最大化项目的价值，您将结束游戏，该项目的预期价值是多少？

输入
输入以包含一个整数T的一行开始：测试用例的数量。 T测试案例如下。

每个测试用例包含两行。第一行包含两个整数N和K：包中的项目数，以及您可以重拨的最大次数。第二行由N个整数Vi组成，每个整数表示第i个项的值。

产量
对于每个测试用例，输出一行包含Case #x：y，其中x是测试用例编号（从1开始），y是上述期望值。如果在正确答案的10-6的绝对或相对误差范围内，您的答案将被视为正确。请参阅常见问题解答，了解其含义以及我们接受的实数格式。