def func1(require = [], go = False):
    if go:
        require.append(20)
        return require
        
    add = func1(go = True)
    require += add
    #print (require)
    return require

add = 10

def therealreal(update):
    def modify(require = []):
        #print(update())
        require += update()
        
        global add
        require.append(add)
        add += 10
        return require
    
    return modify
    
use = therealreal(func1)
upto = 213

calc = use()
#print(calc)
for _ in range(1, upto+1):
    calc = use(calc)

#print(calc)
print(sum(calc))
