
# coding: utf-8

# In[6]:


a = int(input())
b = int(input())

count = 0
for i in range(a, b+1):
    if i%8!=0:
        continue
    count+=1
print(count)


# In[32]:


### tổng của n số tự nhiên đầu tiên chia hết cho k
n = int(input())
k = int(input())

count = 0
tong = 0
m=n
for i in range (0,m):
    if count < n and i%k==0:
        tong = tong + i
        count+=1
        print(i)
        print(m)
        print(n)
    m+=1
print(tong)


# In[11]:


s = input()

count = 0
for i in s:
    if i.isalpha()==0:
        continue
    count+=1
print(count)


# In[48]:


### tổng của n số tự nhiên đầu tiên chia hết cho k
n = int(input())
k = int(input())

count = 0
tong = 0

i=0
while count < n:
    if i%k==0:
        tong = tong + i
        count+=1
    i+=1
print(tong)


# In[44]:


n = int(input())
my_list = []
for i in range(0,n):
    my_list.append(int(input()))
    
count = 0
for j in range(0,len(my_list)):
    if my_list[j] < 10:
        count+=1
        print('iiii:',my_list[j])

print(count)
print(my_list)


# In[47]:


for i in "123":
    print(i)


# In[49]:


n = int(input())

tong = 0
for i in str(n):
    tong += int(i)

print(tong)


# In[26]:


chuoi = input()
l=len(chuoi)
mid=l//2
stat = 'YES'
#print(mid)
for i in range(0,l):
    j=l-1
    #print(chuoi[i],'-',chuoi[j])
    #print(i,'-',l)
    if chuoi[i] != chuoi[j]:
        stat='NO'
        break
    l-=1
    
    if(i==(mid-1)):
        break
print(stat)


# In[1]:


chuoi = input()
l=len(chuoi)
print(chuoi[l-1])


# In[16]:


chuoi = input()
l=len(chuoi)
mid=l//2
print(mid)


# In[47]:


n=int(input())
f1=n-1
crong=n*2
h1=''
sl=0

def themsao(slsao):
    sao=''
    for i in range(0,slsao):
        sao+='*'
    return sao

for j in range(0,n):    
    for i in range(0,crong):
        if(i<=f1):            
            if(i==f1):
                h1+='*'
                h1+=themsao(sl)
            else:
                h1+=' '
    print(h1)
    f1=f1-1
    h1=''
    sl+=2

