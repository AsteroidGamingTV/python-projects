
def ask(question):
    print(question)
    answer = input('> ').strip()
    return answer

###################################################

print('''
Welcome to the age difference patato!
''')

name1 = ask("What is your name? ").title()
name2 = ask("What is your friends name? ").title()
age1 = int(ask("How old are you? "))
age2 = int(ask("How old is your friend? "))

years_apart = abs(age1 - age2)

print(years_apart)
