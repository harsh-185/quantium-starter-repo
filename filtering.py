import csv

with open('filtered_data.csv', mode='w') as filtered_file:
        csv_writer = csv.writer(filtered_file)
        csv_writer.writerow(["Sales","Data","Region"])

def filter(file):
    with open('filtered_data.csv', mode='a') as filtered_file:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0]=="pink morsel":
                    sales=float(row[1][1:])*float(row[2])
                    date=row[3]
                    region=row[4]

                    csv_writer = csv.writer(filtered_file)
                    csv_writer.writerow([sales,date,region])

file1="data/daily_sales_data_0.csv"
file2="data/daily_sales_data_1.csv"
file3="data/daily_sales_data_2.csv"

filter(file1)
filter(file2)
filter(file3)
