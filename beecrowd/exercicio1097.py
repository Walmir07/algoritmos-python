# Sequencia IJ 3

i = 1
j = 7

for num in range(i, 10, 2):

    for cont in range(3):
        print("I={:.0f} J={:.0f}".format(i, j))
        j -= 1
        
    j += 5
    i += 2