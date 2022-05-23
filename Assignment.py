#program to accept radius from user and calculate area of a circle

# radius = float(input("What is the radius of the circle: "))
# pi = 3.14
# area = pi * radius * radius
# print("Area of circle is: " +str(area))


#program to calculate volume of a sphere given r = 6
# radius = 6.0
# pi = 3.14
# volume = (4.0/3.0) * (pi * radius * radius * radius)
# print("The volume of the sphere is: " +str(volume))

#program that validate a password if the password is lesser than 6 character or greater than 12 - reject

# p = (input("Enter your password: "))

# if len(p) < 6 or  len(p) > 12:
#     print("password rejected ")
# else:
#     print("password accepted ")    

#loop way of executing blocks of code in a continuous manner or respectively

#while loop executes a block of code as long as the condition stated is true and stops when the condition ceases to be true

# x = 1
# while x <= 10:
#     print(x)
#     x += 1

#assignment 10 - 0, -30 - +30, 30 - 0(even numbers)
# x = 10
# while x >= 0:
#     print(x)
#     x -= 1

# x = -30
# while x <= 30:
#     print(x)
#     x += 1

# x = 30
# while x >= 0:
#     print(x)
#     x -= 2

# break statement -  this is used to completely jump out of a loop.

# x = 1
# while x <= 10:
#      if x == 6:
#          break
#      print(x)
#      x += 1

# x = -30
# while x <= -1:
#     if x == 0:
#         break
#     print(x)
#     x += 1

#continue statement
# x = -30
# while x <= 30:
#     if x == 0:
#         x += 1
#         continue
#     print(x)
#     x += 1

#for loop: used to iterate through a collection of characters/ sequence of integer/ collection of arrays

#for variable in string/range/list/dictionary
# word = "python program"
# for x in word:
#     if x == " ":
#         continue
#     print(x)

#range function
# range(11)
# range(1, 11)
# range(0, 11, 2) #counts in twos

# for i in range (int(input("enter a range "))):
#     if i == 5:
#         break
#     print(i)

for i in range(1, 101):
    #print(i)
    if i % 3 == 0 and i % 5 ==0:
        print("fizzball")
    elif i % 5 == 0:
        print("ball")   
    elif i % 3 == 0:
        print("fizz") 
    else:
        print(i)        

#write a program to keep asking for a number until it enters a negative number
#write a program to ask for a name until the user enters end print the name each time when you are done print i am done
#while loop

# x = 0

# while x >= 0:
#     x = int(input("Enter a number: "))
#     if x < 0:
#         print("program ended")
#         break

#guessing game 
#if a user guesses right, it should return you win otherwise you loose a user should be giving 3 trials after the 3rd trial it shoulf return you lose

# i = 1
# while i <= 3:
#     code = int(input("what is the code "))
#     i = i + 1
#     if code == 1234:
#         print("you win ")
#         break
#  else:
#         print("game over ")    

#converter ask user to enter unit

# n = float(input("what is your weight: "))
# k = input("what is your unit: ")
# print("my weight is " +str(n)+ " " +k)
# #conversion of weight to kg/g

# #wg = n/1000
# #wkg = n * 1000
# p = input("what is your current unit after conversion: ")
# print("my current weight after conversion is: " +str(wg)+ " " +p)




    




