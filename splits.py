# str='This is my day'
# #p=str.split()
# #print(p)
# k=str.find('day')
# print(k)
# q=str.find('my')
# print(q)
# q=q+1
# print(str[k:])
# print(str.replace(str[k:q],'good'))


# def not_bad(s):
#   # +++your code here+++
#   # LAB(begin solution)
#   n = s.find('not')
#   b = s.find('bad')
#   if n != -1 and b != -1 and b > n:
#     s = s[:n] + 'good' + s[b+3:]
#   return s
# not_bad('i am that good a person')

string1=['apple','rahul','tiwari','madona']
string2=['lol','rofl','love','tiwari']

for steps in string1:
  
  if steps in string2:
    print(string2.index(steps))
  else:
    print(steps)

