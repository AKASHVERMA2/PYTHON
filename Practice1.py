# Problem-1.Write a program to print Twinkle twinkle little star poem in python.
print('''
Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark.
Though I know not what you are,
Twinkle, twinkle, little star.

Twinkle, twinkle, little star,
How I wonder what you are.''')

# Problem-2.Write the table of 5 in python

# Define the number for which we want to print the table
num = 5

# Define the range for the table (e.g., 1 to 10)
for i in range(1, 11):
    # Calculate the product and print the table
    product = num * i
    print(f"{num} x {i} = {product}")


# Problem-3.Install an external module and use it to perform an operation of your interest.

# we install the module pyttsx3 with the help of pip in terminal and import pyttsx3 in python code

import pyttsx3
engine = pyttsx3.init()
engine.say("hi my name akash")
engine.runAndWait()


# Problem-4.Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. write with comment.

''' Problem No.-4 is not solve'''