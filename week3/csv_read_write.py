
import csv

# assuming input.csv file exists with some data
with open('input.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    data = list(csv_reader)

# Perform some calculations on data here...

# Write the results back to a new CSV file
with open('output.csv', 'w') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(data)

print("Data processing complete.")
