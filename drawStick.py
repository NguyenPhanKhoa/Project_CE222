import turtle

# Create a turtle object
t = turtle.Turtle()

class var:
    def __init__(self, xPos, yPos, p_s_left = True, n_s_left = True):
        self.name = ""
        self.xPos = xPos
        self.yPos = yPos
        self.p_s_left = True
        self.n_s_left = True
        self.SPos_Ndiff = self.point(0, 0)
        self.DPos_Ndiff = self.point(0, 0)
        self.SPos_Pdiff = self.point(0, 0)
        self.DPos_Pdiff = self.point(0, 0)

    class point:
        def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y

def metal1(a, b, x):
    t.pencolor("blue")
    t.penup()
    t.goto(a, b)
    t.pendown()
    t.forward(200 * x)
    t.penup()

def ndiff(a, b, x):
    t.pencolor("green")
    t.penup()
    t.goto(a, b)
    t.pendown()
    t.forward(200 * x)
    t.penup()

def pdiff(a, b, x):
    t.pencolor("gold")
    t.penup()
    t.goto(a, b)
    t.pendown()
    t.forward(200 * x)
    t.penup()

def poly(a, b, c):
    t.pencolor("red")
    t.penup()
    t.goto(a, b)
    t.write(c, font=("Arial", 10, "normal"))
    t.pendown()
    t.right(90)
    t.forward(70)
    t.left(90)
    t.penup()

def StickDefault(x):
    metal1(-150, 0, x)
    t.write("Gnd", font=("Arial", 10, "normal"))
    ndiff(-150, 25, x)
    t.write("ndiff", font=("Arial", 10, "normal"))
    pdiff(-150, 75, x)
    t.write("pdiff", font=("Arial", 10, "normal"))
    metal1(-150, 100, x)
    t.write("Vdd", font=("Arial", 10, "normal"))
    t.hideturtle()

def StickPoly(x, exp, a, b):
    v = []  # Define an empty list to store the variables
    c = list(a.union(b))  # Combine the two sets
    i = 0
    if exp == 'None':
        x = 2
        c.append('X')
        for i in range(2):
            v.append(var(-75 + 50*i , 85))
            v[i].name = c[i]
            poly(v[i].xPos, v[i].yPos, v[i].name)
    else:
        for i in range(x):
            v.append(var(-75 + 50*i , 85))
            v[i].name = c[i]
            poly(v[i].xPos, v[i].yPos, v[i].name)
    Parallel(exp, v)
    i = 0
    for i in range(x):
        StickPolyNdiff(v[i])
        StickPolyPdiff(v[i])
    if exp == 'None':
        drawNone(v[0], v[1])
    elif exp == 'NOT':
        drawNot(v[0])
    elif exp == 'NAND':
        drawNand(v[0], v[1])
    elif exp == 'NOR':
        drawNor(v[0], v[1])
    return v
    
def StickPolyPdiff(var):
    t.penup()
    var.SPos_Pdiff = var.point(var.xPos - 10, var.yPos - 10)
    t.goto(var.SPos_Pdiff.x, var.SPos_Pdiff.y)
    var.DPos_Pdiff = var.point(var.xPos + 10, var.yPos - 10)
    t.goto(var.DPos_Pdiff.x , var.DPos_Pdiff.y)
    if var.p_s_left == True:
        t.goto(var.SPos_Pdiff.x, var.SPos_Pdiff.y)
        t.write("S", align="center", font=("Arial", 7, "normal"))
        t.goto(var.DPos_Pdiff.x , var.DPos_Pdiff.y)
        t.write("D", align="center", font=("Arial", 7, "normal"))
    elif var.p_s_left == False:
        t.goto(var.DPos_Pdiff.x , var.DPos_Pdiff.y)
        t.write("S", align="center", font=("Arial", 7, "normal"))
        t.goto(var.SPos_Pdiff.x, var.SPos_Pdiff.y)
        t.write("D", align="center", font=("Arial", 7, "normal"))

def StickPolyNdiff(var):     
    t.penup()
    var.SPos_Ndiff = var.point(var.xPos - 10, var.yPos - 60)
    t.goto(var.SPos_Ndiff.x, var.SPos_Ndiff.y)
    var.DPos_Ndiff = var.point(var.xPos + 10, var.yPos - 60)
    t.goto(var.DPos_Ndiff.x , var.DPos_Ndiff.y)
    if var.n_s_left == False:
        t.goto(var.SPos_Ndiff.x, var.SPos_Ndiff.y)
        t.write("S", align="center", font=("Arial", 7, "normal"))
        t.goto(var.DPos_Ndiff.x , var.DPos_Ndiff.y)
        t.write("D", align="center", font=("Arial", 7, "normal"))
    elif var.n_s_left == True:
        t.goto(var.DPos_Ndiff.x, var.DPos_Ndiff.y)
        t.write("S", align="center", font=("Arial", 7, "normal"))
        t.goto(var.SPos_Ndiff.x, var.SPos_Ndiff.y)
        t.write("D", align="center", font=("Arial", 7, "normal"))

def Parallel(exp, var):
    if exp == 'None':
        var[0].p_s_left = True
        var[0].n_s_left = False
        var[1].p_s_left = True
        var[1].n_s_left = False
    if exp == 'NOT':
        var[0].p_s_left = True
        var[0].n_s_left = False
    elif exp == 'NOR':
        var[0].p_s_left = True
        var[1].p_s_left = True
        var[0].n_s_left = False
        var[1].n_s_left = True
    elif exp == 'NAND':
        var[0].p_s_left = True
        var[1].p_s_left = False
        var[0].n_s_left = False
        var[1].n_s_left = False

def drawNot(v0):
    t.penup()
    t.pencolor("blue")
    t.goto(v0.SPos_Pdiff.x, v0.SPos_Pdiff.y)
    t.pendown()
    t.dot(5, "black")
    t.left(90)
    t.forward(25)
    t.right(90)
    t.penup()
    t.goto(v0.SPos_Ndiff.x, v0.SPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.right(90)
    t.forward(25)
    t.penup()
    t.goto(v0.DPos_Ndiff.x, v0.DPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.goto(v0.DPos_Pdiff.x, v0.DPos_Pdiff.y)
    t.left(90)
    t.dot(5, "black")
    notEndPoint = var.point(v0.DPos_Pdiff.x, (v0.DPos_Ndiff.y + v0.DPos_Pdiff.y) / 2)
    t.goto(v0.DPos_Pdiff.x, (v0.DPos_Ndiff.y + v0.DPos_Pdiff.y) / 2)
    t.forward(30)
    t.write('Y')
    return notEndPoint

def drawNand(v0, v1):
    t.penup()
    t.pencolor("blue")
    t.goto(v0.SPos_Pdiff.x, v0.SPos_Pdiff.y)
    t.pendown()
    t.dot(5, "black")
    t.left(90)
    t.forward(25)
    t.right(90)
    t.penup()
    t.goto(v1.DPos_Pdiff.x, v1.DPos_Pdiff.y)
    t.pendown()
    t.dot(5, "black")
    t.left(90)
    t.forward(25)
    t.penup()
    t.goto(v0.SPos_Ndiff.x, v0.SPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.backward(25)
    t.penup()
    t.goto(v0.DPos_Pdiff.x - v1.DPos_Pdiff.x, v0.DPos_Pdiff.y)
    t.pendown()
    t.dot(5, "black")
    t.right(180)
    t.forward(25)
    t.left(90)
    t.forward(100)
    t.write('Y')
    t.penup()
    t.goto(v1.DPos_Ndiff.x, v1.DPos_Ndiff.y)
    t.left(90)
    t.pendown()
    t.dot(5, "black")
    t.forward(25)


def drawNor(v0, v1):
    t.penup()
    t.pencolor("blue")
    t.goto(v0.SPos_Ndiff.x, v0.SPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.left(90)
    t.backward(25)
    t.right(90)
    t.penup()
    t.goto(v1.DPos_Ndiff.x, v1.DPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.left(90)
    t.backward(25)
    t.penup()
    t.goto(v0.SPos_Pdiff.x, v0.SPos_Pdiff.y)
    t.pendown()
    t.dot(5, "black")
    t.forward(25)
    t.penup()
    t.goto((v0.DPos_Ndiff.x - v1.DPos_Ndiff.x), v0.DPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.right(180)
    t.backward(25)
    t.left(90)
    t.forward(100)
    t.write('Y')
    t.penup()
    t.goto(v1.DPos_Pdiff.x, v1.DPos_Pdiff.y)
    t.left(90)
    t.pendown()
    t.dot(5, "black")
    t.backward(25)

def drawNone(v0, v1):
    t.penup()
    t.pencolor("blue")
    t.goto(v0.SPos_Ndiff.x, v0.SPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.left(90)
    t.backward(25)
    t.right(90)
    t.penup()
    t.goto(v0.SPos_Pdiff.x, v0.SPos_Pdiff.y)
    t.pendown()
    t.dot(5, "black")
    t.left(90)
    t.forward(25)
    t.penup()
    t.goto(v1.SPos_Ndiff.x, v1.SPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.backward(25)
    t.penup()
    t.goto(v1.SPos_Pdiff.x, v1.SPos_Pdiff.y)
    t.pendown()
    t.dot(5, "black")
    t.forward(25)
    t.penup()
    t.goto(v0.DPos_Ndiff.x, v0.DPos_Ndiff.y)
    t.pendown()
    t.dot(5, "black")
    t.right(180)
    t.backward(50)
    t.dot(5, "black")
    t.forward(25)
    t.left(90)
    t.forward(40)
    t.penup()
    t.goto(v1.DPos_Pdiff.x, v1.DPos_Pdiff.y)
    t.left(90)
    t.pendown()
    t.dot(5, "black")
    t.backward(50)
    t.dot(5, "black")
    t.forward(25)
    t.right(90)
    t.forward(40)
    t.write('Y')

def main():
    StickDefault(1)
    # drawNone()
    x = {'~A'}
    y = set()
    v = StickPoly(1, 'NOT', x, y)
    turtle.done()

if __name__ == "__main__":
    main()