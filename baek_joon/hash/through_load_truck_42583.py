import sys
input = sys.stdin.readline

#bridge_length = 2
#weight = 10
#truck_weights = [7,4,5,6]

bridge_length = 100
weight = 100
truck_weights = [10]

def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    print(f'bridge = {bridge}')
    
    while bridge:
        
        answer += 1
        bridge.pop(0)

        print(f'pop after bridge = {bridge}, answer = {answer}, truck_weights ={truck_weights}')
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
                 
         
    return answer

print(solution(bridge_length, weight, truck_weights))
