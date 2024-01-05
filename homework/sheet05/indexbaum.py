from random import shuffle,randint
def print_indextree(tree):
    indent = "    "
    def rec_print_indextree(tree, depth):
        if not tree:
            return
        links, wurzel, rechts = tree
        rec_print_indextree(rechts, depth + 1)
        print(depth * indent, wurzel)
        rec_print_indextree(links, depth + 1)
    rec_print_indextree(tree, 0)

def random_indextree(n):
    def rec_random_tree(L):
        if len(L)==0:
            return []
        else:
            shuffle(L)
            i=L.pop()
            m=randint(0,len(L))
            return [rec_random_tree(L[0:m]),i,rec_random_tree(L[m:])]
    return rec_random_tree(list(range(n)))

def is_indextree(n,tree):
    def get_list(t):
        if not type(t)==list:
            return False
        elif t==[]:
            return t
        elif not len(t)==3:
            return False
        elif not type(t[1])==int:
            return False
        else:
            r=t[1]
            (left,right)=(get_list(t[0]),get_list(t[2]))

            if left==False or right==False:
                return False
            elif r in left or r in right or \
                    not set(left).isdisjoint(set(right)):
                        return False
            else:
                return left+[r]+right
    L=get_list(tree)
    if type(L)==list:
        return set(L)==set(range(n))
    else:
        return False
    
def size(tree):
    return 0 if tree==[] else 1+size(tree[0])+size(tree[2])

def inorder(tree):
    if tree==[]:
        return []
    else:
        links,wurzel,rechts=tree
        return inorder(links)+[wurzel]+inorder(rechts)
    