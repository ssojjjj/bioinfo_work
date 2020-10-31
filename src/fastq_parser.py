
f = open("./review/data067.filtered.fastq", r)
A = f.readline()

cnt = 0
if A.startwith("<"):
    cnt += 1

print(cnt)

