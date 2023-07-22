"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements 
that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruitis in your list. 
If the fruit is in your list, the if block should print a statement, such as You really like bananas!
"""
fruits = ['watermelon','mango','jackfruit','sapota','strawberry','rasberry','gooseberry','banana','pomegrenate']
if 'mango' in fruits:
    print ("Adding mango to the mixture.")
if 'strawberry' in fruits:
    print("Adding strawberry to the mixture..")
if 'watermelon' in fruits:
    print("Adding watermelon to the mixture...")
if 'apple' in fruits:
    print("Adding apple in the mixture....")
if 'grapes' in fruits:
    print("Adding grapes in the mixtures.....")

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
"""
alien_colour = 'red'
if alien_colour == 'green':
    points = 5
if alien_colour == 'yellow':
    points = 10
if alien_colour == 'red':
    points = 20
print(f"You have earned {points} points")

"""
5-5 Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
"""
alien_colour = 'green'
if alien_colour == 'green':
     print("You have earned 5 points")
elif alien_colour == 'yellow':
     print("You have earned 10 points") 
else:
     print("You have earned 15 points")

alien_colour = 'yellow'
if alien_colour == 'green':
     print("You have earned 5 points")
elif alien_colour == 'yellow': 
     print("You have earned 10 points") 
else:
     print("You have earned 15 points")

alien_colour = 'red'
if alien_colour == 'green':
     print("You have earned 5 points")
elif alien_colour == 'yellow':
     print("You have earned 10 points") 
else:
     print("You have earned 15 points")


"""
5-6 Stages of Life: Write an if-elif-else chain that determines a person’s stage
of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that the
person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""
age = 14
if age < 2:
     stage = 'baby'
elif age < 4:
     stage = 'toddler'
elif age < 13:
     stage = 'kid'
elif age < 20: 
     stage = 'teenager'
elif age < 65: 
     stage = 'adult'
elif age >= 65:
     stage = 'elder' 
print(f"You are a {stage}")