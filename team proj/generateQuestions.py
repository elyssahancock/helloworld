import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import math
import random

file = "maze-game-a1717-firebase-adminsdk-joa22-2638c2055a.json"
cred = credentials.Certificate(file)

firebase_admin.initialize_app(cred)

db = firestore.client()



def main():
    dict_list = []
    for _ in range(300):
        dict_list.append(generateQuestion())
    for dict in dict_list:
        db.collection("Questions").add(dict)


def generateQuestion():
    num1 = random.randint(0, 25)
    num2 = random.randint(0, 25)
    operation = random.choice(["+", "-", "*", "/"])
    
    match operation:
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
        case "*":
            answer = num1 * num2
        case "/":
            if num2 == 0:
                answer = "undefined"
            else:
                
                num1 = num1 * num2 * (random.randint(1, 5))
                answer = num1 / num2
                


    question = (f"{num1} {operation} {num2}")
    dict = {
        "Question": question,
        "Answer": answer
    }

    return dict
    
 
main()