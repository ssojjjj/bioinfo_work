
f = open("../data/067.filtered.fastq", "r")
A = f.readlines()

cnt = 0

for s in A:
    if s.startswith("@"):
        cnt = cnt+1


print(cnt)

