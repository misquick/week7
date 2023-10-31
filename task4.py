numbers = []
print("Typing 'done' will exit the program")
while True:
    user_input = input("Please enter an integer: ")
    
    if user_input.lower() == 'done':
        break

    try:
        num = int(user_input)
        numbers.append(num)
        avg = sum(numbers) / len(numbers)
        print(f"[{', '.join(map(str, numbers))}] , average = {avg:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("--- Bye !! ---")
