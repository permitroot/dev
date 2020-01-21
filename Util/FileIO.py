# avoidant OOM
f_in = file('filename.txt', 'w')
for line in f_in.readlines():
    print(line[:-1]) # Hard line break