import numpy as np

w = {
    'AND': np.array([0.5, 0.5]),
    'NAND': np.array([-0.5, -0.5]),
    'OR': np.array([0.5, 0.5]),
}

b = {
    'AND': -0.7,
    'NAND': 0.7,
    'OR': -0.2,
}


def AND(x1, x2):
    x = np.array([x1, x2])
    return CalcPerception(x, w['AND'], b['AND'])


def NAND(x1, x2):
    x = np.array([x1, x2])
    return CalcPerception(x, w['NAND'], b['NAND'])


def OR(x1, x2):
    x = np.array([x1, x2])
    return CalcPerception(x, w['OR'], b['OR'])


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)


def CalcPerception(x, weight, bias):
    tmp = np.sum(weight*x) + bias
    return 0 if tmp <= 0 else 1


print("AND")
print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

print("NAND")
print(NAND(0, 0))
print(NAND(1, 0))
print(NAND(0, 1))
print(NAND(1, 1))

print("OR")
print(OR(0, 0))
print(OR(1, 0))
print(OR(0, 1))
print(OR(1, 1))

print("XOR")
print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))
