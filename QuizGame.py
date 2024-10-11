def newgame():
    guesses = []
    correct_guesses = 0
    questionNo = 1
    for key in questions:
        print("-------------------------------------")
        print(key)
        for i in options[questionNo - 1]:
            print(i)
        guess = input("Enter ('A','B','C','D')").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        questionNo += 1

    display_score(correct_guesses,guesses)
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT !")
        return  1
    else:
        print("WRONG !")
        return  0
def display_score(correct_guesses,guesses):
    print("------------------------------")
    print("RESULTS")
    print("------------------------------")
    print("Answers: ",end=" ")
    for  i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guessess", end="")
    for i in guesses:
        print(i,end="")
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print(f"Your score is : {score} %")

def play_again():
    response = input('Do you want to play again(yes/ no) :').lower()
    if response == "yes":
       return True
    else:
        return False





questions = {
    "Who created python? :":"A",
    "What year was  python Created ? :":"B",
    "Python is tributed to which comedy group? :":"C",
     "Is earth round ?:":"A"
}


options = [["A. Guido van rossum","B. Anil  kumar nayak","C. Ankita Modi","D. Elon musk"],
           ["A. 1989","B. 1991","C. 2000","D.2002"],
           ["A. Lonely Island","B. Smosh","C. Monty Python ","D. Ama gan comedy"],
           ["A. True","B. False","C. Sometimes","D.What's earth"]]

newgame()
while play_again():
    newgame()


print("BYEEEEE !")
