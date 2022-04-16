diagnostics = open('day3_input.txt', 'r').readlines()
diagnostics = [line.strip() for line in diagnostics]

print("Solution 1")

row_count = len(diagnostics) 
gamma_counter = []

for _ in range(0, len(diagnostics[0])):
    gamma_counter.append(0)

for bits in diagnostics:
    for i in range (0, len(bits)):
        if (bits[i] == '1'):
            gamma_counter[i] = gamma_counter[i] + 1

gamma_bin = ''
epsilon_bin = ''

for number in gamma_counter:
    if (number > row_count/2):
        gamma_bin += '1'
        epsilon_bin += '0'
    else:
        gamma_bin += '0'
        epsilon_bin += '1'

print("Power Consumption:", int(gamma_bin, 2) * int(epsilon_bin, 2))

print("Solution 2")

def filter_sequences(sequences, position, filter):
    result = []
    for sequence in sequences:
        if (sequence[position] == filter):
            result.append(sequence)
    return result

def calculate(type):
    sequences = diagnostics
    for i in range (0, len(diagnostics[0])):
        one_counter = 0
        
        for bits in sequences:
            if (bits[i] == '1'):
                one_counter += 1

        zero_counter = len(sequences) - one_counter

        if (one_counter >= zero_counter):
            if type == 'oxygen':
                sequences = filter_sequences(sequences, i, '1')
            else:
                sequences = filter_sequences(sequences, i, '0')
        else:
            if type == 'oxygen':
                sequences = filter_sequences(sequences, i, '0')
            else:
                sequences = filter_sequences(sequences, i, '1')

        if (len(sequences) == 1):
            result = sequences[0]
            break
    return result

life_support_rating = int(calculate('co2'), 2) * int(calculate('oxygen'), 2)
print("Life Support Rating:", life_support_rating)