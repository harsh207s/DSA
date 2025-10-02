
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        # count1 -> how many times s1 has been traversed
        # count2 -> how many times s2 has been matched
        # index -> current position in s2
        index = 0
        count1 = count2 = 0
        
        # record[index_in_s2] = (count1, count2)
        record = {}
        
        while count1 < n1:
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        count2 += 1
            count1 += 1
            
            # cycle detection
            if index in record:
                prev_count1, prev_count2 = record[index]
                
                # length of the cycle
                cycle_len1 = count1 - prev_count1
                cycle_len2 = count2 - prev_count2
                
                # how many cycles fit in the remaining s1
                remaining = n1 - count1
                cycles = remaining // cycle_len1
                
                count1 += cycles * cycle_len1
                count2 += cycles * cycle_len2
            else:
                record[index] = (count1, count2)
        
        return count2 // n2

