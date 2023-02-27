# Creating List With For Loop
tnx = [10, 20, 30, 40, 50]

def total_amt(num):
    gst_rate = 0.1
    return num * (1 + gst_rate)

final_amt = []
for i in tnx:
    final_amt.append(total_amt(i))
print(final_amt) # Output -> [11.0, 22.0, 33.0, 44.0, 55.00000000000001]

tnx_with_tax = map(total_amt, tnx)
print(list(tnx_with_tax)) # Output -> [11.0, 22.0, 33.0, 44.0, 55.00000000000001]

# Creating List With List Comprehension
# New_List = [Expression For Member In Iterable]
print([i * i for i in range(10)]) # Output -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([total_amt(num) for num in tnx]) # Output -> [11.0, 22.0, 33.0, 44.0, 55.00000000000001]
 #Alternatively
print([num * (1 + 0.1) for num in tnx]) # Output -> [11.0, 22.0, 33.0, 44.0, 55.00000000000001]

# List Comprehension With Conditional Logic
# New_List2 = [Expression For Member In Iterable (if condition)]
print([vowels for vowels in 'Hello World' if vowels in 'aeiou']) # Output -> ['e', 'o', 'o']