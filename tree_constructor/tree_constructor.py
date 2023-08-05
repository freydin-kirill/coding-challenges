def TreeConstructor(strArr):
    # Initialize empty lists to store nodes and their relationships
    root = []
    parents = []
    children = []

    # Loop through the input list of relationships between nodes
    for node in strArr:
        # Evaluate the relationship into child and parent
        child, parent = eval(node)

        # Check if a parent has more than two children
        parents.append(parent)
        if parents.count(parent) > 2:
            return 'false'

        # Check if a child has more than two parents
        children.append(child)
        if children.count(child) > 2:
            return 'false'

        # If the child is already marked as a root, remove it from the root list
        if child in root:
            root.remove(child)

        # If the parent is not a child of any other node, mark it as a root
        if parent not in children and parent not in root:
            root.append(parent)

        # Check for cyclic relationships (i.e., child being the parent of its parent)
        if parent in children and child in parents:
            if children.index(parent) == parents.index(child):
                return 'false'

    # After processing all relationships, check if there is exactly one root
    if len(root) != 1:
        return 'false'

    # If everything passes, return true indicating that it's a valid tree
    return 'true'


# Keep this function call here
print(TreeConstructor(input()))
