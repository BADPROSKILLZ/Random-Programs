"""
This program acts as a caesar cypher.
"""
import random

class CaesarCypher:
    shift = 0
    message = ""
    shiftedMessage = ""
    global alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, shft: int = random.randint(1, 25), msg: str = "PLACEHOLDER MESSAGE"):
        self.shift = shft
        self.message = msg
        self.updateCypher()

    def updateShift(self, shft):
        self.shift = shft
        self.updateCypher()

    def updateMessage(self, msg):
        self.message = msg
        self.updateCypher()
        
    def updateCypher(self):
        for char in self.message:
            if char not in alphabet and char not in alphabet.upper():
                self.shiftedMessage += char
            elif char.isupper():
                self.shiftedMessage += alphabet.upper()[(alphabet.upper().index(char) + self.shift) % 26]
            else:
                self.shiftedMessage += alphabet[(alphabet.index(char) + self.shift) % 26]

    def __str__(self):
        return self.shiftedMessage

cypher = CaesarCypher(6, "HeLlO & wOrLd")
print(cypher)
