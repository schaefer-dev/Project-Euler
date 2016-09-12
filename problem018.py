# simple solution using recursion

#parameters:
maxdepth = 15;

def iter(x,y):
    if (y == maxdepth-1):
        return Matrix[x][y]
    else:
        return Matrix[x][y] + max(iter(x,y+1), iter(x+1,y+1))


# read and split data
data = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
data = data.split()
data = map(int,data)

# Build Triangle Matrix

Matrix = [[0 for x in range(maxdepth)] for y in range(maxdepth)] 
counter = 0
blocksize = 1
row = 0
while (counter < len(data)):
	for i in range(0,blocksize):
            Matrix[i][row] = data[counter]
            counter += 1
        blocksize += 1
        row += 1

# compute Routes

print(str(iter(0,0)))
