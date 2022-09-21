n = 1
run = True

def flippblipp(n):
    if (n % 3 == 0 and n % 5 == 0):
        return ("flipp blipp")
    elif(n % 3 == 0):
        return("flipp")
    elif (n % 5 == 0):
        return("blipp")
    else:
        return(str(n))
    
print("      ", 1)  
while(run == True):
    n = n + 1
    correct_answer = flippblipp(n)
    user_input = input("Nästa: ")
    if (user_input != correct_answer):
        print("Fel - ", correct_answer)
        print()
        print("Game Over")
        run = False
    
    