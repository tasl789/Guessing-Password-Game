import random

easy_words = ["sad", "happy", "dirty", "good", "small", "clean", "hello"]
medium_words = ["honest", "success", "prepare", "difficult", "python", "laptop", "respect"]
hard_words = ["consistency", "preparation", "sustainability", "transformation", "optimization", "celebration", "collabration", "implementation"]

print("welcome, To Password Guessing Game")
print("Choose difficulty level : easy, medium, hard")

level = input("Enter level of game : ").lower().strip()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else :
    print("Invalid level. Defaultly going  with easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\n Guess the password")

while True :
    guess = input("Enter your guess : ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations, you will guess in {attempts} attempte.")
        break
    
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else :
            hint += "_"
    print(f"Hint : {hint}")
print("Game Over")
