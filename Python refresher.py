
# python as fast as possible

# Data types
# Integer, ex: 56783, -857463, as long as it does not have a decimel point on it
# Float(anything that has a decimal on it), 2727.0, -9.7
# anything surrounded by single or double quotation marks 'hello' and "hello" are equivalent, 'hello"' is embedded
# Bool, where we have True(1) or we have False(0)


# print ('Hello World!'), has to be wrapped in a string, you can just print a float though that is not a string, like print(4.5), can do print ('4.5', 'end', 87, False)
# add end= '\n' if you want the print to go to the next line of code, if you do end=' | ', then it will say Hello end 87 False\Hello
# hello = 'tim' means that this is a variable, then if you do world = 'world' and world = hello, then it will print tim tim
# if with the line above, you then add hello = 'no', then it will print no tim, since you change what the variable meant with the new string
# in a variable, you cannot have any special characters or start with a number.... if you want seperate words, say hello_world (this is snake case, helloWorld is camel case)
# cannot do 9hello, but can do Hello_world32
# you want to assign a input to a variable, so Name = input('Name: '), and then age = input('Age: ')
# print('Hello', name, 'you are', age, 'years old')
# x = 9| y = 3| result = x + y| print(result), and you can make either of these numbers a decimal
# if you use the division sign (\) in a math equation, it will give the calculated value as a float| if you want to make suer that it is an integer, then just say result = int(x / y)_
# doing result = x**y shows as an exponent, result = x // y gives a integer result, so there are no decimal points
# if you do a %, then this is will give you the remainder 10/3, 3 remainder 1
# python follows order of operations, so Brackets, Exponenets, division, multiplication, addition, and subtraction
# if you do num = input('Number: ') -> gives us a string | print(num - 5), this will not work as num is a string although it looks like an int
# so instead we need to do num = input('Number: ') -> gives us a string | print(int(num) - 5), can do float(num) if we want to get a float result instead
# hello = 'hello'| print(type(hello)), this is a <class 'str'>, so it's an instance of a class string


# METHOD, so its a decimal followed by what we need, so .upper(), can also use .lower(), .capitalize() like a sentence, .count will check how many of something is in a string
# so if we do hello = 'hello'.upper(), it makes this entire string upper case.....can also just do hello = 'hello'|print(hello.upper())
# hello = 'heLL0 World'| print(hello.lower().count('ll'))
# x = 'hello' | y = 3, can then do print(x * y) and it will print hellohellohello
# print(x + y) gives us helloyes
# so == checks for equality of the left hand side and the right hand side, and != checks for inequality, and we have <=, >=, <, >
# x = 'hello', y = 'hello', so print(x == y), and this will yield the value of true
# x = "hello"
# y = 'helLo'
# this will show up as not equal because of the difference in capitalization
# print('a' > 'Z'), this will yield true as its greater than in the in the AscII code
# print(ord('Z')), you'll get 90.....print(ord('a')), then you'll get 97....if you do print('a' > 'b'), this is False because b = 98
# if you do print ('ab' > 'b') it will compare teh characters from left to right, so it would say true, but if you do print ('ab' > 'ad'), then this would say false
# print(7.0 == 7), this would say true


# Chained Condidtionals -> combined multiple conditions together to get one bigger condition
# x = 7| y = 8| z = 0|   result1 = x == y| result2 = y > x| results3 = z < x + 2
# I can use the keywords of and, or, not
# result4 = result1 or not result2 or result3 | print(result4)
# print (not False), will print True
# print(not (False and True)), this is saying is the False and True true
# in order of operations, not is first, and is second, and or is last


## If/Else/Elsif


# x = input('Name: ')

# if x == 'Tim':
#      print('You are great!')

# print('Always do this')......this will work
# if you enter another name, then it will just output Always do this

# x = input('Name: ')

# if x == 'Tim':
#       print('You are great!')
# else:
#       print('No')

# an elif statement must come after an if, and before an else...can have as many elif's as possible, but only one if and else

# if x == 'Tim':
#       print ('You are great')
# elif x == 'Joe':
#       print ('Bye Joe')
# elif x == 'Sarah':
#       print ('Random')


# A collection is an unordered or ordered group of elements

## LISTS AND TUPLES

# Lists are square brackets, tuples are round brackets
# x = [4, True, 'hi']
# y = 'hi'
# print(len(x)), len will let me know the length of the list, which in this case is 3
# print(len(x), len(y)) will give you 3 2

# x = [4, True, 'hi']
# x.append('hello') # use append when you just need to add one element, use extend when there 
# print(x), then this will give ytou [4, True, 'hi', 'hello']
# you can use x.extend([4,5,5,5,5,5]), then this will add all of this onto the end of the list

# if you do print(x.pop())| print(x), then it will remove 'hi' from the list and just give you hi| [4, True]
# remember that in python, the first element of a list is 0, second is 1, and so on
# x = [4, True, 'hi']| print(x.pop(0))| print(x), then the 4 will by itself, and [True, 'hi'] will be printed next
# x = [4, True, 'hi']| x[0] = 'hello'| print(x), ['hello', True, 'hi'] will be printed next
# x = [4, True, 'hi']| y = x| x[0] = 'hello'| print(x, y) #it will print the same thing
# x = [4, True, 'hi']| y = x[:], this means that y will be a copy of x

# tupples work the same as lists except that they are immuitable, so you can you use round brackets
# this means that once they are created, their elements cannot be modified or changed. You cannot add, remove, or latger elements in a tuple after it's been defined 

## FOR LOOPS
# for variable in iterable:
    # code to be executed for each iteration
# variable: This is a variable that takes the value of the item inside the iterable on each iteration. You can choose any valid variable name.
# iterable: This is the object over which the loop is iterating. It could be a list, tuple, string, dictionary, or any other iterable object.
# The indented block of code beneath the for statement is the body of the loop. This block is executed for each item in the iterable.

# for i in range(10):
#       print(i)

# if range(1), then it just stops at 10, if range(1,10), then it goes from 1-10, if range(1,10,2), this is start, stop, step

# x = [3,4,42,3,2,4]

# for i in range(len(x)):
#       print(x[i])      #get the numbers we want

# x = [3,4,42,3,2,4]

# for i, element in enumerate(x):
#    print(i, element)


## WHILE LOOPS

#x = [3,4,42,3,2,4]

#i = 0
#while i < 10 :
#    print('run')
#    i += 1
#    while True
#    if i == 10:
#        break
#    i += 1 #way of saying i = i + 1


## SLICE OPERATOR, allows us to take a slice of a collection

# x = [0,1,2,3,4,5,6,7,8]
# y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# s = "hello"

# sliced = x[start:stop:step]
# sliced = x[0:4:2] # since we are going up to 4 here, it will not be in the final result
# sliced = x[:4] # The colon is saying to start at the beginning and then end at 4, if it was sliced = x[2:] then it would go from 2 till the end
# can do sliced = x[4:2:-1], which means start at 4 and step down by -1 to 2

# print(sliced)


## SETS

# s = {}, this is the representation of a set
# x = set()
# s = {4,32,2,2}
# s2 = {3,4,22,1}
# print(s) # doing this will give you {32, 2, 4}, a random order and the duplicate 2's were removed
# s.add(5) # this adds 5 to the set
# s.remove (5) # gives us an error since there is not a 5 there, will remove a integer if it's in the set
# print(s)

# print(4 in s) # will tell us if within s, there is a 4. There is, so it yields true

# print(s.union(s2)) # reference to lines 148 and 149, puts all numbers from both sets into one

## RANDOM ASIDE, WHAT ARE HASH COLLISIONS

## DICTS, a dictionary is estentially a key value pair. So everything is a value that corresponds to something else in the dictionary
# Dictionary Key:
# In the context of dictionaries, a "key" refers to one of the unique identifiers used to access a value. 
# Dictionaries in Python are composed of key-value pairs, where each key must be unique within the dictionary. 
# You use the key to retrieve the associated value. IMPORTANT

# students = [
#    {"name": "Alice", "age": 22},
#   {"name": "Bob", "age": 20},
#    {"name": "Charlie", "age": 25}
#]

# Sorting students based on age
#sorted_students = sorted(students, key=lambda x: x["age"])
#print(sorted_students)

# In this example, the key parameter specifies a lambda function that extracts the "age" from each dictionary, and the list is sorted based on these extracted ages.

# lambda arguments: expression
# lambda: The keyword that tells Python you're creating a lambda function.
# arguments: The input parameters of the function.
# expression: The operation to be performed using the input parameters.

# add_lambda = lambda x, y: x + y, this shows that when you use the function it will add the numbers together

# x = {'key': 4}, # x = {'key': some value it corresponds to}, the value can be a list, single value like 4, 
# print(x['key'])
# x['key2'] = 5 # therefore key 2 within x corresponds to 5
# x[2] = 8 # so for x, the 2 corresponds to 8
# print(x)
# print('key' in x), result says True
# print(list(x.values())), result says dict_values([4]), wqhen you do this though you will want to make it a list, line 170 shows that
# print(list(x.values()))

# del x['key'], so this will delete the key, and when you print below the key is gone so the result is {}
# print(x)

# for key, value in x.items():         # so if you want to loop through all the keys and all of the items, do x.items()
#        print(key, value)

# for key in x:     # this will give me all the keys in x
#        print(key, x[key])    # yields the same as line 180 and 181


## COMPREHENSIONS, python may be one of the only coding languages that has these
# these are basically a one line initialization of a list, tupal


# x = [x for x in range(5)]
# x = [x + 5 for x in range(5)], output is [5,6,7,8,9]
# x % 5: This is the expression inside the list comprehension. It calculates the remainder when x+5 is divided by 5.
# x = [[4 for x in range(10)] for x in range(5)] # so this gives me 5 groups of 10 4's
# x = [i for i in range(100) if i % 5 == 0] # gives you all the values from 0 through 95
# x = {i:0 for i in range(100) if i % 5 == 0} # makes this a dictionary
## WHAT'S A GENERATOR OBJECT
# x = tuple(i:0 for i in range(100) if i % 5 == 0)
# print(x)

# FUNCTIONS, HECK YA

#def func():    # you are defining your function name, you can put functions within functions if you wanted to
#    print('Run')    # functions are technically objects so you can return them
# func()   # you are calling the function out here to be used

# def func(x, y, z=None):    # this means that if there is no z value, nothing will show up. If there is a z value, it will override this
#    print('Run', x, y, z)
#    return x * y, x / y

# r1, r2 = func(5, 6)
# print(r1, r2)

## UNPACK OPERATOR AND ARGS (Arbitrary Arguments)/KWARGS(Keyword Arguments)

# functions are objects, so they can be passed around just like variables
# sometimes you just have to delete the history
# def func(x):
#    def func2():
#        print(x)
#
#    return func2

# x = func(3)
# x()    # so x was equal to func2, review this

#def func(*args, **kwargs):
 #   pass

#x = [1,23,236363,2727]
#print(*x)   # this means unpack x, so the output is 1 23 236363 2727
# if you just do print(x), it gives you [1, 23, 236363, 2727] 
#def func(x,y):
#    print(x, y)

#pairs = [(1,2), (3,4)]

#for pair in pairs:
#    func(*pair)     # In python, this take both pairs, uinpack them and separate them

# The *args syntax in a function definition allows the function to accept any number of positional arguments. 
# These arguments are passed to the function as a tuple.
# **kwargs allows a function to accept any number of keyword arguments, which are passed to the function as a dictionary.

#def func(x,y):
#    print(x, y)

#pairs = [(1,2), (3,4)]

#for pair in pairs:
#    func(**{'x': 2, 'y':5})      # saying to make x's a 2, and make y's a 5
#    # func(**{'y':5, 'x': 2}) this way works too, it doesn't have to be the correct order

#def func(*args, **kwargs):
#    print(*args, kwargs)

#func(1,2,3,4,5, one=0, two =1)  #doesn't make much sense but you can see how the keyword arguments and positional arguments work


## SCOPE AND GLOBALS

# x = 'tim'

# def func(name):
#    global x
#    x = name

# print(x)
# func('changed')
# print(x)

## EXCEPTIONS

# raise Exception('Bad')
#try:
 #   x = 7 / 0
#except Exception as e:
#    print(e)
#finally:
#    print('finally')

## Lambda      it is a one line anonomous function
# x = lambda x, y: x + 5


## Map and Filter

x = [1,2,3,4,5,3,3,21,2,21,2,313,1,23,142,4]

#mp = map(lambda i: i + 2, x )
#print(list(mp))

# mp = filter(lambda i: i % 2 == 0, x)    # lambda is good for when you don't wnat to define your entire function, just a filtered statement
# print(list(mp))


## F -strings

# tim = 89
# x = f'hello{6 + 8} {tim} {67 + 9}'
# print(f'hello {tim}')


