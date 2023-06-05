## 1. Interfering with the Built-In Functions ##

a_list = [1, 8, 10, 9, 7]
print(max(a_list))

def max(list_):
    return "No max value returned"

max_val_test_0 = max(a_list)
print(max_val_test_0)

del max

print(max(a_list))

## 3. Default Arguments ##

def open_dataset(file_name='AppleStore.csv'):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset()

## 4. The Official Python Documentation ##

one_decimal = round(3.43, 1)
two_decimals = round(0.23321, 2)
five_decimals = round(921.2225227, 5)

## 5. Multiple Return Statements ##

def open_dataset(file_name='AppleStore.csv', header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    if header:
        data = list(read_file)
    else:
        data = list(read_file)[1::]
    return data

apps_data = open_dataset(header=False)

## 6. Not Using the else Clause ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:]
    else:
        return data