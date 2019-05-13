class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # print(bin(n))
        # s = bin(n)[-1:1:-1]
        # print(s)
        # print(s.ljust(32, "0"))
        return int(bin(n)[-1:1:-1].ljust(32, "0"), 2)