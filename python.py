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

if 1<2:
     print("yes this is correct")
else:
     print( "worng message" )




usersa = ["ram", "shaym", "hari", "kukuar"]

k = input("enter a name ma ki ch: ")

usersa.append(k)
if k in usersa:
    print(k + " is present")
else:
    print(k + " is dead")    

    #dictionary

subodh = {
    "height": "5.6",
    "weight": "200",
    "age": "31",
    "job": "devops"
}

print("height of subodh is: " + subodh["height"])

manche = [
    {"name":"subodh1","job":"system","age":"31"},
    {"name":"pashu","job":"qa","age":"34"},
    {"name":"kari","job":"ba","age":"26"}
]

for i in manche:
    print("username is",i["name"],"and job is",i["job"],"age is",i["age"])

for u in range(0,len(manche)):
    manche[u]['password'] = '123456'
print(manche)

def sayHello():
    print("hello")

sayHello()    
    