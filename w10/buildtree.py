# Python program to construct tree using inorder and 
# preorder traversals

# A binary tree node 
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

"""Recursive function to construct binary of size len from
Inorder traversal in[] and Preorder traversal pre[]. Initial values
of inStrt and inEnd should be 0 and len -1. The function doesn't
do any error checking for cases where inorder and preorder
do not form a tree """
def buildTree(inOrder, preOrder, inStrt, inEnd):
	
	if (inStrt > inEnd):
		return None

	# Pick current node from Preorder traversal using
	# preIndex and increment preIndex
	tNode = Node(preOrder[buildTree.preIndex])
	buildTree.preIndex += 1

	# If this node has no children then return
	if inStrt == inEnd :
		return tNode

	# Else find the index of this node in Inorder traversal
	inIndex = search(inOrder, inStrt, inEnd, tNode.data)
	
	# Using index in Inorder Traversal, construct left 
	# and right subtrees
	tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
	tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

	return tNode

# UTILITY FUNCTIONS
# Function to find index of value in arr[start...end]
# The function assumes that value is present in inOrder[]

def search(arr, start, end, value):
	for i in range(start, end + 1):
		if arr[i] == value:
			return i

def printPostorder(node):
    if node is None:
        return
    printPostorder(node.left)
    
    printPostorder(node.right)
    
    print(node.data, end=' ')

def printInorder(node):
	if node is None:
		return
	
	# first recur on left child
	printInorder(node.left)
	
	# then print the data of node
	print (node.data,end=' ')

	# now recur on right child
	printInorder(node.right)
	
# Driver program to test above function
inOrder = [25, 22, 21, 20, 19, 17, 14, 13, 12, 11, 10]
preOrder = [19, 22, 25, 20, 21, 13, 17, 14, 11, 12, 10]
# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)

# Let us test the build tree by printing Inorder traversal
print ("Inorder traversal of the constructed tree is")
printInorder(root)
print ("Postorder traversal of the constructed tree is")
printPostorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
