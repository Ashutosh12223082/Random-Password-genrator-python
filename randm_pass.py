import random
list1 = []
for i in range(ord("A"),ord("Z")+1):
    list1.append(chr(i))
    list1.append(chr(i).lower())
print(list1)
num=["1","2","3","4","5","6","7","8","9",'0']
symbols=['!','@',"#","$",'%',"^","&","*","(",")","_","+"]
print("welcome to password generator")
n_lt=int(input("enter no of letters in password: "))
n_S=int(input("no of sym in password: "))
n_n=int(input("no of num in password: "))
password_list=[]
for char in range(1,n_lt+1):
    password_list.append(random.choice(list1))
for char in range(1,n_S+1):
    password_list.append(random.choice(symbols))
for char in range(1,n_n+1):
    password_list.append(random.choice(num))
random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print(password)