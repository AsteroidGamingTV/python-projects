
def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    print("Thou hast answered: {}".format(answer))
    return answer

def let_pass():
    print("Fine, off you go.")

def kill():
    print("Thou art cast into the Gorge.")
    
#######################################

name = ask("What is your name? ")
quest = ask("What is your quest? ")


if name == 'patato':
    color = ask("What is your favorite color? ")
    if color == 'blue':
        let_pass()
    else:
        kill()
