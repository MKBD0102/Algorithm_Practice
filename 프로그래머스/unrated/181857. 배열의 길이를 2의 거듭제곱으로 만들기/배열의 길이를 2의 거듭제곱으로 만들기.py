def solution(arr):
    n = len(arr)
    if n&(n-1) == 0:
        return arr
    else:
        r = 2**len(bin(n)[2:]) - n
        arr += [0 for i in range(r)]
        return arr
    
'''
# len(bin(n)[2:]) 말고 한 번에 2진수 길이 찾는 함수 bit_length() (비트 -> 이진법)
# x.bit_length():  2**(k-1) <= abs(x) < 2**k 를 만족하는 유일한 양의 정수 k

def solution(arr):
    n = len(arr)
    if n == 2 ** (n-1).bit_length:
        return arr
    else:
        r = 2 ** (n-1).bit_length - n
        # 리스트 확장 함수 extend()
        arr.extend([0]*r)
        return arr
'''