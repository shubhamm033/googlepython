loo=[(1,2,6),(1,4,5),(7,8,9)]
def lastelement():
    list=[]
    for tuple in loo:
        
        n=tuple[-1]
        list.append(n)
    list.sort()
        
    return list
    
print(sorted(loo,key=list))