#Variables initialization
check_progr = True
pack_number = 0
total_weight = 0
lowest_record = 0
it_record = 0

try:
    it_times = int(input("Provide maximum number of items to be shipped: ")) # Input to decide number of iterations
    print(f"Total number of packages to be sent: {it_times} \n")
    for package in range(it_times):
        if not check_progr: # Boolean if program was stopped during iterations
            break
        else:
            print(f"Add items to package number {package+1}\n")
            current_weight = 0
            while current_weight <= 20:
                try:
                    input_weight = float(input(f"Put the weight of item for package number {package+1}: "))
                    if input_weight == 0:
                        print("Program halted")
                        check_progr = False # Change boolean value to stop program
                        break
                    elif input_weight < 1 or input_weight > 10:
                        print("Item weight must be between 1 and 10\n")
                    elif current_weight + input_weight <= 20:
                        current_weight = current_weight + input_weight
                    else:
                        print(f"Limit reached, package sent, total package weight is {current_weight}Kg\n") # Block to increase counters and record iteration with most unused capacity
                        pack_number += 1
                        total_weight = total_weight + current_weight
                        unused_weight = 20 - current_weight
                        curr_lowest = unused_weight
                        if curr_lowest >= lowest_record:
                            lowest_record = curr_lowest
                            it_record = package + 1
                        break
                    print(f"Current weight of package number {package+1}: {current_weight}\n")

                except ValueError: # Exception to handle inputs when a float number is not provided
                    print("Invalid weight, weight must be a float number\n")
                    continue
    print("\nPackage summary: \n\n"
          f"Total weight: {total_weight}\n"
          f"Total packages: {pack_number}\n"
          f"The package number {it_record} had the most unused capacity, unused capacity was {lowest_record}Kg\n")
except ValueError: # Exception to handle inputs that are not integers
    print("Not valid entry, retry with a valid number")