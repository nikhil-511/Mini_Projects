
#Convertion of a linked list into a flat list
def flat_list(array):
    output=[]
    def reemovNestings(l):
        for i in l:
            if type(i) == list:
                reemovNestings(i)
            else:
                output.append(i)
    reemovNestings(array)
    
    return output


list1=[1,[2,3],[2],56]
print(flat_list(list1))


"""
def flat_list(l):
    r = []
    def f(l):
        for i in l:
            r.append(i) if type(i) is int else f(i)
    f(l)
    return r
"""
