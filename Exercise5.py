
# Exercise 5:
# Loop through elements in list
# Save value to list with temporary unique elements
# If element occurs second time, remove element

# Proof of concept:
long_sequence = [1, 2, 2, 4, 5, 6, 3, 1, 7, 8, 9, 3, 4, 10, 5, 11, 6, 12, 7, 8, 9, 13, 10, 11, 12, 13, 34]
memory = 8
chunk = []
i = 0
while i < len(long_sequence):
    chunk.append(long_sequence[i: i + 8])
    i += 8

unique_values = []
for n in chunk:
    if n in unique_values:
        unique_values.remove(n)
    else:
        unique_values.append(n)
#print(unique_values)

