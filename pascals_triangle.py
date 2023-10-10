#! /usr/bin/env python3

def triangle_algorithm(list):
    copied_list = list.copy()
    for i in range(1, len(copied_list) -1):
        copied_list[i] = list[i] + list[i-1]
    return copied_list

def compute_triangle(n):
    list_values = [[1]]
    for i in range(0, n - 1):
        values = list_values[i]
        new_values = []
        for j in values:
            new_values.append(j)
        new_values.append(1)
        new_list = triangle_algorithm(new_values)
        list_values.append(new_list)
    return list_values

def convert_to_string(list):
    for i in range(0, len(list)):
        list[i] = str(list[i])
    string = " ".join(list)
    return string

def print_triangle(list_of_string):
    for i in list_of_string:
        print(i.center(len(list_of_string[-1])))

def pascals_triangle(n):
    list_of_list = compute_triangle(n)
    list_of_string = []
    for i in list_of_list:
        string = convert_to_string(i)
        list_of_string.append(string)
    print_triangle(list_of_string)

pascals_triangle(5)
pascals_triangle(7)
pascals_triangle(12)