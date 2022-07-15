NumOfDays = int(input("Enter the no. of days: "))
temp = []
total = 0
for i in range(NumOfDays):
    NextDay = int(input('Day ' + str(i+1) + "'s " + 'temp: ' ))
    temp.append(NextDay)
    total += temp[i]

avg = round(total/NumOfDays, 2)
print("Average: " + str(avg))


above = 0
for i in temp:
    if i > avg:
        above += 1

print('No. of Days(s) above average: ' + str(above))