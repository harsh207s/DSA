class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # Try every possible split for first and second number
        for i in range(1, n):              # first number ends at i-1
            for j in range(i+1, n):        # second number ends at j-1
                
                # extract first and second numbers
                a, b = num[:i], num[i:j]
                
                # Skip leading zero cases
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue
                
                # Now generate the sequence
                prev1, prev2 = int(a), int(b)
                k = j
                while k < n:
                    nxt = prev1 + prev2
                    nxt_str = str(nxt)
                    
                    # if next required number doesn't match
                    if not num.startswith(nxt_str, k):
                        break
                    
                    # move forward
                    k += len(nxt_str)
                    prev1, prev2 = prev2, nxt
                
                # if reached end successfully
                if k == n:
                    return True
        
        return False
