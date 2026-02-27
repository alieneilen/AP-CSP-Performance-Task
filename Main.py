# MOST RECENT VERSION ----------------------------------------------------------------------------------------------------------------------------
# Snack Recommender Code
# Author: Lily Zajczenko
# Date: 02/09/26
# Description: This program asks the user various questions, that then lead the code to recommend the user a specific snack.
#-----------------------------------------------------------------
# SNACK LIST W/ SERVING AND CAL COUNT
# chocolate rice cakes = 60 calories for one cake serving
# peanuts= 160 calories per ounce serving
# pretzels = 110 for 1 ouce serving
# oreos = 270 cal for 5 oreo serving
# string cheese = 60 cal for 1 cheese serving
# blue heat takis = 150 cal for 1 ounce serving
# spicy snack wrap = 380 cal per wrap serving
#--------------------------------------------------------                                                                           
total_snacks = []                                                                                   # Empty list that will then store all snack choices

def main():                                                                                         # Function to figure out what snack to give user
    flavor = input("Do you want a sweet or savory snack? ")
    if flavor == "sweet":                                                                           # "If"" statement to categorize if snack will be savory or sweet                                        
            chocolate = input("Do you like chocolate?: ")                                           # First input on what type of snack asked
            if chocolate == "yes":
                calories = input("Would you like your snack to have high or low calories?: ")       # Second input on snack
                if calories == "high":                                                              # Correlating "If" statement 
                    print("You should try oreos!")
                    satisfied = input("Are you satisfied with this suggestion?: ")
                    while satisfied == "no":                                                        # While loop in order to repeat code when input is correct
                        more = input("Do you want another snack?: ")
                        if more == "yes":                                                           # "If" statement that gives specific outcomes
                            chocolate = "none"                                                      # Reset variables' values to help program run correctly
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)                                              # If not repeating original function, then code goes to next function (ends code)
                    while satisfied == "yes":                                                       # Second while loop
                        total_snacks.append("Oreos")                                                # Adds chosen snack to list
                        more = input("Do you want another snack?: ")
                        if more == "yes":
                            chocolate = "none"                                                      # "If" statement that gives specific outcomes
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)
                elif calories == "low":                                                             # Goes back to original "If" statement, gives extra outcomes/chances for new input
                    print("You should try a chocolate rice cake!")
                    satisfied = input("Are you satisfied with this suggestion?: ")
                    while satisfied == "no":
                        more = input("Do you want another snack?: ")
                        if more == "yes":                                                           # "If" statement that gives specific outcomes
                            chocolate = "none"                                                         
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)
                    while satisfied == "yes":
                        total_snacks.append("Chocolate rice cake")
                        more = input("Do you want another snack?: ")
                        if more == "yes":
                            chocolate = "none"                                                         
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)
            else:                                                                                   # "Else" statement to give last option for "If" statement
                print("If you don't like chocolate, you should try gummy bears!")
                satisfied = input("Are you satisfied with this suggestion?: ")
                while satisfied == "no":
                    more = input("Do you want another snack?: ")
                    if more == "yes":
                            chocolate = "none"                                                         
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                    else:
                            more == "done"
                            return total(total_snacks)
                while satisfied == "yes":
                    total_snacks.append("Gummy bears")
                    more = input("Do you want another snack?: ")
                    if more == "yes":
                            chocolate = "none"                                                         
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                    else:
                            more == "done"
                            return total(total_snacks)
    elif flavor == "savory":                                                                        # Repeats code for second flavor profile option, with different snack options and questions, but same code implementations                        
            spicy = input("Do you like spicy food?: ")                                              # Input on what type of snack asked
            if spicy == "yes":
                calories = input("Would you like your snack to have high or low calories?: ")       # Another input on snack
                if calories == "high":
                    print("You should try a McDonald's spicy snack wrap!")
                    satisfied = input("Are you satisfied with this suggestion?: ")
                    while satisfied == "no":
                        more = input("Do you want another snack?: ")
                        if more == "yes":
                            chocolate = "none"                                                         
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)
                    while satisfied == "yes":
                        total_snacks.append("McDonald's spicy snack wrap")
                        more = input("Do you want another snack?: ")
                        if more == "yes":
                            chocolate = "none"                                                        
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)
                elif calories == "low":
                    print("You should try blue heat takis!")
                    satisfied = input("Are you satisfied with this suggestion?: ")
                    while satisfied == "no":
                        more = input("Do you want another snack?: ")
                        if more == "yes":
                            chocolate = "none"                                                      
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)
                    while satisfied == "yes":
                        total_snacks.append("Blue heat takis")
                        more = input("Do you want another snack?: ")
                        if more == "yes":
                            chocolate = "none"                                                        
                            calories = "none" 
                            satisfied = "none" 
                            more = "none" 
                            spicy = "none" 
                            return main()
                        else:
                            more == "done"
                            return total(total_snacks)
            else:
                print("If you don't like spicy food, you should try string cheese!")
                satisfied = input("Are you satisfied with this suggestion?: ")
                while satisfied == "no":
                    more = input("Do you want another snack?: ")
                    if more == "yes":
                        chocolate = "none"  
                        calories = "none"                                                       
                        satisfied = "none" 
                        more = "none" 
                        spicy = "none" 
                        return main()
                    else:
                        more == "done"
                        return total(total_snacks)
                while satisfied == "yes":
                    total_snacks.append("string cheese")                                            #"Append." statement implemented to add chosen snack to final list
                    more = input("Do you want another snack?: ")
                    if more == "yes":
                        chocolate = "none"                                                       
                        calories = "none" 
                        satisfied = "none" 
                        more = "none" 
                        spicy = "none" 
                        return main()
                    else:
                        more == "done"
                        return total(total_snacks)
    else:                                                                                    
        print("Invalid input. Please try again.")                                                   # Reroutes user to beginning of list when improper input is used
        return main()

def total(list):                                                                                    # Second function to display final chosen snacks list
        print(f"All snacks chosen: {list}")                                                                            

main()                                                                                              # Run the program