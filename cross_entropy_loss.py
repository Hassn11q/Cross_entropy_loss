import math
input_data = [(0.26 , 1) , (0.20 , 0) , (0.48,1) , (0.30,0)]
def cross_entropy(input_data):
    loss = 0
    n = len(input_data)
    for cost in input_data:
        weight_sum = cost[0]
        y = cost[1]
        loss+=-(y*math.log10(weight_sum)+(1-y)*math.log10(1-weight_sum))
    return loss/n
print(cross_entropy(input_data))
