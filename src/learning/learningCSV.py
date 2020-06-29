import csv

data = []
counter = 0
labels = []

with open('test.csv',  newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if counter == 0: # if on the first row read in the labels
            for col in row:
                labels.append(col.strip())
        else: # else, collect the data into the data list
            data.append(row)

        counter += 1 # increase the row counter

with open('test.csv','a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow([])
    for i in range(0,10):
        writer.writerow(["DrX", 50 + i])

print(labels) # print the labels out




