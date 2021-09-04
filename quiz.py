print("Welcome to my quiz!")

playing = input("Do you want to play? ")

# if player does not say yes, quit the game
if playing.lower() != "yes":
    quit()

print("Okay! Game will start")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print(f"You got {score} questions correct!")
