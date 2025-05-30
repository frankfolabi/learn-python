responses = {}
# Set a flag to indecate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain would you like to climb someday? ")

    # Store the response in a dectionary.
    responses[name] = response # Setting name as key and response as value.

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.itmes():
    print(f"{name} would like to climb {response}.")
