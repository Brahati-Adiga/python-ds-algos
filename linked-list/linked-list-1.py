from collections import defaultdict
Sample_dict = defaultdict(list)

def hash_string(string, size):
    return sum([ord(literal) for literal in string])%size


with open("C:\\Users\\BRAHATI ADIGA\\Downloads\\tt.txt", 'r+') as f:
    if f.read(1) != '\n':
        f.flush()
        f.seek(0)
    lines = [line[:-1] for line in f]
for line in lines:
    print(line)
    result = hash_string(line, 16)
    Sample_dict[result].append(line)
print(Sample_dict)

