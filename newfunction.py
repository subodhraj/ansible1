#!/usr/bin/python3
manche = [
    {"name":"subodh","job":"system","age":"34"},
    {"name":"pashu","job":"qa","age":"34"},
    {"name":"ajay","job":"ba","age":"26"}
]

def auth(name1,job1):
    for u in manche:
        if u['name'] == name1 and u['job'] == job1:
            return True
    return False

k = input("enter a name: ")
c = input("enter a job: ")
print(k)
print(c)

if auth(k,c):
    print("welcome to the page my lord, you are the king of the universe")
else:
    print("fuck off mother fucker, go back to your country")
