a = ["82113243", -90]

def allExpressions(data, target):
    operators = ['+', '-', '*', '']
    expressions = []
    for i in range(len(data)):
        digit = data[i]
        if i == 0:
            expressions.append(digit)
            # if data[i] != "0":
            #     expressions.append("-" + digit)
        else:
            exp = []
            for j in operators:
                exp.extend([x + j + digit for x in expressions])
            expressions = exp
    exp = []
    for i in expressions:
        try:
            t = eval(i)
            if t == target:
                exp.append(i)
        except SyntaxError:
            # print(i)
            pass
    return exp


print(",".join(allExpressions(a[0], a[1])))
