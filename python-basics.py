# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
a_string = "I'm a string"
a_number = 6
a_list = [1, 2, 3]
a_boolean = True
print(a_string, a_number, a_list, a_boolean)
# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
three_first_letters = a_string[0:3]
print(three_first_letters)
# Exercise 3: Use an index to grab the first element from your list.
first_element = a_list[0]
print(first_element)
# Exercise 4: Create a new number variable that adds 10 to your original number.
new_number = a_number + 10
print(new_number)
# Exercise 5: Use an index to get the last element in your list.
last_element = a_list[-1]
print(last_element)
# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
string_to_list = names.split(',')
print(string_to_list)
# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
first_word = a_string[0:1].upper()
new_string = first_word + a_string[1:]
print(new_string)
# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f"my number variable is: {a_number}")
# Exercise 9: Print “hello world”.
print("hello world")


