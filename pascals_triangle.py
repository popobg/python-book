#! /usr/bin/env python3

'''A pascal's triangle in algebra is a triangle arrangement of numbers. It is constructed by first placing a 1 at the top, then adding together the two numbers side by side (imagining that the edge are adding to 0).
Example with 3 rows: 1
                    1 1
                   1 2 1'''

def compute_level(list):
    copied_list = list.copy()
    for i in range(1, len(copied_list) -1):
        copied_list[i] = list[i] + list[i-1]
    return copied_list

def compute_triangle(n):
    list_triangle = [[1]]
    for i in range(0, n - 1):
        values = list_triangle[i]
        new_values = []
        for j in values:
            new_values.append(j)
        new_values.append(1)
        new_level = compute_level(new_values)
        list_triangle.append(new_level)
    return list_triangle

def convert_to_string(list):
    for i in range(0, len(list)):
        list[i] = str(list[i])
    string = " ".join(list)
    return string

def print_triangle(list_of_string):
    for i in list_of_string:
        print(i.center(len(list_of_string[-1])))

def pascals_triangle(n):
    triangle_lists = compute_triangle(n)
    triangle_strings = []
    for i in triangle_lists:
        string = convert_to_string(i)
        triangle_strings.append(string)
    print_triangle(triangle_strings)

pascals_triangle(5)
pascals_triangle(7)
pascals_triangle(12)