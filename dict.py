s = "mississippi"
d = {}
for i in s:
    c = s.count(i)
    if i not in d:
        d[i]=c
print(d)

# max of three numbers
def max_of_two(x, y):
    if x>y:
        return x 
    return y 
def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))
print(max_of_three(3, 6, -5))

n = input("Enter n: ")

