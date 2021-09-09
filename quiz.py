print("Welcome to my quiz!")

playing = input("Do you want to play? ")

# if player does not say yes, quit the game
if playing.lower() != "yes":
    quit()

print("Okay! Game will start")
score = 0

questions = ["What does CPU stand for? ", "What does GPU stand for? ", "What does RAM stand for? "]
answers = ["central processing unit", "graphics processing unit", "random access memory"]

for e, question in enumerate(questions):
    answer = input(question).lower()

    if question[e] and answer == answers[e]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")



print(f"You got {score} questions correct!")
