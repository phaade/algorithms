#write a program to ask for a name until the user enters end print the name each time when you are done print i am done
# name = " "
# while name != "end":  #while name is not = end continue running the program
#     name = input("what is your name: ")
#     print(name)
#     if name == "end":
#         print("i am done")


# method 2

start = 0
end = 1

while start != end:
    name = input("enter a name ")
    start -= 1
    if name != "end":
        print(name)
    else:
        print("i am done")  
        break  
    

