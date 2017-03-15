# coding=utf-8
import random

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
    return L

# 排序并去重
def quick_sort1(L):
    if len(L) == 0 or len(L) == 1:
        return L
    m = L[0]
    small = [i for i in L if i < m]
    big = [i for i in L if i > m]
    return quick_sort1(small) + [m] + quick_sort1(big)

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def quick_sort4(L, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = L[low]
    # 选定一个基准数
    # 左右扫描，只要未碰头，一轮：
    # 从右开始，右边找到一个比基准数小的，交换
    # 左边开始，找到一个比基准数大的，交换，循环下一轮
    # 基准数归为，处理左右的两段
    while low < high:
        while low < high and L[high] > key:
            high -= 1
        L[low] = L[high]
        L[high] = key
        while low < high and L[low] <= key:
            low += 1
        L[high] = L[low]
        L[low] = key
    quick_sort4(L, left, low-1)
    quick_sort4(L, low+1, right)

# 树遍历
# 构建一个树
class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 遍历
class TreeOrder(object):
    def preorder(self):
        if tree is None:
            return
        print tree.data,
        self.preorder(tree.left)
        self.preorder(tree.right)

    def miorder(self, tree):
        if tree is None:
            return
        self.miorder(tree.left)
        print tree.data,
        self.miorder(tree.right)

    def postorder(self, tree):
        if tree is None:
            return
        self.postorder(tree.left)
        self.postorder(tree.right)
        print tree.data,

'''
完全二叉树——》最小堆：h[n]
特点：每个节点都小于它的子节点
def shiftdown(i节点):
    while i<n/2 and i需要调整：
        跟左右儿子比较，记录下最小的节点t
        如果最小节点不是自己：
            交换 i 和 t
            更新i为t，继续向下
        如果是：
            不需要调整了
def shiftup(i节点）：
    while i 不是顶点 or i需要调整：
        if i值大于父节点：
            交换，更新节点
        if i 小于父节点：
            不需要调整了
创建一个最小堆：从最后一层非叶节点向前，对每个节点shiftdown
堆排序：交换顶点<->最后节点；保存最后节点数值；删除此堆最后节点
'''

def shiftdown(h, i, end=None):
    if not end:
        n = len(h) - 1
    else:
        n = end
    flag = 0
    while 2*i+1 <= n and flag == 0:  # 至少有左儿子
        if h[i] < h[2*i+1]:  # 跟左儿子比较
            t = i
        else:
            t = 2*i+1
        if 2*i+2 <= n and h[t] > h[2*i+2]:  # 如果有右儿子，且右儿子更小
            t = 2*i+2
        if i != t:  # 如果最小的不是自己，交换，并更新节点
            swap(h, i, t)
            i = t
        else:  # 没有子节点，或者自己是最小的，不用调整了
            flag = 1

def create(h):  # 从非叶节点层开始向前调整
    n = len(h)
    for i in range(n//2 -1, -1, -1):
        shiftdown(h, i)

def delmin(h, end):
    t = h[0]
    h[0] = h[end]
    end = end - 1
    shiftdown(h, 0, end)
    return t

# 从小到达排序，每次取堆的顶点，然后交换顶点最后点，调整
def sort_h(L):
    n = len(L) - 1
    for end in range(n, 0, -1):
        print delmin(L, end),


if __name__ == '__main__':
    L = [random.randint(0, 100) for i in range(12)]
    print L
    # print quick_sort4(L, 0, len(L)-1)
    # print L
    # t1 = Tree(8)
    # t2 = Tree(3)
    # t3 = Tree(90, t1, t2)
    # ot = TreeOrder()
    # ot.preorder(t3)
    create(L)
    print L
    sort_h(L)





