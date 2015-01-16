"""
Given a boss-employee relationship with each person's age
print out the relationship, starting with boss

employee name,boss name,age

A,B,32
K,A,34
B,,37
T,B,40
D,A,41
P,B,29

"""
def func1(people):
    rel_pool = {}
    age_pool = {}
    boss = None
    for person in people:
        if person[1] == '':
            boss = person[0]
        if rel_pool.has_key(person[1]):
            rel_pool[person[1]].append(person[0])
        else:
            if person[1] != '':
                rel_pool[person[1]] = [person[0]]
        age_pool[person[0]] = person[2]

    space = 0
    temp = [(boss, space)]
    while len(temp) > 0:
        curr_name, curr_space = temp.pop()
        print ' ' * curr_space + curr_name, age_pool[curr_name]
        curr_space = curr_space + 1
        if rel_pool.has_key(curr_name):
            for _ in rel_pool[curr_name]:
                temp.append((_, curr_space))
    return


import sys
temp = sys.argv[1].split(';')
people = []
for person in temp:
    people.append([_ for _ in person.split(',')])
print func1(people)

#python interview1.py 'A,B,32;K,A,34;B,,37;T,B,40;D,A,41;P,B,29'
