---
title: Tree
tags: dataStructures,intermediate,recursion,tree,functions
---
It creates a tree dataStructure and support main operations insert,delete,traversals
in addition to some utility funcs: finding max depth,symetric bst and validation of bst

-create instance of the class Tree
-insert nodes
-do any operation

```py
#Create tree node
class Tree:
	#Creating a node at any instance
	def __init__(self,val):
		self.left=None
		self.right=None
		self.val=val
	#Inserting in a tree (bst)
	def insert(self,val):
		if(self.val):
			if(val<self.val):
				if(self.left is None):
					self.left=Tree(val)
				else:
					#Call the function recursively untill the left node is Null
					self.left.insert(val)
			elif(val>self.val):
				if(self.right is None):
					self.right=Tree(val)
				else:
					self.right.insert(val)
			else:
				self.val=val
#Traversing and printing tree nodes in three methods (inorder(left_Root_right),preorder(Root_left_right),postorder(left_right_Root))
#The values are printed in the same line since we use end=" "
#Inorder traversal we return a list so we can use it in validation of bst
def inorder(root):
	res=[]
	if(root):
		res=inorder(root.left)
		res.append(root.val)
		res+=inorder(root.right)
	return res

def preorder(root):
	if(root):
		print(root.val,end=" ")
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if(root):
		postorder(root.left)
		postorder(root.right)
		print(root.val,end=" ")

#A function that return the min node in the tree
def minNode(root):
	current=root
	#keep going through left nodes untill we get a node whose left is null
	while(current.left):
		current=current.left
	return current
#Delete a node with a given key
def delete(root,key):
	if(root is None):
		return root
	#if key is less than the root val the look at the left <- untill find the key
	if(key<root.val):
		root.left=delete(root.left,key)
	#Case bigger than look at right ->
	elif(key>root.val):
		root.right=delete(root.right,key)
	#Case finding the key
	else:
	#if the node has only on child or less
		if(root.left is None):
			temp=root.right
			root=None
			return temp
		elif(root.right is None):
			temp=root.left
			root=None
			return temp
	#if the node has 2 children
		#copy the value of the right minimum node to the key root then delete the right min node (inorder successor)
		temp=minNode(root.right)
		root.val=temp.val
		root.right=delete(root.right,temp.val)
	return root

#A function to check if the tree is a valid bst or not (ret:Bool)
def validate(root):
	tree=inorder(root)
	return all(tree[i]<tree[i+1] for i in range(len(tree)-1))

#A function to return the max depth or the height of the tree.
#Note:The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
def maxDepth(root):
	if(root is None):
		return 0
	else:
		lDepth=maxDepth(root.left)
		rDepth=maxDepth(root.right)
	return max(lDepth,rDepth)+1

#A function check wheather the tree is symetric (mirror)or not
def isSymetric(root):
	def checker(node1,node2):
		if(node1 is None and node2 is None):
			return True
		else:
			if(node1 and node2):
				if(node1.val==node2.val):
					return checker(node1.left,node2.right) and checker(node1.right,node2.left)
		return False
	if(root is None):
		return True
	else:
		return checker(root.left,root.right)
```
```py
root = Tree(50)
root.insert(20) 
root.insert(40)
root.insert(80)
print('inorder')
print(inorder(root))
print('\ninorder after deleting 40')
print(inorder(root))
print(validate(root))
print(maxDepth(root))
print(isSymetric(root))
```
