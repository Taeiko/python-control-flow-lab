# # Exercise 1: Vowel or Consonant
# #
# # Write a Python function named `check_letter` that determines if a given letter
# # is a vowel or a consonant.
# #
# # Requirements:
# # - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# # - It should handle both uppercase and lowercase letters.
# # - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# # - If the letter is a consonant, print: "The letter x is a consonant."
# # - Replace 'x' with the actual letter entered by the user.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Utilize the `in` operator to check for vowels.
# # - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     # Your control flow logic goes here
#     letter = input('Enter the letter:').lower()
#     if letter =='a' or letter == 'e' or letter == 'i' or letter =='o' or letter == 'u':
#         print('the letter is a vowel')
#     else:
#         print('the letter is consonant!')
# # Call the function
# check_letter()




# # Exercise 2: Old enough to vote?
# #
# # Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# # Fill in the logic to perform the eligibility check inside the function.
# #
# # Function Details:
# # - Prompt the user to input their age: "Please enter your age: "
# # - Validate the input to ensure the age is a possible value (no negative numbers).
# # - Determine if the user is eligible to vote. Set a variable for the voting age.
# # - Print a message indicating whether the user is eligible to vote based on the entered age.
# #
# # Hints:
# # - Use the `input()` function to capture the user's age.
# # - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# # - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     # Your control flow logic goes here
#     voting_age = input('please enter your age').lower()
#     if int(voting_age) > 21:
#         print('you are old enough')
#     else:
#         print('you are not old enough!')

# # Call the function
# check_voting_eligibility()



# # Exercise 3: Calculate Dog Years
# #
# # Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# # Fill in the logic to perform the calculation inside the function.
# #
# # Function Details:
# # - Prompt the user to enter a dog's age: "Input a dog's age: "
# # - Calculate the dog's age in dog years:
# #      - The first two years of the dog's life count as 10 dog years each.
# #      - Each subsequent year counts as 7 dog years.
# # - Print the calculated age: "The dog's age in dog years is xx."
# # - Replace 'xx' with the calculated dog years.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Convert the string input to an integer using `int()`.
# # - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     # Your control flow logic goes here
#     dog_years = input('please enter dog/s age')
#     dog_year_results = 0
#     for year in range(1,int(dog_years)+1):
#         if year == 1 or year == 2:
#             dog_year_results+= 10
#         else:
#             dog_year_results +=7
        
#     print(f'your dog is {dog_year_results} old.')

# # Call the function
# calculate_dog_years()





# # Exercise 4: Weather Advice
# #
# # Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
# #
# # Requirements:
# # - The script should prompt the user to enter if it is cold (yes/no).
# # - Then, ask if it is raining (yes/no).
# # - Use logical operators to determine clothing advice:
# #   - If it is cold AND raining, print "Wear a waterproof coat."
# #   - If it is cold BUT NOT raining, print "Wear a warm coat."
# #   - If it is NOT cold but raining, print "Carry an umbrella."
# #   - If it is NOT cold AND NOT raining, print "Wear light clothing."
# #
# # Hints:
# # - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice():
#     # Your control flow logic goes here
#     cold = input('is it cold?').lower()
#     raining = input('is it raining?').lower()
    
#     if  cold ==  'yes' and raining=="yes":
#         print('Wear a waterproof coat.')
#     elif cold == 'yes' and raining == 'no':
#         print('Wear a warm coat.')
#     elif cold == 'no' and raining == 'yes':
#         print('Carry an umbrella.')
#     elif cold == 'no' and raining == 'no':
#         print('wear light clothing')
# # Call the function
# weather_advice()




# Write a Python script named `fizz_buzz` that prints numbers from 1 to 50, but:
# - For multiples of 3, print "Fizz" instead of the number.
# - For multiples of 5, print "Buzz" instead of the number.
# - For multiples of BOTH 3 and 5, print "FizzBuzz".
#
# Requirements:
# - Use a loop to iterate through numbers from 1 to 50.
# - Use conditional statements to check divisibility.
# - Print each result on a new line.
#
# Hints:
# - Use the modulo operator `%` to check if a number is divisible by another.
# - Check for multiples of BOTH 3 and 5 first to avoid missing them.
#
def fizz_buzz():
    # Your loop and condition logic goes here
    for num in range(1, 50):
        if num%3 ==0:
            print('fiz')
        elif num%5 ==0:
            print('buzz')
        elif num%3 ==0 and num%5 ==0:
            print('fizzbuzz')


# Call the function
fizz_buzz()