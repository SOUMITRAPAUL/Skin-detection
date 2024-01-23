# Read probabilities from text files
def read_probabilities(file_path):
    probabilities = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            pixel = tuple(map(int, parts[0][1:-1].split(',')))
            probability = float(parts[1].strip())
            probabilities[pixel] = probability
    return probabilities

# Calculate sum of probabilities
def calculate_sum_of_probabilities(probabilities):
    return sum(probabilities.values())

# Calculate threshold
def calculate_threshold(sum_p_cs, sum_p_cns):
    return sum_p_cs / sum_p_cns

# Example usage
p_cs_file_path = 'p_cs_probabilities.txt'
p_cns_file_path = 'p_cns_probabilities.txt'

p_cs_probabilities = read_probabilities(p_cs_file_path)
p_cns_probabilities = read_probabilities(p_cns_file_path)

# Calculate sum of probabilities for P(c|S) and P(c|NS)
sum_p_cs = calculate_sum_of_probabilities(p_cs_probabilities)
sum_p_cns = calculate_sum_of_probabilities(p_cns_probabilities)

# Calculate threshold T
threshold = calculate_threshold(sum_p_cs, sum_p_cns)

# Print the results
print(f"Sum of P(c|S): {sum_p_cs}")
print(f"Sum of P(c|NS): {sum_p_cns}")
print(f"Threshold T: {threshold}")
