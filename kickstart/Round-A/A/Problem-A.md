Problem A. Even Digits
This contest is open for practice. You can try every problem as many times as you like, though we won't keep track of which problems you solve. Read the Quick-Start Guide to get started.
Small input
8 points    
Solve A-small
Large input
15 points   
Solve A-large
Problem
Supervin has a unique calculator. This calculator only has a display, a plus button, and a minus button. Currently, the integer N is displayed on the calculator display.

Pressing the plus button increases the current number displayed on the calculator display by 1. Similarly, pressing the minus button decreases the current number displayed on the calculator display by 1. The calculator does not display any leading zeros. For example, if 100 is displayed on the calculator display, pressing the minus button once will cause the calculator to display 99.

Supervin does not like odd digits, because he thinks they are "odd". Therefore, he wants to display an integer with only even digits in its decimal representation, using only the calculator buttons. Since the calculator is a bit old and the buttons are hard to press, he wants to use a minimal number of button presses.

Please help Supervin to determine the minimum number of button presses to make the calculator display an integer with no odd digits.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line containing an integer N: the integer initially displayed on Supervin's calculator.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of button presses, as described above.

Limits
1 ≤ T ≤ 100.
Small dataset
1 ≤ N ≤ 105.
Large dataset
1 ≤ N ≤ 1016.
Sample

Input 
    
Output 
 
4
42
11
1
2018

Case #1: 0
Case #2: 3
Case #3: 1
Case #4: 2

In Sample Case #1, the integer initially displayed on the calculator has no odd digits, so no button presses are needed.

In Sample Case #2, pressing the minus button three times will cause the calculator to display 8. There is no way to satisfy the requirements with fewer than three button presses.

In Sample Case #3, either pressing the minus button once (causing the calculator to display 0) or pressing the plus button once will cause the calculator to display an integer without an odd digit.

In Sample Case #4, pressing the plus button twice will cause the calculator to display 2020. There is no way to satisfy the requirements with fewer than two button presses.



----



问题
Supervin有一个独特的计算器。此计算器只有一个显示，一个加号按钮和一个减号按钮。目前，整数N显示在计算器显示器上。

按加号按钮可将计算器显示屏上显示的当前数字增加1.同样，按减号按钮可将计算器显示屏上显示的当前数字减1.计算器不会显示任何前导零。例如，如果计算器显示屏上显示100，则按减号按钮一次将使计算器显示99。

Supervin不喜欢奇数，因为他认为他们是“奇怪的”。因此，他只想使用计算器按钮显示十进制表示中只有偶数位的整数。由于计算器有点旧并且按钮难以按下，因此他希望使用最少数量的按钮按下。

请帮助Supervin确定按下按钮的最小次数，以使计算器显示没有奇数位的整数。

输入
输入的第一行给出了测试用例的数量，T。T测试用例如下。每个都以一行包含整数N开始：最初显示在Supervin计算器上的整数。

产量
对于每个测试用例，输出一行包含Case #x：y，其中x是测试用例编号（从1开始），y是按下按钮的最小次数，如上所述。


