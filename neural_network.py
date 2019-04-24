import random

def activation_function(w, x):
	y = 0
	for i in range(len(w)):
	    y += w[i] * x[i]
    
	if y > 0.5:
	    return 1
	else:
	    return 0

def train_newtork(training_set, weights):
    
    error_aux = 1
    not_infinity = 0
    
    while(error_aux > 0):
        error = 0
        for training in training_set:
        	y  = activation_function(training[:-1], weights)
        	aux = training[-1] - y
        	error += abs(aux)
        	for i in range(len(weights)):
        		weights[i] += aux * training[i]
        
        error_aux = error
        not_infinity += 1
        
        if not_infinity > 1000:
            break
    return error
        
if __name__ == "__main__":
    
    training_set = []
    test_set = []
    
    d = int(input())
    m = int(input())
    n = int(input())
    
    for i in range(m):
        training_set.append(list(map(float,input().replace(" ", "").split(","))))
        
    for i in range(n):
        test_set.append(list(map(float,input().replace(" ", "").split(","))))
    
    weights = [] 
    for i in range(d):
    	weights.append(random.random())
    
    error = train_newtork(training_set, weights)
    
    if error == 0:
        for test in test_set:
            print(activation_function(test, weights))
    else:
        print("no solution found")
        