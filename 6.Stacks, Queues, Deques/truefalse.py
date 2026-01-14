def check(data):
    if len(data) <= 0:
        return True
    if data[0] != data[-1]:
        return False
    
    return check(data[1:-1])

print(check("racecar"))
print(check("12345"))

original = [1,2,3]
y = original[:]
y[1] = 9
print(original)

original = [1,2,3]
y = original
y[1] = 9
print(original)