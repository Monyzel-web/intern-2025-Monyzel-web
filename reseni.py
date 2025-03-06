from itertools import product
import sys

#read the file, extract the data, process it into dictionary
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
    valid_temp = []
    symbols = ['+', '*']
    valid_sum = 0
    for key, value in dic.items():
        combinations = list(product(symbols, repeat = len(value)-1)) #create all possible combinations of operators
        for operator in combinations:
            temp = ''.join(str(value[i]) + operator[i] for i in range(len(operator))) + str(value[-1]) 
            if eval(temp) == key:
                valid_temp.append(key)
                break
    for i in valid_temp:
        valid_sum += i
    return valid_sum

if __name__ == "__main__":
    calculations = open_process_file()
    print(sum_valid(calculations))  #print the sum in cmd
