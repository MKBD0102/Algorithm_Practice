str = input()
print("".join([s.upper() if s.islower() else s.lower() for s in str]))