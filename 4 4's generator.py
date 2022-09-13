
import string
import math
from traceback import print_tb
import numpy as np
import random
import time



starter_char  = ["(", "(", "4", "4", "sqrt(", "math.factorial("]
starter_char_not_4  = ["(", "sqrt(", "math.factorial("]
factorial_char = ["-", "/", ")"]
sqrt_char = ["-", "/", "*", ")"]
general_operators = ["+", "-", "*", "/"]

open_bracket = 0
open_sqrt = False
open_factorial = False

equation = []
equation_example = [""] * 50


current_goal = 0

number_of_equations = np.zeros(50)

for x in range(200000):
    equation = []
    while equation.count("4") < 4:


        if len(equation) == 0:
            equation.append(starter_char[random.randint(0,5)])
            if equation[-1] == "(":
                open_bracket += 1

            

        


        if equation[-1] == "sqrt(":
            equation.append("4")
            equation.append(sqrt_char[random.randint(0,3)])
            if equation[-1] != ")":
                equation.append("4")

            equation.append(")")
            
        if equation[-1] == "math.factorial(":
            equation.append("4")
            equation += sqrt_char[random.randint(0,3)]
            if equation[-1] != ")":
                equation.append("4")

            equation.append(")")

        if equation[-1] == "4":
            if random.randint(0, 20) == 0:
                equation.append("4")

        if equation[-1] == "(":
            equation.append("4")

            



        if equation[-1] == ")" or equation[-1] == "4":
            equation.append(general_operators[random.randint(0,3)])
            equation.append(starter_char[random.randint(0,5)])
            if equation[-1] == "(":
                open_bracket += 1 



    
    


        


    while open_bracket > 0:
        equation.append(")")
        open_bracket -= 1

    
        
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
        pass

for x in range(50):
    if equation_example[x] != "":
        print(equation_example[x])


print(number_of_equations)

print("done")

time.sleep(15000)


    