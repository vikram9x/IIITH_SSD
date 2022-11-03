import csv
#from tabulate import tabulate


file_data = []
with open("lab_11_data.csv", newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    file_data = list(csv_reader)

col_names = file_data[0]
file_data = file_data[1:]

#i drop last n rows -- 6 is hardcoded because of question req
file_data = list(map(lambda x : x[:-6], file_data))
#print(tabulate(file_data, showindex='always'))

#ii drop -ve % change rows < -3%
file_data = list(filter(lambda x: float(x[6]) >= -3.0 , file_data[1:]))
#print(tabulate(file_data, headers=col_names[:-6], showindex='always'))

#iii avg of open, high, low and write to file avg_output.txt
avg_open = sum(map(lambda x : float(x[1].replace(',', '')), file_data)) / len(file_data)
avg_high = sum(map(lambda x : float(x[2].replace(',', '')), file_data)) / len(file_data)
avg_low = sum(map(lambda x : float(x[3].replace(',', '')), file_data)) / len(file_data)
with open("avg_output.txt", 'w', newline='\n') as avg_file:
    avg_file.write(str(avg_open) + "\n")
    avg_file.write(str(avg_high) + "\n")
    avg_file.write(str(avg_low) + "\n")


#iv Display info for names starting with a specific char
ch = input("Enter a character : ")
file_data = list(filter(lambda x : x[0][0] == ch, file_data))
#print(tabulate(file_data, showindex='always'))

#v write output to stock_output.txt
with open("stock_output.txt", 'w') as stock_file:
    for x in file_data:
        stock_file.write(' '.join(x))
        stock_file.write("\n")