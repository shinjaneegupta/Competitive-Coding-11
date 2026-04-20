# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : e use a stack to store digits and keep removing the top if the current digit is smaller and we still have k left.
# We remove remaining digits from the end if k is still not zero after the loop.
# We build the result by skipping leading zeros and return "0" if everything got removed.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for c in num:
            while st and c < st[-1] and k > 0:
                st.pop()
                k -= 1
            st.append(c)

        while k > 0:
            st.pop()
            k -= 1

        sb = []
        firstZero = True
        for c in st:
            if firstZero and c == '0':
                continue
            firstZero = False
            sb.append(c)

        if not sb:
            return "0"
        return "".join(sb)
