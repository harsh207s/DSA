class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def dfs(index, path, value, last):
            # index: current digit position
            # path: expression string
            # value: current evaluated result
            # last: last multiplied segment to adjust multiplication precedence
            
            if index == len(num):
                if value == target:
                    res.append(path)
                return
            
            for i in range(index, len(num)):
                # avoid leading zeros
                if i != index and num[index] == '0':
                    break
                
                cur_str = num[index:i+1]
                cur = int(cur_str)
                
                # First number in expression (no operator before it)
                if index == 0:
                    dfs(i + 1, cur_str, cur, cur)
                else:
                    # Addition
                    dfs(i + 1, path + "+" + cur_str, value + cur, cur)
                    # Subtraction
                    dfs(i + 1, path + "-" + cur_str, value - cur, -cur)
                    # Multiplication
                    dfs(i + 1, path + "*" + cur_str, value - last + last * cur, last * cur)
        
        dfs(0, "", 0, 0)
        return res
