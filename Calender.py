month = {i+1 : 31 for i in range(12)} # All the rest
month[4], month[6], month[9], month[11] = 30, 30, 30, 30 # Apr, Jun, Sep, Nov
month[2] = 28 # Feb
print(month)
year = 1901
for i in range(1900, 2002):
    flag = "평년"
    if i%4==0:
        flag = "윤년"
        if i%100