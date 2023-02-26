class Node:
	def __init__(self, data, link=None):
		self.data = data
		self.link = link


def add(lnkNodes,val):
    tmp = Node(val)
    tmp.link = lnkNodes
    lnkNodes = tmp
    return lnkNodes
    


    


def printLinkedNodes(lnkNodes):
    cn =lnkNodes
    while cn != None:

        print(cn.data,end=" ")
 
        cn = cn.link
    print()

def addBackNode(lnkNodes, val):
    tmp = Node(val)
    cn = lnkNodes
    while cn.link!= None:
   
        cn = cn.link
        
    cn.link=tmp
 
    return lnkNodes

# unable to add first node, how can we manage it	
def removeNode(lnkNodes, val):
    cn = lnkNodes
    if cn.data !=val:
        while cn.link!= None:
            

            if cn.link.data == val:
                tmp = cn.link
                cn.link = tmp.link
                del tmp
                break
            cn = cn.link
        cn =lnkNodes
        return lnkNodes
    else:
        tmp =cn.link
        cn.link =None
        cn=tmp
        del tmp
        return cn

    print()

def le(n):
    a =n
    c =0
    while a!=None:
        c +=1
        a =a.link
    return c

def sort(lnkNodes):
    l =le(lnkNodes)
    j =1
    c =lnkNodes
    while j<=l:
        n =lnkNodes

        while n.link!=None:


            if n.data>n.link.data:


                tmp =n.data
                n.data =n.link.data
                n.link.data =tmp



            

            n =n.link
        j +=1
 
    return lnkNodes
def main():
    nodeSet1 = Node(300000)
    val =add(nodeSet1,12)

    val1 =add(val, 20)
    printLinkedNodes(val1)
    printLinkedNodes(removeNode(val,10000))



    val2 =add(val1,50)

    val3 =add(val2, -10)
    val4 =add(val3, 100)
    #printLinkedNodes(val4)
    printLinkedNodes(val4)
    z =removeNode(val4,100)




    printLinkedNodes(sort(z))

main()

