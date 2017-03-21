# coding=utf-8


class Solution:
    # target字符串在source出现的位置
    def find_str(self, source, target):
        if source is None or target is None:
            return -1
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i+j] != target[j]:
                    break
            else:
                return i
        return -1


# 统计字频是否一样
# python直接:sorted(s1) == sorted(s2)
class Anagram:
    # 判断s1和s2词频是否一致
    def is_anagram(self, s1, s2):
        l = [0 for x in range(255)]
        for char in s1:
            l[ord(char)] += 1
        for char in s2:
            if l[ord(char)] == 0:
                return False
            l[ord(char)] -= 1
        return True if sum(l) == 0 else False

    # 判断s1是否包s2里面的所有元素
    def is_contain(self, s1, s2):
        assert len(s1) > len(s2), 's1 must be longer than s2'
        d = {}
        for char in s1:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for char in s2:
            if char not in d or d[char] == 0:
                return False
            d[char] -= 1
        return True

    # 判断[str1,str2,...]是否词频一样
    def all_is_anagrams(self, strs):
        for s in strs[1:]:
            if self.is_anagram(strs[0], s) is False:
                return False
        return True


# 根据offset的次数，翻转s
def reverse(offset, s):
    if len(s) == 1:
        return s
    while offset:
        s = s[-1] + s[:-1]
        offset -= 1
    return s

if __name__ == '__main__':
    print reverse(3, 'abcdfeds')

