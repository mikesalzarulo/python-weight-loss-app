#
# Michael Salzarulo
#
# weight.py
#
# A weight loss pal that prompts the user for a menu option and then displays weight loss
# options or projections dependent on the choice.
#
# Algorithm
# Display menu: 1. Display "10 ways to cut 500 calories" guideline.
#               2. Generate next semester expected weight table.
#               3. Quit
# Input: A number (1-3).
# Processing: 1. Display menu.
#             2. Promt user for number (1-3). 
#             3. Determine if number is 1 and display weight loss options.
#             4. Determine if the number is 2, prompt weight, and display projections.
#             5. Determine if the number is 3 and quit.
#             6. Display result.
# Output: Try these 10 ways/ Weight table.
#

# Define main function.
def main():

    # Declare variables.
    option = 0
    month = 0
    weight = 0
    # Intro.
    print('500 Less a Day Makes the Weight Go Away ...')

    # Continues the loop until a value of 3 is entered.
    while option != 3:

    # Display menu and prompt for menu option.
        option = int(input('Choose one of the following options:\n'+
                   '1. Display "10 ways to cut 500 calories" guideline.\n'+
                   '2. Generate next semester expected weight table.\n'+
                   '3. Quit.\n'+
                   'Option: '))        

        # Tests if input is within menu range.
        if option >= 1 and option <= 3:

            # Prints weight loss options if user chooses option 1.
            if option == 1:
                print('Try these 10 ways to cut 500 calroies every day.\n'+
                      '* Swap you snack.\n'+
                      ' * Cut one high-calorie treat.\n'+
                      ' * Do NOT drink your calories.\n'+
                      ' * Make low calorie substitutions.\n'+
                      ' * Ask for a doggie bag.\n'+
                      ' * Just say no "no" to fried food\n'+
                      ' * Build a thinner pizza.\n'+
                      ' * Use a smaller plate.\n'+
                      ' * Avoid alcohol.\n'+
                      'Source: US National Library of Medicine.')

            # Enters the control structure of option 2.
            elif option == 2:
                # Prompts for and stores the value of weight in its variable.
                weight = int(input('Please enter starting weight in pounds (>=100): '))
                # Validates if weight is greater than or equal to 100lbs and proceeds to projections if it is.
                if weight >= 100:

                    # Returns projected weight table header.
                    print('-----------------\n'+
                          'Month   Weight\n'+
                          '-----------------')
                    # Calculates and returns projected weight table.
                    for month in range(1,7):
                        PROJWEIGHT = weight - (month * 4)
                        print(month, '     ', PROJWEIGHT)
                # Validates for correct weight if under 100lbs.       
                elif weight < 100:
                    # Enters a loop to find correct weight until equal to or over 100lbs.
                    while weight < 100:
                        # Throws error in loop until valid.
                        print('Error ... Invalid weight. Try Again')
                        # Prompts for valid weight.
                        weight = int(input('Please enter starting weight in pounds (>=100): '))
                        # Enters control statement if valid
                        if weight >= 100:
                            # Loops and prints valid table.
                            for month in range(1,7):
                                # Calling constant in function to be used
                                PROJWEIGHT = weight - (month * 4)
                                # Prints valid table for user and exits loop.
                                print(month, '     ', PROJWEIGHT)
                            # Breaks loop in case of error.
                        else:
                            break
                                
                # Validates if weight is within criteria.   
                else:
                    break
                    
                    
            # Ends the loop if user decides.
            elif option == 3:
                # End of loop goodbye.
                print('Good Bye ...')
                # Breaks the loop.
                break
        # Prints error if input is not in range.
            else:
                print('That option is not valid.')

    # Prints error if input is not in range.        
        else:
            print('That option is not valid.')
main()
