#独学programmer chapter3~8
#chapter3
#Hello, World! * 100
for i in range(5):
    print("Hello, World!")

#print others
print("Python")
print("こんにちは！")
print\
    ("""It is very very very very
    very long multiple lines.""")

#constants and variables
a = 10
b = 5
print(a + b, a - b, a * b, a / b, a % b)
greeting_morning = "Hi, how are you?"

#arithmeric operators
x = 7
y = 3
print(x ** y, x // y, x % y)
print(x < y and x != y)
print(x >= y or not x == y)

#conditionals
home = "America"
if home == "Japan":
    print("日本の皆さんこんにちは！")
elif home == "China":
    print("大家好在中国！")
else:
    print("Hello everybody in the world!")

#chapter4 function
class Function:
    def __init__(self, str, int):
        self.str = str
        self.int = int

    def built_in_function(self):
        if self.int % 2 == 0:
            print(self.str + " " + str(len(self.str)))

function = Function("apple", 4)
function.built_in_function()

#optional argument
def option(num = 2):
    return num ** 10

print(option())
print(option(5))

#scope
#use variables at 20th line
def just_print():
    print(x)
    print(y)

just_print()

def just_print2():
    x = 5
    y = 1
    print(x)
    print(y)

just_print2()

#chapter5
#list
vegetables = ["carot", "potato", "cucumber", "pumpkin"]
vegetables.append("watermelon")
count = 0
while count < 5:
    if len(vegetables[count]) == 6:
        print("It's a potato!!!")
    count += 1

#taple
killer = ("crocodile", "dog", "snake")
print(killer)

#dictionary
killer_animals = {"crocodile":10 ,"dog":4 ,"snake":3}
killer_animals["human"] = 2
print(killer_animals)

#two-dimensional array
def times_tables():
    if table * times < 10:
        print(" " + str(table * times), end=" ")
    else:
        print(table * times, end=" ")

for table in range(1,10):
    for times in range(1,10):
        times_tables()
    print()

#chapter6 string operation
#upper and lower
desire = "I WANNA GET THE FREEDOM".lower()
desire2 = "I'll be a millionaire".upper()
print(desire + " and " + desire2)

#format
print("Hi, {}. How old are you?".format("William"))

#division and union
complain = "why I couldn't use f-string".split()
print(complain)
complain_fixed = " ".join(complain)
print(complain_fixed)

#removal and replace
remove = " (  ' 3     '  )".strip()
print(remove)
removed_space = remove.replace(" ", "")
print(removed_space)

#index and in
print("tomatomato".index("a"))
print("atom" in "tomatomato")

#escape and \n
print("\"do you understand it?\"")
print("ty\nao\ntm\nei")

#slice
words = "alive or dead"
print(words[9:],words[6:8],words[0:5])

#loop
#I've already done "for" at 4th line
#I've already done "while" at 77th line
nums = 0
while True:
    if nums == 7: break
    if nums == 4:
        nums += 2
        continue
    print(nums)
    nums += 1

#I've already done "nesting loop" at 91st line

#chapter8 module
def modules():
    import math
    import random
    print(math.pi * random.randint(5,10))
modules()
