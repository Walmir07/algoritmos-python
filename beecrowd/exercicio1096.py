# Sequencia IJ 2

i = 1

for num in range(i, 10, 2):

    j = 7

    for cont in range(3):
        print("I={:.0f} J={:.0f}".format(i, j))
        j -= 1

    i += 2