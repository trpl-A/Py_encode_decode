class Asterisk:
    """
    This class is 
    """
    
    def __init__(self):
        self.binary = []
        self.asterisk_code = []
        
    # =================================================
        
    # ENCODE
    def plain_to_bin(self, word="plain to binary") -> list:
        # convert to ascii value
        code = []
        for char in list(word):
            a = ord(char)
            # print(a)
            
            code.append(a)
        print()

        # convert to binary
        for c in code:
            b = bin(c)
            b = b.replace("0b", "")

            # add to the list
            self.binary.append(b)  

        return self.binary 
    # =================================================

    def bin_to_asterisk(self, entry_name="title") -> None:
        # map = self.binary
        map = self.plain_to_bin()

        for point in map:
            for switch in point:
                if switch == '1':
                    print("*", end="")
                    self.asterisk_code.append("*")

                elif switch == '0':
                    print(" ", end="")
                    self.asterisk_code.append(" ")

            self.asterisk_code.append("\n")       
            print()
        # print(self.asterisk_code)


        # writing to text file
        import datetime
        a = datetime.datetime.now()
        name = (a.strftime("%Y-%m-%d %H-%M-%S")) + entry_name 
        
        f = open(f"{name}.txt", "w")
        for p in self.asterisk_code:
            f.write(p)
    # =================================================


    # DECODE
    def asterisk_to_bin(self, filename="texting") -> list:
        f = open(f'{filename}.txt', 'r')
        g = f.readlines()


        # removing new line chars      
        h = []
        for line in g:
            l = line.strip("\n")
            h.append(l)

        # converting to bin
        bin = []
        for i in h:
            for point in i:
                if point == "*":
                    # print(1, end="")
                    bin.append(1)

                elif point == " ":
                    # print(0, end="")
                    bin.append(0)
            # bin.append("\n")


        # writing to text file
        result = open(f"{filename}_result.txt", "w")

        return bin 
    # =================================================

    def bin_to_plain(self, filename="file") -> None:
        file = self.asterisk_to_bin(filename)

        # writing to new file
        new = open(f"{filename}_decode.txt", "w")
        
        for line in file:
            line = str(line)
            ln = line.replace("\n", "")

            le = chr(int(ln))
            # print(le, end="")
            
            # writing to file
            new.write(le)
        
        print("\n<Conversion complete>")
    # =================================================
# *****************************************************

obj = Asterisk()

# obj.bin_to_asterisk()
# print(obj.asterisk_to_bin("2023-11-12 01-23-53title"))
# obj.bin_to_plain("2023-11-12 01-23-53title")

# ****************************************************