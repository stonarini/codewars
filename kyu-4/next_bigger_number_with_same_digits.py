# https://www.codewars.com/kata/55983863da40caa2c900004e
# Next Bigger Number With the Same Digits

# First Implementation 02/10/2021
def next_bigger(n):
        if len(str(n)) == 1: return -1
        originalNum=n
        nLenght=len(str(n))
        num = [i for i in list(str(n))]
        foundBigger=False
        
        if num[-1] > num[-2]:
            num[-1], num[-2] = num[-2], num[-1]
            return int("".join(num))
        
        for i in range(nLenght-2, 0, -1):
            if num[i] > num[i-1]:
                foundBigger=True
                subsetNum=num[i-1:]
                num=num[:i-1]
                break
                    
        if not foundBigger:
            return -1
        
        solvedNum=[]
        for i in range(len(subsetNum)):
            smallest=False
            if i == 0:
                for j in range(1, len(subsetNum)):
                    if smallest:
                        if subsetNum[j] > subsetNum[0]:
                            if subsetNum[j] < subsetNum[smallest]:
                                smallest=j
                    else:
                        if subsetNum[j] > subsetNum[0]:
                            smallest=j
            else:
                for j in range(1, len(subsetNum)):
                    if smallest:
                        if subsetNum[j] < subsetNum[smallest]:
                            smallest=j
                    else: 
                        if subsetNum[j] < subsetNum[0]:
                            smallest=j
            if smallest:
                subsetNum[0], subsetNum[smallest] = subsetNum[smallest], subsetNum[0]
            
            solvedNum.append(subsetNum.pop(0))
            
        return int("".join(num) + "".join(solvedNum))