

class Number_sys:
    """
    This class 

    Methods
    - _bin
        > converts a string to binary numbers

    - _hex
        > 

    - _oct  
        > 
        
    """
    
    
    def __init__(self):
        pass 
    # ==================================

    
    def _bin(self, plain=str):
        ascii_list = []
        for char in plain:
            ascii_value = ord(char)
            ascii_list.append(ascii_value)

        bin_list = []
        for num in ascii_list:
            bin_value = bin(num)
            bin_list.append(bin_value)

        for b in bin_list:
            print(b, end=" ")
        print()
    # end of function =============================


    def _hex(self, plain=str):
        ascii_list = list()
        for char in plain:
            ascii_value = ord(char)
            ascii_list.append(ascii_value)

        hex_list = list()
        for num in ascii_list:
            hex_value = hex(num)
            hex_list.append(hex_value)

        for h in hex_list:
            print(h)
        print()
    # end of function =============================

    
    def _oct(self, plain=str):
        ascii_list = list()
        for char in plain:
            ascii_value = ord(char)
            ascii_list.append(ascii_value)

        oct_list = list()
        for num in ascii_list:
            oct_value = oct(num)
            oct_list.append(oct_value)

        for o in oct_list:
            print(o)
        print()
    # end of function =============================

# *************************************************
obj = Number_sys()

obj._bin("asas")

# *************************************************