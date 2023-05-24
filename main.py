from addition import add
from multiplication import multiply
from subtraction import subtract
from exponent import power
from average import avg
from factorial import factorial_function


if __name__=="__main__":
    A=6
    B=4

    print(add(A,B))
    print(multiply(A,B))
    print(subtract(A,B))
    print(power(A,B))
    print(avg(A,B))
    print(f'{A}! is {factorial_function(A)}')
    print(f'{B}! is {factorial_function(B)}')
    