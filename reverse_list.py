num_list=[]
rev_list=[]
final_list=[]
while True:
    num=int(input('Enter number :'))
    if(num==0):
        break
    if(num>=99 and num<=999):
        num_list.append(num)
    else:
        print('Enter 3 digit number only.')

for i in num_list:
    rev=0
    while(i>0):
        a=i%10
        rev=rev*10+a
        i=i//10
    rev_list.append(rev)

for i in rev_list:
    final_list.insert(0,i)

print("orignel list :",num_list)
print("After reverse the number :", rev_list)
print("After reverse the list :",final_list)
