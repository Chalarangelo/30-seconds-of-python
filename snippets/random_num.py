#random number generator
import random  
run = True


print("Welcome to random number generator")       
first_num = int(input("Type in a number where you would like to start "))    
second_num = int(input("Type in a number where you would like to end "))   
randomnum = random.randint(first_num, second_num)      
print(str(randomnum))             
