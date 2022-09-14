from cmath import sqrt
import string
import math
from traceback import print_tb
import numpy as np
import random
import time



starter_char  = ["(", "4", "(", "4", "(", "4", "(", "4", "sqrt("] #, "math.factorial("]
starter_char_not_4  = ["(", "sqrt("] #, "math.factorial("]
chars_following_4_or_bracket = ["4", "4", "(", "(", "sqrt("] #, "math.factorial("]
chars_following_4 = ["4", "+", "-", "*", "/"]
chars_following_4_if_open_bracket = ["4", "+", "-", "*", "/", ")"]

general_operators = ["+", "-", "*", "/"]


open_bracket = 0
open_sqrt = False
open_factorial = False

equation = []
equation_example = [""] * 50


current_goal = 0

number_of_equations = np.zeros(50)

samples = 100000

while number_of_equations[3] == 0:
    for x in range(samples):
        equation = []
        while equation.count("4") < 4:


            if len(equation) == 0:
                equation.append(starter_char[random.randint(0,8)])
                if equation[-1] in starter_char_not_4:
                    open_bracket += 1
                
            if equation[-1] in starter_char_not_4:
                equation.append(chars_following_4_or_bracket[random.randint(0,4)])
                if equation[-1] in starter_char_not_4:
                    open_bracket += 1

            if equation[-1] == "4":
                if open_bracket > 0:
                    equation.append(chars_following_4_if_open_bracket[random.randint(0,4)])
                else:
                    equation.append(chars_following_4[random.randint(0,4)])
            
            if equation[-1] == ")":
                equation.append(general_operators[random.randint(0,3)])

            if equation[-1] in general_operators:
                equation.append(starter_char[random.randint(0,8)])
                if equation[-1] in starter_char_not_4:
                    open_bracket += 1


            #print(equation)
            #time.sleep(.1)

        #print(open_bracket)
        
        while open_bracket > 0:
            equation.append(")")
            open_bracket -= 1

            #print("".join(equation))
            #print(open_bracket)

        

        
            
        try:
            output_value = eval("".join(equation))
            #print(output_value)
            if  output_value < 50:
                if output_value >= 0:
                    if (output_value).is_integer() == True:
                        if equation.count("4") == 4:
                            number_of_equations[int(output_value)] += 1

                            if equation_example[int(output_value)] == "":
                                equation_example[int(output_value)] = str(str(int(output_value)) + " = " + str("".join(equation)))
                            
                                
                            if int(output_value) == current_goal:
                                #print("here")
                                #print(str(int(output_value)) + " = " + str("".join(equation)))
                                current_goal += 1
                                
                            else:
                                pass 
                                
                

        except:
            #print("failed")
            pass

        #time.sleep(1)
        #if ((x/samples)*100).is_integer() == True:
            #print((x/samples)*100)

    for x in range(50):
        if equation_example[x] != "":
            print(equation_example[x])


    print(number_of_equations)


print("done")

time.sleep(15000)


    
