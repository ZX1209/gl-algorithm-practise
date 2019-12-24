# leetcode-5055-困于圆中的机器人.py  显示英文描述
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Easy
# 在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：

# "G"：直走 1 个单位
# "L"：左转 90 度
# "R"：右转 90 度
# 机器人按顺序执行指令 instructions，并一直重复它们。

# 只有在平面中存在圆使得机器人永远无法离开圆时，返回 true。否则，返回 false。

# 示例 1：

# 输入："GGLLGG"
# 输出：true
# 解释：
# 机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
# 重复指令时，机器人将保持在以原点为中心，2 为半径的圆中。
# 示例 2：

# 输入："GG"
# 输出：false
# 解释：
# 机器人无限向北移动。
# 示例 3：

# 输入："GL"
# 输出：true
# 解释：
# 机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动。

# 提示：

# 1 <= instructions.length <= 100
# instructions[i] 在 {'G', 'L', 'R'} 中


class Solution:

    def isRobotBounded(self, instructions: str) -> bool:
        lastPos = [0, 0]
        angles = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        pointer = 0
        outAngle = 0

        for order in instructions:
            if order == 'G':
                lastPos[0] += angles[pointer % 4][0]
                lastPos[1] += angles[pointer % 4][1]

                print(lastPos)
            elif order == 'L':
                pointer += 1
            elif order == 'R':
                pointer -= 1

        if lastPos[0] == lastPos[1] == 0:
            return True
        elif pointer%4 == 0:
            return False
        elif 

        return True


if __name__ == "__main__":
    test = Solution()
    print(
        test.isRobotBounded(
            "RRGRRGLLLRLGGLGLLGRLRLGLRLRRGLGGLLRRRLRLRLLGRGLGRRRGRLG"))
