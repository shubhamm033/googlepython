# d={'s':1,'p':2,'d':4}
# string1='l l l s s s d f f f'
# words= string1.split()
# print(words)
# for word in words:
#     if word in d:
#         d[word]=d[word]+1
#     else:
#         d[word]=1
# print(d)

# k=d.keys()

# g=d.values()
# print(k)
# print(g)


filename='test.txt'

file=open(filename,'r')
##### read whole file line by line...
#f= file.readlines()
#print(f)

#### print the whole file in one string..Conveinient when we need whole file at a time. 
txt=file.read()
print(txt)
# for line in file:
#     print line
    
#     new_line=line.split()
#     #print
#     for word in new_line:
#        print word 
    