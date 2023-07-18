s = ["h","e","l","l","o"]
for i in s: 
    x = s.pop()
    s = s.insert(0,x)
    s.pop()
    print("test")
    print('x')
    
print("s", s)