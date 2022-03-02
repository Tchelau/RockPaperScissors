from random import choice
from time import sleep

cpu = ["ROCK", "PAPER", "SCISSORS"]
cpuhand = choice(cpu)

print('''Choose your move!
[ 1 ] ROCK!
[ 2 ] PAPER!
[ 3 ] SCISSORS! ''')
playerhand = int(input("Sua escolha: "))
print("\033[1;36m""JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO""\033[0;0m")

print("-="*12)

if playerhand == 1:
    print(f"YOU: ROCK!!!")
elif playerhand == 2:
    print("YOU: PAPER!!!")
else:
    print("YOU: SCISSORS!!!")

print("-="*12)

print(f"CPU: {cpuhand}!!!")

if playerhand == 1 and cpuhand == 'ROCK': #pedra vs pedra
    print("\033[1;34m""DRAW!""\033[0;0m")
elif playerhand == 1 and cpuhand == 'PAPER': #pedra vs papel
    print("\033[1;31m""YOU LOOSE!""\033[0;0m")
elif playerhand == 1 and cpuhand == 'SCISSORS': #pedra vs tesoura
    print("\033[0;32m""YOU WIN!""\033[0;0m")
elif playerhand == 2 and cpuhand == 'ROCK': #papel vs pedra
    print("\033[0;32m""YOU WIN!""\033[0;0m")
elif playerhand == 2 and cpuhand == 'PAPER': #papel vs papel
    print("\033[1;34m""DRAW!""\033[0;0m")
elif playerhand == 2 and cpuhand == 'SCISSORS': #papel vs tesoura
    print("\033[1;31m""YOU LOOSE!""\033[0;0m")
elif playerhand == 3 and cpuhand == 'ROCK': #tesoura vs pedra
    print("\033[1;31m""YOU LOOSE!""\033[0;0m")
elif playerhand == 3 and cpuhand == 'PAPER': #tesoura vs papel
    print("\033[0;32m""YOU WIN!""\033[0;0m")
elif playerhand == 3 and cpuhand == 'SCISSORS': #tesoura vs tesoura
    print("\033[1;34m""DRAW!""\033[0;0m")
