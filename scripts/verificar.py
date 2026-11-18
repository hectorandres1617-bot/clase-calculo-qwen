import math
def simpson(f,a,b,n=200000):
    h=(b-a)/n; s=f(a)+f(b)
    for i in range(1,n): s+=f(a+i*h)*(4 if i%2 else 2)
    return s*h/3
print("1) area bajo 3x^2+1 en [0,2]  :", round(simpson(lambda x:3*x*x+1,0,2),4), "(esperado 10)")
print("2) area entre y=x e y=x^2     :", round(simpson(lambda x:x-x*x,0,1),4), "(esperado 1/6=0.1667)")
print("3) volumen discos y=sqrt(x)   :", round(simpson(lambda x:math.pi*x,0,4),4), "(esperado 8*pi=25.1327)")
print("3b) arandela y=x e y=x^2, giro eje x:", round(simpson(lambda x:math.pi*(x*x-x**4),0,1),5), "(esperado 2*pi/15=0.41888)")
print("4) x*ln(x) en [0,1]           :", round(simpson(lambda x:x*math.log(x) if x != 0 else 0,0,1),4), "(esperado -0.25)")
print("5) 1/x^2 de 1 a 1e6           :", round(simpson(lambda x:1/x**2,1,1e6,2000000),3), "(tiende a 1)")
print("   cono r=2,h=4 (NO coincide) :", round(math.pi*4*4/3,4), "= 16*pi/3: el solido es un paraboloide")
