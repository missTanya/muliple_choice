
from Questions import Questions
import sys


class main():
    """
    THIS IS A MULTIPLE CHOICE ANSWER GAME.
    It will ask for the user's name and number of tries for the Mutiple Choice game.
    """
    print("This is a Multiple Choice Questions\n".upper())

    questions_prompt  = [
        "What is the color of the sky?\n(a) Blue\n(b) Green\n(c) Pink",
        "What is the color of Banana?\n(a) Violet\n(b) Yellow\n(c) Black",
        "What is the color of Strawberry?\n(a) Orange\n(b) Grey\n(c) Red"
    ]

    def run_MC_test(questions):
        score = 0
        for q in questions:
            print(q.prompt + "\n")
            answer = input("Answer: ")
            print("")
            if answer == q.answer:
                score += 1
        print("You got {}/{} correct!".format(str(score), str(len(questions))))

    list_of_answers = [
        Questions(questions_prompt[0], "a"),
        Questions(questions_prompt[1], "b"),
        Questions(questions_prompt[2], "c")
    ]

    name = input("Hi, Please type in your name: ")
    print("Hi {}, Welcome to your first Multiple Choice Game!".format(name.title()))
    start = input("\nAre you ready to play? [Y/N] ")
    if start.lower() == 'y':
        tries = int(input("How many tries do you want? "))
        while (tries>0):
            run_MC_test(list_of_answers)
            tries -= 1

        else:
            print("Thank you for playing!")
            sys.exit(1)
    else:
        print("Thank you, please play again!")
        sys.exit(1)


if __name__ == "__main__":
    main()