class Numberfy:
    """
    This class is 
    """
    
    def __init__(self):
        pass 
    # ===============================================


    def ascii_encode(self, file_in="data_encoded.txt", file_dest="data_encoded.txt"):
        # reading
        with open(file_in, "r") as f:
            lines = f.readlines()
            content = []
            for l in lines:
                if l != "\n":
                    l = l.strip("\n")
                    content.append(l)
                    # print(len(l))


        # writing
        with open(file_dest, "w") as nums:
            ascii_list = []
            for string in content:
                for char in string:
                    a = ord(char)
                    ascii_list.append(a)
                    nums.write(str(a))
                    nums.write("\n")

        print("<process complete>")
        # print(ascii_list)
    # ===============================================

    def ascii_decode(self, file_in="ascii.txt", file_dest="d_encoded.txt"):
        with open(file_in, "r") as asc:
            plain = []
            lines = asc.readlines()

            # writing to a new file
            f = open(file_dest, "w")
            for num in lines:
                num = num.strip("\n")
                a = ord("]")
                if num == str(a):
                    char = chr(int(num))
                    print(char, end="\n")
                    f.write(char)
                    f.write("\n")
                
                else:
                    # end = num.index("]")
                    # print(end)
                    # new = num[0:end]
                    # print(new)

                    char = chr(int(num))
                    print(char, end="")
                    f.write(char)
                    # plain.append(char)
    # ===============================================

    def ascii_string(self, msg="testing", mod=0):
        ascii_list = []

        for char in msg:
            ascii = ord(char) + mod
            ascii_list.append(ascii)

        return ascii_list 
    # ===============================================

# ***************************************************

obj = Numberfy()
print(obj.ascii_string())
# ***************************************************