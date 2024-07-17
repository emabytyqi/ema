def shuma(x,y):
    print (f"shuma eshte:{x+y}")
shuma(5,10)

def katror(x):
    rezultati = x**2
    return rezultati
y = katror(5) + 5
print(y)

def funksioni():
    x=5
    print(x)
funksioni()

def funksionii():
    x = "I love jCoders"
    print(x)
x = "Me too!"
funksionii()
print(x)

def ffunksioni():
    global x 
    x = 10
x = "Python"
print(x)
ffunksioni
print(x)

def calculate(x,y,o):
    if o == "+":
        print(x+y)
    elif o == "*":
        print(x*y)
    else:
        print("sheno nje operator valid")
calculate(3,5,"+")

lista = [1,2,3,4,5,6,7]
vleraMin=()
vleraMax=()
vleraMes=()