def brute_force(block_weight, weight_cost):
    if block_weight <= 0:
        return 0, []

    max_profit = 0
    pieces_list = []
    
    for i in range(block_weight):
        cost = 0
        if i+1 in weight_cost.keys():
            cost = weight_cost[i+1]
        profit, pieces = brute_force(block_weight - (i+1), weight_cost)
        max_profit = max(max_profit, cost + profit)
        if max_profit == cost + profit:
            pieces_list = pieces + [i+1]

    return max_profit, pieces_list

def dynamic(block_weight, weight_cost):
    max_profit = [0]*(block_weight+1)
    #max_profit[0] = 0
    pieces_list = [[]]*(block_weight+1)
    for i in range(1, block_weight+1):
        max_val = 0
        #print("i =", i)
        pieces = []
        for j in range(i):
            cost = 0

            if j+1 in weight_cost.keys():
                cost = weight_cost[j+1]

            #print("\tj =", j)
            #print("\tmax_val =", max_val, "\tweight_cost[", j+1, "] + max_profit[", i - j - 1, "] = ", cost, "+", max_profit[i - j - 1],
             #     "=", cost + max_profit[i - j - 1])
            max_val = max(max_val, cost + max_profit[i-j-1])
            if max_val == cost + max_profit[i-j-1]:
                pieces = pieces_list[i-j-1] + [j+1]
        max_profit[i] = max_val
        pieces_list[i] = pieces
        #print()

    return max_profit[block_weight], pieces_list[block_weight]

def greedy(block_weight, weight_cost):
    max_profit = 0
    pieces_list = []

    while block_weight >= min(weight_cost.keys()):
        weight, cost = max_weight_cost(block_weight, weight_cost)
        max_profit += cost
        block_weight -= weight
        pieces_list.append(weight)

    if block_weight < min(weight_cost.keys()) and block_weight > 0:
        pieces_list.append(block_weight)

    return max_profit, pieces_list

def max_weight_cost(block_weight, weight_cost):
    max_weight = 0
    max_cost = 0
    for w in weight_cost.keys():
        if weight_cost[w] > max_cost and w <= block_weight:
            max_cost = weight_cost[w]
            max_weight = w

    return max_weight, max_cost

