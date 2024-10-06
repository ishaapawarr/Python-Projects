from numpy.ma.extras import average


def greetHello(name, ending):
    print("Hello " + name)
    print("Hello")
    print("Hello")
    print(ending)

def letterGenerator(name, date):
    st = f"Hi maam, This is {name} and I will not come to school on {date}"
    print(st)

def average(a, b):
    return (a+b)/2

print("Executing function")
greetHello("Isha", "Thank You")
greetHello("Rahul", "Thanks")
letterGenerator("Jyoti", "06th Oct")
letterGenerator("Ishita", "07th Oct")
print(average(34,25))
print("Done")