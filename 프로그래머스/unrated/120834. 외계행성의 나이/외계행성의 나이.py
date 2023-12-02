def solution(age):
    alphabet = [chr(s) for s in range(97,123)]
    return ''.join([alphabet[int(s)] for s in str(age)])