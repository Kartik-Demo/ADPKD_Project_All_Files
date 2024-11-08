from prettytable import PrettyTable

myTable = PrettyTable(["Student Name", "Year", "Semister", "Percentage"])

myTable.add_row(["Leanord", "Second", "4th", "91.2 %"])


myTable.add_row(["Howard", "Second", "4th", "90.23 %"])

myTable.add_row(["Bernadette", "Second", "4th", "92.7 %"])

myTable.add_row(["Sheldon", "Third", "5th", "98.2 %"])

myTable.add_row(["Raj", "Third", "5th", "88.1 %"])

myTable.add_row(["Amy", "Third", "5th", "95.0 %"])

print(myTable)
