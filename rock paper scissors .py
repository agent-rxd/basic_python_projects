import random
print("WELCOME TO ROCK PAPER SCISSORS")

usr=input("Enter Rock(R) , Paper(P), Scissors(S) : ")
usr_choice=usr.lower()
comp_choice=random.randint(1,3)
if usr_choice=="r":
    print("You chose rock")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif usr_choice=="p":
    print("You chose paper")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print("You chose scissors")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if comp_choice==1:
    print("Computer chose ROCK")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif comp_choice==2:
    print("Computer chose PAPER")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print("Computer chose SCISSORS")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if (usr_choice=="r") and (comp_choice==1):
    print("You Both Chose Rock")
    print("It is a DRAW ! ")
if (usr_choice=="r") and(comp_choice==2):
    print("YOU WIN ")
if(usr_choice=="r")and(comp_choice==3):
    print("YOU WIN ")
if(usr_choice=="p"):
    if comp_choice==1:
        print("YOU WIN ")
    if comp_choice==2:
        print("IT IS A DRAW")
    else:
        print("Oops ! COMPUTER WON ")
if usr_choice=="s":
    if comp_choice==1:
        print("Ooops ! COMPUTER WON ")
    if comp_choice==2:
        print("YOU WON ")
    else:
        print("IT IS A DRAW")
