#!/usr/bin/python3
manche = [
    {"name":"subodh","job":"system","age":"34","password":"nepal123","priv":"admin"},
    {"name":"pashu","job":"qa","age":"34","password":"pashu123","priv":"admin"},
    {"name":"ajay","job":"ba","age":"26","password":"ajay123","priv":"admin"}
]
ram = { 
    "name":"her",
    "age":"keti"

}

for key,value in ram.items():
    print(key,value)

def auth(priv,name1,job1,pass1):
    for u in manche:
        if u['name'] == name1 and u['job'] == job1 and u['password'] == pass1:
            return True
    return False

k = input("enter a name: ")
c = input("enter a job: ")
d = input("enter a password: ")

print(k)
print(c)

if auth('admin',k,c,d):
    print("welcome to the page my lord, you are the king of the universe")
else:
    print("fuck off mother fucker, go back to your country")

if auth('admin',name1 = k,job1 = c,pass1 = d):
    print("welcome to the page my lord, you are the king of the universe")
else:
    print("fuck off mother fucker, go back to your country")

def multiply(*num):
    if len(num) == 0:
            return 0
    result = 1
    for n in num:
        result *= n
    return result

print(multiply(2,4,5,6,7))

users = [
    {"name":"subodh","job":"system","age":"34","password":"nepal123","priv":"admin"},
    {"name":"pashu","job":"qa","age":"34","password":"pashu123","priv":"admin"},
    {"name":"ajay","job":"ba","age":"26","password":"ajay123","priv":"admin"}
]

def createuser(name,password,**meta):
    users = {}
    users["name"] = name
    users["password"] = password
    for k,v in meta.items():
        users[k] = v
    return users

a = input("enter a key")
b = input("enter a value")
users = createuser("subodh","nepal123",a = b)
print(users)
