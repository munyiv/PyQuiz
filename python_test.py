x = [100,110,120]
z=[10,9]
x.extend(z)
print(x)
for b in z:
    m=[x*5 for b in z]
print(m)


def divisible_by_three():
    n=range(1,7)
    for a in n:
        if a % 3==0:
            print("Is divisible by 3")
        else:
            print("Is not divisible bt 3")
divisible_by_three()

def nested():
    x = [[1,2],[3,4],[5,6]]
    for b in x:
        print(b)
nested()

def duplicate():
    k= ['a','b','a','e','d','b','c','e','f','g','h']
    m=set(k)
    print(m)
duplicate()

def sorts():
    a=[9,8,7,6,5,4,3,2,1]
    a.sort()
sorts()

def divisible_by_7():
    x=range(100,200)
    for a in x:
        if a %7==0:
            print(a)
        else:
            print("Is not divisible by 7")
divisible_by_7()

def greet():
    students=[
        {"age":19,"name":"Eunice"},
        {"age":21,"name":"Agnes"},
        {"age":18,"name":"Audrey"},
        {"age":22,"name":"Lisa"},
      ]
    for student in students:
        if student.len ==4:
            return f"Hello" 
        else :
            return "you are not a student" 
greet()
 




