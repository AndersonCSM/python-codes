## 1. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result = 'It exists'
    print(result)

## 2. Updating Dictionary Values ##

content_ratings = {'4+': 622, '12+': '1155', '9+': 987, '17+': 4433}

temp = content_ratings['4+']
content_ratings['4+'] = content_ratings['17+']
content_ratings['17+'] = temp

content_ratings['12+'] = int(content_ratings['12+'])

print(content_ratings)

## 3. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+':0, '9+':0, '12+':0, '17+':0}

for c_rating in apps_data:
    if c_rating[10] in content_ratings:
        content_ratings[c_rating[10]] += 1

print(content_ratings)

## 4. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}

for row in apps_data[1::]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
print(content_ratings)

## 5. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}

for i in apps_data[1::]:
    genre = i[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre]= 1
        
print(genre_counting)

## 6. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for k in content_ratings:
    content_ratings[k] = (content_ratings[k] / total_number_of_apps) * 100
    
percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['9+'] + content_ratings['4+'] + content_ratings['12+']

## 7. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_percentages = {}
c_ratings_proportions = {}

for k in content_ratings:
    c_ratings_proportions[k] = content_ratings[k] / total_number_of_apps
    c_ratings_percentages[k] = c_ratings_proportions[k] * 100

## 8. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []

for row in apps_data[1::]:
    size = float(row[2])
    data_sizes.append(size)

min_size = min(data_sizes)
max_size = max(data_sizes)