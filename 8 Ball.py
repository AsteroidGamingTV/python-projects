import random

print("Behold, I am the magic 8 ball.")

answers = ['Yes.','No.','Maybe.']


def ask():
    print("Type your question below.")
    question = input('> ').strip().lower()
    answer = random.choice(answers)
    print(answer)
    print()

while True: ask()
