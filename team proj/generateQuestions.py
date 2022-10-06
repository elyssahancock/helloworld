import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import math

file = "maze-game-a1717-firebase-adminsdk-joa22-2638c2055a.json"
cred = credentials.Certificate(file)

firebase_admin.initialize_app(cred)

db = firestore.client()


def main():
    None
def generateQuestions(num_of_questions):
    for _ in range(num_of_questions):
        num1 = math.random(0,9)
        
