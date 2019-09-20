from os import system
import time
import random

N = int(input("Give the value of N: "))
if N < 3 or N > 10:
    print("N must fall between 3 and 10 (inclusive)!")
    exit()

random_numbers = []
for i in range(N):
    random_numbers.append(random.randint(-1000, 1000))

for i in range(len(random_numbers)):
    print(i, random_numbers[i])
    time.sleep(0.5)
    system('clear')

random_index = random.randint(0, N -1)
selected_number = random_numbers[random_index]
prompt_message = 'What was the index of this number? ' + str(selected_number) + '\nEnter the number: '
guessed_index = int(input(prompt_message))

if random_index == guessed_index:
    print('You won!')
else:
    print('You die!')
