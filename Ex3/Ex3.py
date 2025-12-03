print("Provide maximum number of items to be shipped : ")

#Variables initialization
check_progr = True
pack_number = 0
total_weight = 0
lowest_record = 0
it_record = 0
tot_un_cap = 0

try:
    it_times = int(input()) # Input to decide number of iterations
    print(f"Total number of items to be sent: {it_times}")

    current_weight = 0
    print(f"Add items to package number {pack_number + 1}")

    for i in range(it_times):
        if not check_progr: # Boolean if program was stopped during iterations
            break
        else:
            while True:
                try:
                    print("Put weight of package: ")
                    input_weight = float(input())
                    if input_weight == 0:
                        print("Program halted")
                        check_progr = False # Change boolean value to stop program
                        break
                    elif input_weight < 1 or input_weight > 10:
                        print("Item weight must be between 1 and 10")
                        continue
                    elif current_weight + input_weight <= 20:
                        current_weight = current_weight + input_weight
                        print(f"Current weight of package: {current_weight}")
                        break
                    else:
                        print(f"Package limit reached, total package weight is {current_weight}") # Block to increase counters and record iteration with most unused capacity
                        pack_number += 1
                        total_weight = total_weight + current_weight
                        unused_weight = 20 - current_weight
                        tot_un_cap += unused_weight
                        if unused_weight >= lowest_record:
                            lowest_record = unused_weight
                            it_record = pack_number
                        current_weight = input_weight
                        print(f"Add items to package number {pack_number + 1}")
                        print(f"Current weight of package: {current_weight}")
                        break

                except ValueError: # Exception to handle inputs when a float number is not provided
                    print("Invalid weight, weight must be a float number")
                    continue

    if current_weight > 0 and check_progr: #Block to handle last package if any item inside
        print(f"Final package weight is {current_weight}")
        pack_number += 1
        total_weight = total_weight + current_weight
        unused_weight = 20 - current_weight
        tot_un_cap += unused_weight

        if unused_weight > lowest_record:
            lowest_record = unused_weight
            it_record = pack_number

    print("\nPackage summary: \n\n"
          f"Total weight: {total_weight}\n"
          f"Total packages: {pack_number}\n"
          f"Total unused capacity: {tot_un_cap}\n"
          f"The package number {it_record} has the most unused capacity, unused capacity is {lowest_record} units\n")
except ValueError: # Exception to handle inputs that are not integers
    print("Not valid entry, retry with a valid number")