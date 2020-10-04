
class PrefixCodeTree():
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None


    def insert(self, codeword, symbol):
        tmp = self
        # Insert nodes into the tree, 0 is left node, 1 is right node
        i=0
        while i < len(codeword):
            if i == len(codeword) -1:
                if codeword[i] == 0:
                    tmp.left = PrefixCodeTree(symbol)
                elif codeword[i] == 1:
                    tmp.right = PrefixCodeTree(symbol)
            else:
                if codeword[i] == 0:
                    if tmp.left is None:
                        tmp.left = PrefixCodeTree("")
                    tmp = tmp.left
                elif codeword[i] == 1:
                    if tmp.right is None:
                        tmp.right = PrefixCodeTree("")
                    tmp = tmp.right

            i+=1

    def decode(self, encodeData, datalen):
        # Convert byte to bitstring 
        bitstr = "".join(f"{byte:0>8b}" for byte in encodeData)[:datalen]
        m = ''

        tmp = self

        # traverse the tree 
        for bit in bitstr:
            if int(bit) == 0:
                tmp = tmp.left
            elif int(bit) == 1:
                tmp = tmp.right

            if tmp.data != "":
                m += tmp.data
                tmp = self

        return m

                        