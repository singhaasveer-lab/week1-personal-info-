def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value.title()

        print("Input cannot be empty. Please try again.")


print("=" * 35)
print("PERSONAL INFORMATION MANAGER")
print("=" * 35)
print()

name = "Alex Johnson"
age = 22
city = "San Francisco"
hobby = "Playing Guitar"

favorite_food = get_non_empty_input("What's your favorite food? ")
favorite_color = get_non_empty_input("What's your favorite color? ")

age_in_months = age * 12

print()
print("=" * 35)
print("YOUR INFORMATION")
print("=" * 35)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

print("=" * 35)
print("Thank you for using this program!")
print("=" * 35)