#! /usr/bin/env python3

# import popo_tools

# def quarter(prompt):
#    return int(popo_tools.input_float(f"{prompt} ?"))

def histo(quarter, Q):
    print(f"{Q}: ", end = '')
    for i in range(0, int(quarter/20000)):
        print("#", end = '')
    print("      ", quarter)

# quarter1 = quarter("Q1")
# quarter2 = quarter("Q2")
# quarter3 = quarter("Q3")
# quarter4 = quarter("Q4")

print("earnings of WidgetCorp in each quarter of 2016")
print("==============================")

quarter1 = 900000
quarter2 = 874000
quarter3 = 200000
quarter4 = 439833

Q1 = "Q1"
Q2 = "Q2"
Q3 = "Q3"
Q4 = "Q4"

histo(quarter1, Q1)
histo(quarter2, Q2)
histo(quarter3, Q3)
histo(quarter4, Q4)