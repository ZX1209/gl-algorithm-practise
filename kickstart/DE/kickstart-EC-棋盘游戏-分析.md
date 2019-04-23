棋盘游戏：分析
小数据集
鉴于Bala将随机统一选择分布，Bahu需要确定最佳的卡片分布。在Small数据集中，N = 3，所以只有9个！ / 3！ / 3！ / 3！ = 1680种不同的方式让玩家分发他们的牌。 （如果存在多个具有相同强度值的卡，则这些分布中的一些可能实际上是等同的，但是为了简单起见，我们将它们视为不同。）我们可以枚举Bahu的所有1680个可能的分布Ui，以及所有1680个可能的分布Aj巴拉。 （这些变量以玩家姓名的最后一个字母命名。）对于每个Ui，我们找到所有失去该Ui的Aj的分数。最大的这样的分数是我们的答案。时间复杂度是小常数因子的16802倍。

大数据集
在大数据集中，有可能N = 5.在这种情况下，有15个！ / 5！ / 5！ / 5！ = 756756个不同的发行版。我们不能使用7567562时间因素的上述策略。

只有三个战场中牌的总和很重要;让他们成为Bahu的U1，U2，U3和Bala的A1，A2，A3。如果满足以下至少两个不等式，则Bahu获胜：U1> A1，U2> A2，U3> A3。

我们可以通过使用包含 - 排除原则来处理该标准的“至少两个”部分。然后，对于每个Ui：

满足上述标准的Aj的数量=
满足U1> A1和U2> A2 +的Aj数
满足U1> A1和U3> A3 +的Aj数
满足U2> A2和U3> A3的Ajs数量 - 
2×满足U1> A1且U2> A2且U3> A3的Aj数。

这些数量中的最后一个是最难计算的数量。在这里我们需要另一个观察，即所有U1，U2，U3只有15个选择5 = 3003种不同的可能性。我们可以标记这些可能性1到3003。

这是一个三维查询，但是我们可以通过按U1的递增顺序处理Us来删除1维，并且还可以按A1的递增顺序预处理As。之后，我们可以创建一个二维分段树来存储A1 <U1的所有（A2，A3）。我们可以找到所有（A2，A3）s，使得U2> A2和U3> A3在log 3003×log 3003时间复杂度中。上述等式中的其他3个量也可以以类似的方式找到。整体时间复杂度大约为756756×log 3003×log 3003倍的小常数因子，这足以解决这个数据集。


Board Game: Analysis
Small dataset
Bahu needs to determine the best possible card distribution given that Bala will choose a distribution uniformly at random. In the Small dataset, N = 3, so there are only 9! / 3! / 3! / 3! = 1680 different ways for a player to distribute their cards. (If there are multiple cards with the same strength value, some of these distributions may be practically equivalent, but we will treat them as different for simplicity.) We can enumerate all 1680 possible distributions Ui for Bahu, and all 1680 possible distributions Aj for Bala. (These variables are named after the last letters of the players' names.) For each Ui, we find the fraction of all Ajs that lose against that Ui. The largest such fraction is our answer. The time complexity is on the order of 16802 times a small constant factor.

Large dataset
In the Large dataset, it is possible that N = 5. In that case, there are 15! / 5! / 5! / 5! = 756756 different distributions. We cannot use the above strategy with a 7567562 time factor.

Only the sums of the cards in the three battlefields matter; let them be U1, U2, U3 for Bahu and A1, A2, A3 for Bala. Then Bahu wins if at least two of the following inequalities are satisfied: U1 > A1, U2 > A2, U3 > A3.

We can deal with the "at least two" part of that criterion by using the inclusion-exclusion principle. Then, for each Ui:

The number of Ajs satisfying the above criterion =
The number of Ajs satisfying U1 > A1 and U2 > A2 +
The number of Ajs satisfying U1 > A1 and U3 > A3 +
The number of Ajs satisfying U2 > A2 and U3 > A3 -
2 × the number of Ajs satisfying U1 > A1 and U2 > A2 and U3 > A3.

The last of those quantities is the most difficult one to calculate. Here we need another observation that there are only 15 choose 5 = 3003 different possibilities for all U1, U2, U3. We can label these possibilities 1 through 3003.

This is a 3-dimensional query, but we can remove 1 dimension by processing the Us in increasing order of U1 and also preprocessing As in increasing order of A1. After that, we can create a 2-dimensional segment tree to store all (A2, A3)s that have A1 < U1. We can find all (A2, A3)s such that U2 > A2 and U3 > A3 in log 3003 × log 3003 time complexity. The other 3 quantities in the equation above can also be found in a similar way. The overall time complexity is on the order of 756756 × log 3003 × log 3003 times a small constant factor, which is fast enough to solve this dataset.