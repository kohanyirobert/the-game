# "The Game"

## Functional requirements:
1. the user specifies a number that will mean how many numbers will be in our list
    N variable (global variable, never assign new value to this), input, int
1a. the minimum is 3 the max is 10
    if (maybe with else), <=, >, print, exit
2. the list fill be filled with random numbers
2a. generate a random number N times
    for (maybe while), using the random module (import, find which function generates a random int)
2b. append the random number to the list
    list, empty list, append
    save the list in a variable
3. the numbers are shown to the user one by one
    for (maybe) -> iterate over the list, print, must know what is the "loop variable"
3a. the screen is cleared each time
    os (module, import), use system('clear'), system('cls')
3b. the number is shown for half a second
    time (module, import), use sleep(3)
4. after each number was shown the game picks a random number, shows it to the user
    pick a random number -> generate a random number from 0 to (N-1)
    save it to a variable -> use it as an index
    using the index print the element (at the index)
4a. the user must remember at which index the number was located in the list
    input, int
    the user gives an input (numeric)
4c. the game decides if it's a match or not
    validate bad input
4d. if it's a match -> the user WON otherwise the user dies
    if VALID:
        print('WON')
    else:
        print('YOU DIED')

Non-functional requirements:
1. if the user gives bad input the program must not crash
2. the program must stay consistent at all times
