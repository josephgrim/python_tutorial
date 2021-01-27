# Initialize my data variable
data = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

 # Read the first three lines (header)
 for _ in range(3):
    datafile.readline()

 # Read and parse the rest of the file
 for line in datafile:
    datum = line.split()
    data.append(datum)

# DEBUG
print(data[8][4])
print(data[8][:5])
print(data[8][::2])
