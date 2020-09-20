table= {}
stepsSizes = [1]

def rec(n):
    if n in [0]:
        return 1
    if(n < 0):
        return 0
    if(n in table.keys()):
    	return table[n]
    
    if(n >= 1):
    	result = 0
    	for step in stepsSizes:
    		result += rec(n-step)
    	#result = rec(n-1) + rec(n-2) + rec(n-3)
    	table[n] = result
    	

    #print(str(n) + "   " + str(result))
    return result

n = 30

print(rec(n))

print(table)
