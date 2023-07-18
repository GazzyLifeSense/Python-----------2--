# 10-1
with open('python.txt', encoding='utf-8') as f:
    # 1
    print(f.read())
    # 2
    for line in f:
        print(line)
    # 3
    lines = f.readlines()

for line in lines:
    print(line)
    
