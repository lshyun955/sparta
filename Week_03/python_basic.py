import requests
num = 10
num2 = num + 5

print(num + num2)


aList = []
aList.append(1)
aList.append('1')
aList.append([1,2])

print(aList);

aDict = {}
aDict = {'name':'John', 'age':26}
aDict['height'] = 178

print(aDict)

def add(a,b):
    return a + b

sum = add(5, 4)
print(sum)


def oddEven(a):
    if a % 2 ==0:
        return True
    else:
        return False

result = oddEven(12381)
print(result)

fruits = ['사과','배','감','귤']
for fruit in fruits:
    print(fruit)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for fruit in fruits:
    if fruit == '배':
        count += 1
print(count)

def count_fruit(name):
    count = 0
    for fruit in fruits:
        if fruit == name:
            count += 1
    return count

print(count_fruit('사과'))

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for person in people:
    print(person['name'],person['age'])

def get_age(name):
    for person in people:
        if person['name'] == name:
            return person['age']

    return None
            

print(get_age('carry'))