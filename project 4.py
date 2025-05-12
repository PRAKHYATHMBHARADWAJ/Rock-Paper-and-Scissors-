import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper , scissors]
user_choice=int(input("what do you chose?0 for rock, 1 for paper and 2 for scissors\n"))
if user_choice>= 0 and user_choice <= 2:
    print(game_images[user_choice])
computers_choice=random.randint(0,2)
print("computers_choice:")
print(game_images[computers_choice])
if user_choice >= 3 or user_choice < 0 :
    print("you typed a invalid number. you lose!")
elif user_choice == 0 and computers_choice == 2:
    print("you win!!")
elif computers_choice==0 and user_choice==2:
    print("you lose!!")
elif computers_choice > user_choice:
    print("computer wins")
elif user_choice > computers_choice:
    print("you win!!")
elif computers_choice==user_choice:
    print("its a draw!")
