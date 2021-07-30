

# read
reader = open('input.txt', 'r')
a, b = [int(n) for n in reader.readline().split(" ")]
reader.close()

# write
writer = open('output.txt', 'w')
writer.write("%d" % (a+b))
writer.close()
