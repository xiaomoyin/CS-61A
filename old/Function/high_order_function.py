from math import sqrt,pi
from operator import mul
def area(r,shap__constant):
    return r*r*shap__constant

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    assert r>0,'A length must be positive'
    return area(r,(3*sqrt(3))/2)













def identity(k):
    return k

def cube(k):
    return pow(k,3)

def exper(k):
    return  8/mul(4*k-3,4*k-1)

def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total


def one(n):
    return summation(n,identity)

def two(n):
    return summation(n,cube)

def three(n):
    return round(summation(n,exper),2)

print(three(1000))




def make_adder(n):
    
    def adder(k):
        return k+n
    

    return adder