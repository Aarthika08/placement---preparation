# Example :
# Sample Test Case
# Input :
# Move#Hash#to#Front
# Output :
# ###MoveHashtoFront

# n=input()
n='Move#Hash#to#Front'
count=0
for i in n:  
    if i=='#':
        count+=1
        k= n.replace('#', '')
        
print('#'*count,end='')  
print(k)        
