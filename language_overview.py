# importing packages
import random
import sys
import os

print("Hello World")

# single line comment
''' multiline comment
going on '''

print("next line")

name="shiv"
print(name)

# [5]data types can be Numbers Strings Lists Tuples Dictionaries
# [7] operators can be +-*/% **(exponential) // (divide and discard remainder)
print("5+2=", 5+2)
print("5-2=", 5-2)
print("5*2=", 5*2)
print("5/2=", 5/2)
print("5%2=", 5%2)
print("5**2=", 5**2)
print("5//2=", 5//2)

# bodmas rule applicable here also

print("\"Its a great day!\"")

# its a common convention to add _ (underscore) in variable names

first_name ="\"shiv"
print(first_name)

multi_line_quote='''great 
piece of code '''

print("%s %s" %("hello", first_name))
# LIST --------------------------------------------

grocery_list=['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First_Item', grocery_list[0])
print(grocery_list[1:3])

other_events=['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list=[other_events, grocery_list]
print(to_do_list)
print(to_do_list[0][0])

grocery_list.append('Onions')
print(to_do_list)
grocery_list.insert(1,'Pickle')
print(grocery_list)
grocery_list.remove('Pickle')
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)
del grocery_list[4]
print(grocery_list)

to_do_list2 = other_events + grocery_list
print(to_do_list2)
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#TUPLE cannot be changed after it is created ----------------
pi_tuple =(3,1,4,1,5,9)
print(pi_tuple)
new_tuple= list(pi_tuple)
print(new_tuple)
new_list= tuple(new_tuple)
print(new_list)

print(len(pi_tuple),min(pi_tuple), max(pi_tuple))

#Dicionaries are basically MAPs -----------------------------

species={'animal':'walk',
                'bird':'fly',
                'fish':'swim'
                }
print(species['animal'])
del(species['animal'])
print(species)
species['animal']='run'
print(len(species))
print(species.get("fish"))
print(species.keys())
print(species.values())

# conditionals if else elif == != > >= < <= ------------------
age =21
if age>16 :
    print("you are old enough to drive")
else :
    print("you not old enough to drive")
    
if age>=21:
    print("you can drive bus")
elif age >= 16:
    print("drive tractor :)")
else :
    print("you are nnot old enough to drive")
    
# logical operator and or not

if((age >=1) and (age<=18)):
    print("under 18")
elif((age == 21) or (age >=65)):
    print("adult")
elif not(age==30):
    print("30s")
else :
    print("except")

# Looping ------------------------------------------------

for x in range(0, 10):
    print(x)
print('\n')

for y in grocery_list:
    print(y)
    
for x in range(0,2):
    for  y in range(0,2):
        print(to_do_list[x][y])
        
random_num = random.randrange(0,100)
while(random_num !=15):
    print(random_num)
    random_num = random.randrange(0,100)
'''
i=0;
while(i<=20):
    if(i%2==0):
        print(i)
    elif(i==9):
        break;
    else:
        i+=1
        continue
'''
def add(n1, n2):
    return n1+n2
print(add(1e6,2e4))
'''
print("whats your name")
name=sys.stdin.readline()
print("hello",name)
'''
long_string="I'll catch you if you fall -  The Floor"
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[0:4]+" be there")
print("%c is my %s letter and my number %d is %.5f"%
('X','favroite', 1, .14))

# string functions
print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace('Floor','Ground'))
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)

# FILE --------------------------------------------------------
test_file =  open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("writing this text\n"))
test_file.close()
test_file= open("test.txt", "r+")
text_in_file = test_file.read();
print(text_in_file)
os.remove("test.txt")

# Objects -----------------------------------------------------
class Animal:
    __name=None # or ""
    __height = 0
    __weight = 0
    __sound = 0
    # contructor
    def __init__(self, name, height, weight, sound):
        self.__name=name
        self.__height=height
        self.__weight=weight
        self.__sound = sound
    # setter and getters i.e accessor and mutators
    def set_name(self, name):
        self.__name =  name
    def get_name(self):
        return self.__name
    def set_height(self, height):
        self.__height =  height
    def get_height(self):
        return self.__height
    def set_weight(self, weight):
        self.__weight =  weight
    def get_weight(self):
        return self.__weight
    def set_sound(self, sound):
        self.__sound =  sound
    def get_sound(self):
        return self.__sound
    def get_type(self):
        print("Animal")
    def to_string(self):
        return("{} is {}cm tall and {}kg and say {}".format(self.__name, self.__height,self.__weight, self.__sound))

cat = Animal("Pussy", 33, 10, "Meow")
print(cat.to_string())

# Inheritance
'''
class Dog(Animal):
    __owner=""
    def __init__(self, name, height, weight, sound, owner):
        self.__owner=owner
        super(Dog,self).__init__(name, height, weight, sound)
    def set_owner(self, owner):
        self.__owner=owner
    def get_owner(self):
        return self.__owner
    def get_type(self):
        print("Dog")
    def to_string(self):
        return("{} is {}cm tall,  {}kg,  say {} and owner is {} ".format(self.__name, self.__height,self.__weight, self.__sound, self.__owner))
    
spot =  Dog("Spot", 53, 23, "Ruff", "Shiv")
print(spot.to_string())
'''