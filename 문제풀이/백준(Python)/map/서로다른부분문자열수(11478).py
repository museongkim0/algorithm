import sys

out = sys.stdin.readline().rstrip()

dict = {}

for i in range(len(out)):
    for j in range(len(out)-i):
        dict[out[j:j+i+1]] = 1
        
print(len(dict))