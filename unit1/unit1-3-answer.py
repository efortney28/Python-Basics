'''
    Syntax, Comments, Variables, Data Types, & Numbers

    Read each comment prompt and try to follow along without looking at the answers.
'''

### First, create a variable named "name" and set it equal to a name
name =  "Eric"

### Now, let's print "Hi!, My name is {name}!" to the console where {name} is your variable.
print("Hi! My name is " + name + "!")


### Second, let's create another variable named color and set it equal to a color.
color = "red"

### Let's print "My favorite color is {color}." to the console!
print("My favorite color is " + color + ".")

### Third, let's create a variable named age and set it equal to a number
age = 27

### Let's print "I am {age} years old!" to the console... but in order to do that, we have to force "age" to become a string. This is called casting and we do it by typing str(age).
print("I am " + str('''What goes here???''') + " years old!")


### Home stretch! let's create two more variables: work, and favorite_thing. Set work equal to some company and favorite_thing equal to your favorite thing about that company.
work = "Google"
favorite_thing = "all of the amazing technology"

### Last thing! Let's print "My favorite thing about working at {work} is {favorite_thing}!". How can we insert two variables and get it to display correctly in the console?
print("My favorite thing about working at {0} is {1}!".format(work, favorite_thing))