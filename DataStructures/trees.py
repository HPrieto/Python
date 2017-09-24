print("Traversals types of Binary Tree")

print("				D				")
print("		B 				F 		")
print("A 		C 		E 		G 	")

print("Preorder Traversal")
print("Visits a tree's root node and then traverses the left")
print("subtree and the right subtree in a similar manner.\n\n")
print("Order: D -> B -> A -> C -> F -> E -> G\n\n\n\n")


print("Inorder Traversal")
print("Traverses the left subtree, visits the root node, and")
print("traverses the right subtree.")
print("This process moves as far to the left in the tree as possible")
print("before visiting a node.")
print("Order: A -> B -> C -> D -> E -> F -> G\n\n\n\n")

print("Postorder Traversal")
print("Traverses the left subtree, traverses the right subtree,")
print("and visits the root node.")
print("Order: A -> C -> B -> E -> G -> F -> D\n\n\n\n\n")

print("Level Order Traversal")
print("Beginning with level 0, the level order traversal algorithm")
print("visits the nodes at each level in left-to-right order.")
print("Order: D -> B -> F -> A -> C -> E -> G\n\n\n\n\n\n")


from linkedbst import LinkedBST

tree = LinkedBST()
print("Adding D B A C F E G")
tree.add("D")
tree.add("B")
tree.add("A")
tree.add("C")
tree.add("F")
tree.add("E")
tree.add("G")

# Display the structure of the tree
print("\nTree Structure:\n")
print(tree)



print("\n\nRemoving items fron Binary Search Tree:")
print("Process:")
print(" 1.) Save reference to root node")
print(" 2.) Locate node to be removed, its parent, and its parent reference to this node")
print(" 3.) If the child has a left and right subchild,")
print("      Replace node's value with value of greatest subtree value")
print(" 4.) If node has only one child, replace node value with childs value")
print(" 5.) Reset the root node to the saved reference.")
print(" 6.) Decrement the size of the tree and return deleted item \n\n")

print("Further understanding of step 3:")
print(" 1.) Search root nodes left subtree for the node with largest value.")
print("     (Rightmost node in subtree)")
print(" 2.) Replace root nodes value with greatest value node")

print("\n\n\nIntroduction to Grammars")
print("Grammars consist of:")
print(" 1.) Vocab (words and symbols)")
print(" 2.) Syntax Rules")
print(" 3.) Semantic Rules (Specify how sentences in a language should be interpreted. \n\n")

print("Terminal Symbols: +, -, /, *")
print("Metasymbols: '', =, [], {}, (), |\n\n\n")

print("Recognizing, Parsing, and Interpreting Sentences in a Language")
print("Recognizer: Determines if a sentence is from a given language\n\n")
print("Parser: Has the features of a recognizer, but returns information about")
print("        the syntactic structure of the sentence\n\n")
print("Interpreter: Carries out the actions specified by the sentence\n\n\n")

print("Lexical Analysis and the Scanner:")
print("Scanner: Recognizes symbols and assigns task at a low level")
print("         Also, outputs error messages.\n\n")
print("Lexical Analysis: Individual words are picked out of a stream of characters.")
print("					 Whether characters go together to form words.\n\n")
print("Tokens: Output of the scanner and become input to syntax analyzer.\n\n")
print("Syntax Analyzer: Uses the tokens and the grammar rules to determine whether the program is")
print(" 				syntactically correct.")
print(" 				Whether words go together to form sentences.\n\n\n\n\n")

print("Parsing Strategies")
print("Recursive Descent Parsing: Defines a function for each rule in the grammar.\n\n")






































