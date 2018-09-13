
Array = [75,81,78,71,89,68,69,65,64,66,79,82,69,76,75,81,67,53,54,59,70,68,68,68]
S=0

for i in range(0,len(Array)):
    S = S+Array[i]*3/(len(Array)*3)

print(S)
