#table-printer
table_data = [["apples", "oranges", "cherries", "bananas"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]

table_info = []

for y in range(len(table_data)):
    column = []
    for x in range(len(table_data[y])):
        column.append(len(table_data[y][x]))
    #table_info.append(column)
    table_info = table_info[y].sort()

def print_table():
    for x in enumerate(table_data):
        print("H")
