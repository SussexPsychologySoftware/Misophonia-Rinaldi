import itertools
import pandas as pd

# GET LIST OF CHANNELS AND COMBINATIONS IN CORRECT ORDER #

# all possible combinations of channels
channels = range(20,28)
codes = []
for L in range(len(channels) + 1):
    for subset in itertools.combinations(channels, L):
        codes.append(subset[::-1])

# Define a custom sorting key that orders elements as specified
def custom_key(item):
    order = [channels]  # Define the order of prefixes
    if len(item) == 0:
        return tuple([0] * len(order))  # Place empty tuples at the beginning
    prefix_index = order.index(item[0]) if item[0] in order else len(order)
    return (prefix_index, item)

# Sort the list using the custom key
sorted_lst = sorted(codes, key=custom_key)



# GET HEX NUMBERS IN CORRECT FORMAT #

# Conversion table of remainders to hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}

# function which converts decimal value to hexadecimal value
def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    if len(hexadecimal)==1:
        hexadecimal = '0'+hexadecimal
    
    return hexadecimal


hex_codes = []
for i in range(len(sorted_lst)):
    hex_codes.append(decimalToHexadecimal(i))

data = {
    "hex": hex_codes,
    "ports": sorted_lst
}

df = pd.DataFrame(data)

df.to_csv('digital_channels.csv', sep='\t', encoding='utf-8')