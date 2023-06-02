#love calculator day 3/100
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1 = name1.lower()  
name2 = name2.lower()  



t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

true_count = t + r + u + e  

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

love_count = l + o + v + e  

chemistry = str(true_count) + str(love_count) 

if int(chemistry) < 10 or int(chemistry) > 90 : 
    print(" your score is", chemistry, ", you go together like coke and mentos") 
elif int(chemistry) >= 40 and int(chemistry) <= 50 : 
    print("Your score is ", chemistry,", you are alright together") 
else: 
    print("Your score is ", chemistry)
