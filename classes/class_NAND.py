#! /usr/bin/env python3

class NAND_gate:
    """a class that simulates the logic of a NAND gate"""
    def __init__(self, x1: int, x2: int, x3: int):
        self.input1 = x1
        self.input2 = x2
        self.input3 = x3
        self.output = self.calculate_output()

    def get_input(self):
        return (self.input1, self.input2, self.input3)

    def get_output(self):
        return self.output

    def set_input(self, y1: int, y2: int = None, y3: int = None):
        """change 1 to 3 inputs, from input1 to input3"""
        # replace only input1
        if y2 == None:
            self.input1 = y1
        # replace input1 and input2
        elif y3 == None:
            self.input1 = y1
            self.input2 = y2
        # replace all input
        else:
            self.input1 = y1
            self.input2 = y2
            self.input3 = y3
        # update the state of the gate according to the new inputs
        self.output = self.calculate_output()

    def calculate_output(self):
            if self.input1 == self.input2 == self.input3 == 1:
                return 0
            else:
                return 1

gate1 = NAND_gate(0, 0, 1)
print(gate1.get_output())
gate1.set_input(1)
print(gate1.get_input())
print(gate1.get_output())