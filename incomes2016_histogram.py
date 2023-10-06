#! /usr/bin/env python3

def make_bar(number_char):
    """return n pounds in a row"""
    return "#" * int(number_char / 20000)

# construct the string to print it at once
def make_string(i, profit):
    return f"Q{i+1}: {make_bar(profit)}     {profit}"

# incomes_histo takes an iterable object and a non_iterable object as arguments
def incomes_histo(profit_year, year):
    """construct an histogram with the profits per quarter of a given year"""
    print(f"Earnings of WidgetCorp in each quarter of {year}")
    print("==============================")
    for i in range(0,4):
        print(make_string(i, profit_year[i]))

profit_2016 = [190000, 340000, 873000, 439833]

incomes_histo(profit_2016, 2016)