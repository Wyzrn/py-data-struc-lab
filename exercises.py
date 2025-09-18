# Exercise 1: List and Indexing
def manage_students():
    students = ['Alice', 'Bob', 'Charlie']
    first_student = students[1]  # Second student
    last_student = students[-1]  # Last student
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
def combine_foods():
    foods = ('pizza', 'sushi', 'tacos')  # Same length as students list (3)
    meal = ''
    for food in foods:
        meal += food + ' '
    return meal

# Call the function and print the result
print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
def slice_foods():
    foods = ('pizza', 'sushi', 'tacos')
    last_two_foods = foods[-2:]  # Slice last two items
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())