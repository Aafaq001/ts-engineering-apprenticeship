x = 10

def test():
    x = 20
    print(x)

test()
print(x)

risk_score = 0

def calculate():
    global risk_score
    risk_score = 50
    return risk_score

print(calculate())

