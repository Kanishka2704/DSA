#reverse a string using stack
string_in_list = []
user_string = input("Enter a string:")
string_in_list.extend(user_string)
reverse_string = ""
while string_in_list:
  reverse_string += string_in_list.pop()
print(reverse_string)
