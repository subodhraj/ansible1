#!/usr/bin/python3

myname = "subodh"
lname = "chutya"
print(myname)
print(myname.capitalize())
print(myname.upper())
print(myname + " " + lname)

users = ["user1","user2","user3"]

print(users[1])
print(users[-1])
users.append("ram")
print("users" + users[-1])
users.insert(1,"marry")
users.pop
sorter_users = sorted(users)
print(sorter_users)

#loop

for u in users:
    print("username is ",u)
    print("username is ",u.title())

for i in range(1,10):
    print(i)

for i in users[1:3]:
    print(i)

num = "123"

for i in range(0,len(users)):
    users[i] = users[i] + num
    
print(users)

ram = input("enter a number: ")
print(ram)

num = input("enter a num: ")
print(num)
print("type", type(num))

num1 = input("enter another num: ")
print(num1)
print("type", type(num1))

message = "ram is chutya"

message = [s + " " for s in message]
print(message)

print(' '.join(message))
