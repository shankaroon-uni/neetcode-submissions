class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            length = len(i)
            encoded_string += str(length) + "#" + i

        return encoded_string

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_strs = []
        pointer = 0
        i = 0
        length = 0
        while i < len(s):
            if s[i] == "#":
                print(pointer)
                print(i)
                length = int(s[pointer:i])
                pointer = (length + 1 + i)
                decoded_strs.append(s[(i+1):(i+1+length)])
                i = pointer
            i += 1
            print(pointer)
            print(i)
        return decoded_strs