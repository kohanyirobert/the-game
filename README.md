# "The Game"

## Functional requirements

1. The user specifies a number that will mean how many numbers will be in our list.
    * Need to store this somewhere: `N` global variable. *Note*: ever assign new value to this, treat this like if it were constant.
    * Need to use `input` and `int` functions.
1. The minimum value for `N` is 3, the max is 10.
    * Need to use `if` (maybe with and `else` branch or `exit`), comparison operators like `<=` or `>` and `print`.
1. The list of numbers need to be filled with random numbers.
    * Need to store these somewhere as well: `random_numbers` global variable.
1. Generate a random number `N` times.
    * Need to use `for` (maybe `while`), use the `random` module with `import` and need to find a function which generates a random integer.
1. Append each generated random number to the list.
    * *Note*: we start out with an empty list.
    * Need to use `append` function of the list.
1. Show the numbers generated and stored in the list to the user one by one.
    * Need to use a `for` again to iterate over the list and print each random number to the console.
    * Must understand what is a "loop variable" and how does it behaves, how its value changes in each repetition of the loop.
1. Clear the screen after each number shown.
    * Must use the `os` module and the `system` function: e.g. `system('clear')` or `system('cls')`.
1. Each number is shown to the user only for half a second.
    * Must use the `time` module and it's `sleep` function (e.g. `sleep(0.5)`). 
1. After each number was shown the game picks a random number from the list and shows that to the user.
    * Must pick a random number (from 0 to `N` - 1) using the random module.
    * Save this to a variable and use it as an index later.
    * Use this index value to print the element at that index.
1. The user must remember at which index this last number was located at in the list.
    * Again, must use `input` and `int` to gather input from the user.
    * The user must give a numeric input.
1. The game decides if the user's input was a match or not.
1. If it's a match the user wins, otherwise the user dies.

## Non-functional requirements

1. The program must not crash when given illegal input.
1. The program must stay consistent at all times.
