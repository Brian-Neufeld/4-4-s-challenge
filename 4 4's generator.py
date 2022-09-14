
import string
import math
from traceback import print_tb
import numpy as np
import random
import time
import re
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


import warnings

def fxn():
    warnings.warn("deprecated", SyntaxWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn() 

""" starter_char  = ["(", "4", "(", "4", "(", "4", "(", "4", "sqrt("] #, "math.factorial("]
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

 """

max_equation_length = 12

example_equation = [""] * 50
all_chars = ["4", "+", "-", "*", "/", "(", ")", ".", "sqrt(", "math.factorial("]
starter_chars = ["4", "(", ".", "sqrt(", "math.factorial("]
equation = [""] * max_equation_length
str_equation = ""

number_of_equations = np.zeros(50)

def evalute_equation(length, equation):

    for x in range(length):

        equation[x] = all_chars[globals()[str(string.ascii_lowercase[x])]]
        if x == 0:
            equation[0] = starter_chars[a]


    

    
                                    
        
    str_equation = "".join(equation[:length])
    """  if str_equation.count("4") != 4:
        equation = [""] * max_equation_length
        str_equation = ""
        pass """
    #print(str_equation)
    #str_equation = str_equation[:length]

    if "math.factorial(" in equation:
        str_equationtest = str_equation.replace("(", "#")
        str_equationtest = str_equationtest.replace(")", "$")
        #print(str_equationtest)


        result = re.search('math.factorial#(.*)$', str_equationtest)

        #print(result)

        if result != None:    
            if result.group(1) != None:
                if result.group(1) != "":
                    #time.sleep(1)
                    #print(result.group(1))

                    try:
                        factorial_insides = eval(result.group(1))
                        if (factorial_insides).is_integer == True:
                            if factorial_insides >= 0:
                                if factorial_insides <= 10:
                                    pass
                                
                                else:
                                    equation = [""] * max_equation_length
                                    str_equation = ""

                        else:
                            equation = [""] * max_equation_length
                            str_equation = ""




                    except:
                        equation = [""] * max_equation_length
                        str_equation = ""
                        


    #time.sleep(.1)


    if str_equation.count("**") > 0:
        str_equation = ""
        equation = [""] * max_equation_length

    if str_equation.count("//") > 0:
        str_equation = ""
        equation = [""] * max_equation_length

    if str_equation.count("++") > 0:
        str_equation = ""
        equation = [""] * max_equation_length    

    if str_equation.count("--") > 0:
        str_equation = ""
        equation = [""] * max_equation_length                            

    if str_equation.count("+-") > 0:
        str_equation = ""
        equation = [""] * max_equation_length    

    if str_equation.count("-+") > 0:
        str_equation = ""
        equation = [""] * max_equation_length    

                                    

    try:
                                        
        #print(str_equation)
        output_value = eval(str_equation)

        #print(output_value)
        if  output_value < 50:
            if output_value >= 0:
                if (output_value).is_integer() == True:
                    if str_equation.count("4") == 4:
                        number_of_equations[int(output_value)] += 1

                        if example_equation[int(output_value)] == "":
                            #print("here")
                            example_equation[int(output_value)] = str_equation
                            #print(example_equation[int(output_value)])

                            print(f"{int(output_value)} = {example_equation[int(output_value)]}")
                        
                        
                        str_equation = ""
                        equation = [""] * max_equation_length
                        
                                            
            equation = [""] * max_equation_length
            str_equation = ""

    except:
        equation = [""] * max_equation_length
        str_equation = ""
        pass

    #print("")
    #time.sleep(1)

global a,b,c,d,e,f,g,h,i


for a in range(4):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                evalute_equation(4, equation)
                for e in range(10):
                    evalute_equation(5, equation)
                    for f in range(10):
                        print(f"{a}{b}{c}{d}{e}{f}")
                        evalute_equation(6, equation)
                        for g in range(10):
                            evalute_equation(7, equation)
                            for h in range(10):
                                evalute_equation(8, equation)
                                for i in range(10):
                                    evalute_equation(9, equation)
                                    for j in range(10):
                                        evalute_equation(9, equation)
                                        for k in range(10):
                                            evalute_equation(9, equation)
                                            #for l in range(10):
                                            #    evalute_equation(9, equation)
                                                

                                    
                                    """ equation[0] = starter_chars[a]
                                    equation[1] = all_chars[b]
                                    equation[2] = all_chars[c]
                                    equation[3] = all_chars[d]
                                    equation[4] = all_chars[e]
                                    equation[5] = all_chars[f]
                                    equation[6] = all_chars[g]
                                    equation[7] = all_chars[h]
                                    equation[8] = all_chars[i]
                                    #print(i)
                                    #print(equation[8])
                                    
        
                                    str_equation = "".join(equation)
                                    str_equation = str_equation[:9]

                                    if str_equation.count("**") > 0:
                                        str_equation = ""
                                        equation = [""] * max_equation_length

                                    if str_equation.count("//") > 0:
                                        str_equation = ""
                                        equation = [""] * max_equation_length

                                    
                                    
                                    #print(str_equation)
                                    

                                    try:
                                        
                                        #print(str_equation)
                                        output_value = eval(str_equation)

                                        #print(output_value)
                                        if  output_value < 50:
                                            if output_value >= 0:
                                                if (output_value).is_integer() == True:
                                                    if str_equation.count("4") == 4:
                                                        number_of_equations[int(output_value)] += 1
                                                        #print(int(output_value))
                                                        #print(str_equation)
                                                        str_equation = ""
                                                        equation = [""] * max_equation_length
                                                        #time.sleep(5)
                                        
                                        equation = [""] * max_equation_length
                                        str_equation = ""

                                    except:
                                        equation = [""] * max_equation_length
                                        str_equation = ""
                                        pass

                                    #print("")
                                    #time.sleep(1) """

                                    

print(number_of_equations)
print(example_equation)

print("done")

time.sleep(150000)


    
