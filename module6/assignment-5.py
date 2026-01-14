full_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
only_even_numbers = []


def filter_even_numbers(only_even_numbers):
    only_even_numbers = [i for i in full_list if i % 2 == 0]
    return (only_even_numbers)

print(f"Original list: {full_list}")
print(f"List with even numbers only: {filter_even_numbers(only_even_numbers)}")