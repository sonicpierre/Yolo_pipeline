import os
print("Hello World !!")

with open('inputs/demo-dataset/salut_mon_gas.txt', 'r') as f:
    line = f.readlines()[0]

print(os.listdir('outputs/'))
with open('outputs/my-volume/output.txt', 'w') as f:
    f.write(line + "YOUPI")