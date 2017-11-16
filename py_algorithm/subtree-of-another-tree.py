class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


s1 = TreeNode(3)
s2 = TreeNode(4)
s3 = TreeNode(5)
s4 = TreeNode(1)
s5 = TreeNode(2)
s1.left = s2
s1.right = s3
s2.left = s4
s2.right = s5

t1 = TreeNode(4)
t2 = TreeNode(1)
t3 = TreeNode(2)
t1.left = t2
t1.right = t3


class Solution(object):
    def isSubtree(self, s, t):
      tree1 = self.preorder(s, True)
      tree2 = self.preorder(t, True)
      return tree2 in tree1
    
    def preorder(self, t, left):
      if not t:
        if left:
          return "lnull"
        else:
          return "rnull"
      
      return "#"+str(t.val) + " " +self.preorder(t.left, True)+" " +self.preorder(t.right, False)


class Solution2(object):
    def isSubtree(self, s, t):
      return self.traverse(s,t)
    
    def traverse(self, s, t):
      return  s!=None and ( self.equals(s,t) or self.traverse(s.left,t) or self.traverse(s.right,t))
    
    def equals(self, s, t):
      if s==None and t==None:
        return True
      if s==None or t==None:
        return False
      return s.val==t.val and self.equals(s.left,t.left) and self.equals(s.right,t.right)


print Solution().isSubtree(s1, t1)
print Solution2().isSubtree(s1, t1)