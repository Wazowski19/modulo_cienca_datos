#Lambda functions

def sum (n1, n2):
    return n1 + n2

sum_lambda = lambda n1, n2: n1 + n2

print(sum(1,2))
print(sum_lambda(1,2 ))

#Lambda in highorder function

def outsideFunction(name):
    return lambda n1, n2: f'{name} su salario es {n1 + n2}'

insideFunctionMiguel = outsideFunction("Miguel")
insideFunctionPau = outsideFunction("Pau")

print(insideFunctionMiguel(1232,245))
print(insideFunctionPau(122,2000))