'''list'''

'''a=[10,2.3,True,'Hello']
a.append(10)
print(a)
a.remove(True)
print(a)'''
'''a.pop(0)
print(a)
'''
'''
a=(10,2.3,5j,True,)
print(a,type(a))'''

'''dict'''


'''a={{1:2}}
print(a)'''


'''a={'a':[10,20,30,40],'b':40}
print(a['a'][1])'''


'''a='HELLO'
print(a[-2:-4-1:-1])
print(a[::-1])'''
a='Good Morning'
'''print(a[1:5+1:2])
print(a[5:11+1:3])
print(a[-7::3])
print(len(a[-2:-8-1:-3]))
'''

'''a=float(input("enter:"))
print(type(a))'''

'''a=int(input("enter:"))
if a%2==0:
    print('even')
else:
    print('odd')
'''

'''l=eval(input("enter list:")) 
if len(l)==5:
    print('yes')
else:
    print('no')
'''
'''
ch=input("enter:")
if "A" <=ch<="Z":
    print('upper')
elif "a" <=ch<='z':
    print("lower")
else:
    print("not an alpha")'''



'''un=input('enter:')
if un=='heroine':
    print('correct username')
    pw=input('enter:')
    if pw=='hi@123':
        print('successful login')
    else:
        print('incorrect pw')
else:
    print('incorrect un')
'''
'''i=1
while i<=100:
    print(i)
    i+=1
    '''
'''i = 2
while i<=50:
    print(i)
    i+=2'''

'''n=int(input("enter number:")) 
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
    print(rev)'''

'''for i in range(1,101):
    print(i)'''

'''for i in range(1,51):
    if i%2==0:
        print(i,)'''

'''l =[10,20,30]
for i in l:
    print(i)'''

'''s=input("enter:")
out=''
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif 'a' <=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=i
        print(out)'''

'''s=input("enter:")
rev=''
for i in s:
    rev=i+rev
    print(rev)
    '''

'''for i in range(1,6):
    for j in range(1,6):
       print('*',end='')
print()'''

'''for i in range(1,6):
    for j in range (1,6):
          if i > j:
               print('1',end=' ')
          else:
            print('@',end=' ')
    print()'''


for i in range(1,6):
     for j in range (1,6):
          if i == j:
               print('1',end=' ')
          else:
            print('@',end=' ')
     print()
               