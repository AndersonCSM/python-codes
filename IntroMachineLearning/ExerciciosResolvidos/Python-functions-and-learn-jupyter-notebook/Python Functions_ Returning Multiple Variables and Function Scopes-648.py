## 1. Returning Multiple Variables ##

def pythagorean(a, b):
    c = (a**2+b**2)**(0.5)
    return a**2, b**2, int(c**2)

rest = pythagorean(5, 12)
a_squared = rest[0]
b_squared = rest[1]
c_squared = rest[2]
print(rest)

## 2. Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:]
    else:
        return data

header, apps_data = open_dataset()

## 3. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
apps_data, header = open_dataset()