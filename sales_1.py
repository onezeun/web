f = open('sales.txt', 'r')
lines = f.readlines() 
f.close()

i = 0

for score in lines:
    i+=int(score)

f = open('summary.txt', 'w', encoding='utf-8')
f.write("총매출 = " + str(i) + '\n')
f.write("평균 일매출 = " + str(i/len(lines)))
f.close()