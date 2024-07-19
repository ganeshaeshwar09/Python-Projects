import copy

original = [1, [2, 3], 4]
deep = copy.deepcopy(original)
deep[1][0] = 'changed'

print(original)  # Output: [1, [2, 3], 4]
print(deep)      # Output: [1, ['changed', 3], 4]
