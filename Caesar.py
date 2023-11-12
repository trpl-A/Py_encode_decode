class Caesar:
    """
    This class if used to read and encrypt, or decrypt the data from a text file
    It uses the Caesar cypher
    """

    def __init__(self):
        self.alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alpha_l = "abcdefghijklmnopqrstuvwxyz"
 

    def encrypt(self, filename=str, key=str) -> None:
        file = open(filename, "r")
        lines = file.readlines()
        # print(lines)

        alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha_l = "abcdefghijklmnopqrstuvwxyz"

        # key 
        k = ""
        if key in alpha_u:
            k = alpha_u.index(key)
            print(k)
        
        elif key in alpha_l:
            k = alpha_l.index(key)


        # encryption
        num_format = []
        for line in lines:
            # replacing \n 
            line.replace("\n", "*")

            # converting letters to their index in the alphabet
            for char in line:
                if char in alpha_l:
                    char = (alpha_l.index(char) + int(k)) % 26
                    num_format.append(char)
                    # print(char, end="")

                elif char in alpha_u:
                    char = (alpha_u.index(char) + int(k)) % 26
                    num_format.append(char)
                    # print(char, end="")

                else:
                    num_format.append(char)
                    # print(char)

        # print(num_format)


        # converting (indexes) numbers to letters
        msg = ""
        nums = range(0, 26)
        for n in num_format:
            if n not in nums:
                letter = str(n)
                # print(letter, end="")

            elif n == "*":
                print()
                
            else:
                letter = alpha_l[n]
                # print(letter, end="")


            msg += letter

        # writing to file
        # with open("eee.txt", "w") as w:
        #     w.write(msg)

        return msg 
        print("\n<Encryption complete>")
    # =============================================

    def encrypt_write(self, input_file="test.txt", dest_file="new_encoded.txt", key="m") -> None:
        encrypting_data = self.encrypt(input_file, key)
        print(encrypting_data)

        # writing to text file
        # import os 
        # directory = os.getcwd()
        # full = os.path.join(directory, dest_file)
        # print(directory)
        # print(full)
        # file = open(f"{full}", "w")

        file = open(f"files_caesar/{dest_file}", "w")
        file.write(f"\n{encrypting_data}\n")
    # =============================================

    # IF THE KEY IS KNOWN
    def decrypt(self, input_file="test.txt", dest_file="data1.txt", key=int) -> None:
        # reading text file
        file = open(f"{input_file}", "r")
        l = file.readlines()
        # print(len(l))


        # removing \n 
        s = []
        for i in l:
            # i = i[0:-2]
            i = i.replace("\n", "")

            if i == "":
                pass 

            else:
                s.append(i)

        # print(s)
        # print(len(s))


        # writing potential message to a text file
        p_msg = open(f"files_plain/{dest_file}", "w")
        # p_msg = open(f"{dest_file}", "w")

        # key = "m"
        # key = 12 

        # decoding
        alpha = "abcdefghijklmnopqrstuvwxyz"
        # alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for m in s:
            for n in m:

                if n not in alpha:
                    # print(n, end="")
                    p_msg.write(n)

                else:
                    lttr = (alpha.index(n) + (26 - key)) % 26
                    a = alpha[lttr]
                    # print(a, end="")
                    p_msg.write(a)

            # print()
            p_msg.write("\n")

        print("\n<decoding complete>")
    # =============================================
 

    def encrypt_str(self, msg_str="testing", key="d") -> str:
        # key 
        k = ""
        if key in self.alpha_u:
            k = self.alpha_u.index(key)
            print(k)
        
        elif key in self.alpha_l:
            k = self.alpha_l.index(key)


        num_format = []
        # converting letters to their index in the alphabet
        for char in msg_str:
            if char in self.alpha_l:
                char = (self.alpha_l.index(char) + int(k)) % 26
                num_format.append(char)
                # print(char, end="")

            elif char in self.alpha_u:
                char = (self.alpha_u.index(char) + int(k)) % 26
                num_format.append(char)
                # print(char, end="")

            else:
                num_format.append(char)
                # print(char)

        # converting (indexes) numbers to letters
        msg = ""
        nums = range(0, 26)
        for n in num_format:
            if n not in nums: letter = str(n)
            elif n == "*":  print()
            else: letter = self.alpha_l[n]
            msg += letter

        return msg 
    # =============================================

    def caesar_ascii(self, msg="testing", key="e") -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        ascii_str = ""

        for char in msg:
            modifier = alpha.index(key)
            # convert to number
            ascii = ord(char) + modifier

            # convert to char
            ascii = chr(ascii)

            # updating
            ascii_str += ascii 

        return ascii_str
    # =============================================
# *************************************************

obj = Caesar()
# print(obj.__doc__)
# print(help(obj))

# obj.encrypt_write("_hu.txt")
obj.decrypt("files_caesar/new_encoded.txt",key=12)
# *************************************************