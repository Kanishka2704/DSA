#sort out all odd numbers using stack and display largest odd number in the stack
stack = []
input_list = input("Enter a number:")
numbers =[int(num) for num in input_list.split()]
stack.extend(numbers)
odd_number = [num for num in stack   if num%2 !=0]
if odd_number:
    largest_odd_number = odd_numbers[0] 
    for num in odd_numbers:
        if num > largest_odd_number:
            largest_odd_number = num
    print(f"Largest odd number is {largest_odd_number}")
else:
    print("There are no odd numbers in the stack.")
