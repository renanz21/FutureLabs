#Personalized Birthday Wishes

print("Recipient's name: ")
r_name = str(input()) #Variable to store recipients name

print("Year of birth: ")
b_year = int(input()) #Variable to store birth year

print("Personalized message: ")
message = str(input()) #Variable to store main message

print("Senders name: ")
s_name = str(input()) #Variable to store senders name

r_age = 2025 - b_year # variable to calculate age based on current year 2025

print(f"{r_name}, let's celebrate your {r_age} years of awesomeness! \n"
      f"Wishing you a day filled with joy and laughter as you turn {r_age}!\n\n"
      
      f"{message}\n\n"

      "With love and best wishes, \n"
      f"{s_name}")

#Output with variables filled with input provided
