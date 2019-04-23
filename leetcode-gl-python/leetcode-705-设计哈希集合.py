# leetcode-705-设计哈希集合.py
# 不使用任何内建的哈希表库设计一个哈希集合

# 具体地说，你的设计应该包含以下的功能

# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

# 示例:

# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // 返回 true
# hashSet.contains(3);    // 返回 false (未找到)
# hashSet.add(2);          
# hashSet.contains(2);    // 返回 true
# hashSet.remove(2);          
# hashSet.contains(2);    // 返回  false (已经被删除)

# 注意：

# 所有的值都在 [1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。



class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key not in self.set:
            self.set.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.set:
            self.set.remove(key)
        

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.set = [[] for _ in range(self.size)]

    def _hash(self,val):
        return val%self.size

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):
            self.set[self._hash(key)].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            self.set[self._hash(key)].remove(key)

        

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.set[self._hash(key)]


执行用时为 96 ms 的范例
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._hash_set = set()
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self._hash_set.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self._hash_set:
            self._hash_set.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self._hash_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)