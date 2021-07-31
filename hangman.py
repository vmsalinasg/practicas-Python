from random import randint

with open("words.txt") as file:
    words = file.read()
    words = words.split()

player_score = 0

guess_number = randint(0,len(words)-1)

print(f"La palabra que debes adivinar \ncontiene {len(words[guess_number])} letras.\n")
print("_ "*len(words[guess_number]))

guessing = ["_" for x in words[guess_number]]

score = 10

print(f"Tienes {score} intentos")

while "".join(guessing) != words[guess_number].lower():
    if score >= 1:
        letter = str(input("\nElige la primera letra: ")).lower()
        indices = [pos for pos, char in enumerate(words[guess_number].lower()) if char == letter.lower()]
        for x in indices:
            guessing[x] = letter.lower()
        print(" ".join(guessing))
    else:
        print("Lo siento, perdiste.")
        break
    score -= 1

print('\n¡Felicidades, tú ganaste!')
