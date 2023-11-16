def regressiva(i): #1
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i-1)
    
def fat(x): #2
    if x == 1:
        return
    else:
        return x * fat(x-1)


print(fat(3))
print(regressiva(10))