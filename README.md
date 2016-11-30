# TRIAL EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
 - You can use any resource online, but **please work individually**
 - Instead of copy-pasting your answers and solutions, write them in your own words.


# Tasks
## 1-5. Complete the tasks seen in the 1-5.py files! (~90 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm used in exercise 2. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:
flowchart:
https://drive.google.com/file/d/0B99ved1Ls044aUpRd25CX2puNFk/view?usp=sharing





### How can you get a random number in python? [2p]
#### Your answer:

You should import the random module. The easiest way is using the randint(a, b) function. It gives back random integer numbers in range between 'a' and 'b'.
Example:
import random

>>>print(random.randint(0, 10)
5

Or you can use the randrange(a, b, c) function. It gives back a number between 'a' and 'b'. The 'c' argument is the step. The function sees only the 'c'nth element in the 'a''b' range.
Example:

>>> print (random.randrange(5)) # a random element in range 0-5.
1
>>> print (random.randrange(1,5)) # a random element in range 1-5.
2
>>> print (random.randrange(1,10, 1)) # a random odd element in range 1-10.
7

### What does M stand for in MVC? [2p]
#### Your answer:

M means the Model in the MVC. The model manages all of the datas, the calculations, the rules, the logic of the application. The controller sends to and pull datas from it. It doesn't communicate with the view.
