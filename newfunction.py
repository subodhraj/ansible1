#!/usr/bin/python3
manche = [
    {"name":"subodh1","job":"system","age":"31"},
    {"name":"pashu","job":"qa","age":"34"},
    {"name":"kari","job":"ba","age":"26"}
]

def auth(name1,job1):
    for u in manche:
        if u['name'] == name1 and u['job'] == job1:
           return True
    return False
