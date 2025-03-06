from itertools import product
import sys

def open_process_file():
    global calculations 
    calculations = {}
    for line in sys.stdin:
        key,  value = line.strip().split(": ")
        key = int(key)
        value = list(map(int, value.split()))
        calculations.update({key: value})
    return calculations

def sum_valid(dic):
    symbols = ['+', '*']
    valid_sum = 0
    for key, value in dic.items():
        combinations = list(product(symbols, repeat = len(value)-1)) 
        for operator in combinations:
            temp = ''.join(str(value[i]) + operator[i] for i in range(len(operator))) + str(value[-1]) 
            if eval(temp) == key:
                valid_sum+=key
                break
    return valid_sum
    
if __name__ == "__main__":
    calculations = open_process_file()
    print(sum_valid(calculations)) 
