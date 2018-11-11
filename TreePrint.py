
#Ryan Singh
import random
class list(object):
    def __init__(self):
        self.data=0
        self.next1=None
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = random.randint(10,99)
        self.height = 0
    def inc_height(self):
        if self.left is not None:
            self.left.inc_height()
            self.right.inc_height()
            self.height=self.left.height+1

    def child_print(self):
        ret1 = ""
        if self.left is not None:
            ret1 = self.left.data
        if self.right is not None:
            ret1 = ret1, self.right.data
        return ret1
    def tree_print(self):
        print (("  .")*(self.height),str(self.data))
        if self.left is not None:
                self.left.tree_print()
    def min(self):
        if self.left is None:return
        if self.left.data<self.right.data: return self.left
        else : return self.right
    def max(self):
        if self.left is None:return
        if self.left.data>=self.right.data: return self.left
        else : return self.right
    def min_max(self):
        path ="root:"+str(self.data)
        next1=self
        while next1.left is not None:
            next1 = next1.min()
            path = path +"\n min:" + str(next1.data)
            if  next1.left is not None:
                next1 = next1.max()
                path = path + "\n max:" + str(next1.data)
        return path
def tree_build(x):
    current =Tree()
    if x == 0:
        return Tree()
    else:
        current.left = tree_build(x - 1)
        current.right = tree_build(x - 1)
        return current
print
main = tree_build(3)
main.inc_height()
print (main.min_max())
print
print("Tree\n"+"       ",main.height,"        ", main.data)
print ("            ",main.child_print())
print ("   ",main.left.child_print(),"        ",main.right.child_print())
print  (main.left.left.child_print(),main.left.right.child_print(),main.right.left.child_print(),main.right.right.child_print())
print ('\n',"output:\n" ,main.min_max())
main.tree_print()
