#!/usr/bin/python3
manche = [
    {"name":"subodh","job":"system","age":"34","password":"nepal123"},
    {"name":"pashu","job":"qa","age":"34","password":"pashu123"},
    {"name":"ajay","job":"ba","age":"26","password":"ajay123"}
]

def auth(name1,job1,pass1):
    for u in manche:
        if u['name'] == name1 and u['job'] == job1 and u['pass'] == pass1:
            return True
    return False

k = input("enter a name: ")
c = input("enter a job: ")
d = input("enter a password: ")

print(k)
print(c)

if auth(k,c,d):
    print("welcome to the page my lord, you are the king of the universe")
else:
    print("fuck off mother fucker, go back to your country")
