# in keyword check the existence of a character in a string
for i in range(1, 101):
    i = int(input("enter a number: "))

    #print(i)
    if i % 3 == 0 and i % 5 ==0:
        print("fizzball")
    elif i > 100:
        print("not in range")    
    elif i % 3 != 0 and i % 5 != 0:
        print("not divisible")   
    elif i % 5 == 0:
        print("ball")
    elif i % 3 == 0:
        print("fizz") 
    else:
        print(i)  
