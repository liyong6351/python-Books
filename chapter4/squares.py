squares = []
for value in range(1,20,2):
    squares.append(value**2)
print(squares)
print('min=' + str(min(squares)))
print('max=' + str(max(squares)))
print('sum=' + str(sum(squares)))

squares1 = [value**2 for value in range(1,11)]
print(squares1)