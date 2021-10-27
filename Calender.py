import pandas as pd
start = input("Enter Start Period YYYYMMDD : ")
end = input("Enter End Period YYYYMMDD : ")
mondays = pd.date_range(start=start, end=end, freq='WOM-1SUN')
ans = []
for m in mondays:
    if m.day == 1:
        ans.append(m)
        print(m)
print(f"There are {len(ans)} Sundays which is first date of each months")