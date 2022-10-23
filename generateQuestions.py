import math
import random
def main():
    generateQuestion()
def generateQuestion():
    num1 = math.random(0, 100)
    num2 = math.random(0, 10)
    operation = math.random("+", "-", "*", "/")
    question = (f"{num1} {operation} {num2}")
    match operation:
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
        case "*":
            answer = num1 * num2
        case "/":
            answer = num1 * num2(math.random(1, 3)) / num2
            num1 = num1 * num2(math.random(1, 3))


    question = (f"{num1} {operation} {num2}")
    

    

 
    