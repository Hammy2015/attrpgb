import os
FOLDER_NAME = os.path.dirname(os.path.realpath(__name__))
import pandas as pd

#Magic item setup
f = open(FOLDER_NAME + "Magic_items.txt", "r")

item_data = []

item_pool = "broken"

for x in f:
    line = x
    if line.startswith("Le") or line.startswith("Grea"):
        item_t1 = line[0:line.find(" ")].replace(" ","")
        item_t2 = line[line.find(" "):line.find(" ",10)].replace(" ","")
        item_slot = line[line.find(" ",10):line.find("\n")].replace(" ","")
    elif line.startswith("d"):
        pass
    elif line.startswith("\n"):
        pass
    elif line.startswith("Table"):
        pass
    else:
        if line[2] == "-":
            lower_bound = line[0:2]
            upper_bound = line[3:5]
            #lower_bound = int(line[0:2])
            #upper_bound = int(line[3:5])
        else:
            lower_bound = line[0:2]
            upper_bound = line[0:2]
            #lower_bound = int(line[0:2])
            #upper_bound = int(line[0:2])
        item_name = line[line.find("\t")+1:line.find("\t",8)]
        try:
            item_price_string = line[line.find("\t",8)+1:line.find("gp",line.find("\t",8))].replace(",","").replace(" ","")
            item_price = int(item_price_string)
        except:
            print('item: ' + item_name + ' price is not correct: "' + item_price_string)
            item_price = 0
        item_data.append([item_t1,item_t2,item_slot,lower_bound,upper_bound,item_name,item_price,0])

#Conversions
headers = ['t1','t2','slot','lower','upper','name','price','range']

item_df = pd.DataFrame(data = item_data, columns = headers)

item_df['lower'] = item_df['lower'].astype('int')

item_df['upper'] = item_df['upper'].astype('int')

item_df['range'] = item_df['range'].astype('int')

for index, row in item_df.iterrows():
    item_df.loc[index, 'range'] = 1 + item_df.loc[index, 'upper'] - item_df.loc[index, 'lower']

for index, row in item_df.iterrows():
    if row['range'] < 0:
        item_df.loc[index, 'range'] = 101 - item_df.loc[index, 'lower']
    if row['t2'] == 'Least':
        item_df.loc[index, 'range'] = item_df.loc[index, 'range'] * 3
    if row['t2'] == 'Minor':
        item_df.loc[index, 'range'] = item_df.loc[index, 'range'] * 100
    if row['t2'] == 'Medium':
        item_df.loc[index, 'range'] = item_df.loc[index, 'range'] * 100
    if row['t2'] == 'Major':
        item_df.loc[index, 'range'] = item_df.loc[index, 'range'] * 100

def mig(price):
    if price < item_df['price'].min():
        return 'too poor'
    search_df = item_df.loc[(item_df['t2'] == 'Minor') & (item_df['price'] <= price)]
    item = search_df.sample(weights = 'range').iloc[0]['name']
    return item

def mig(price,tier):
    if price < item_df['price'].min():
        return 'too poor'
    search_df = item_df.loc[(item_df['t2'] == tier) & (item_df['price'] <= price)]
    item = search_df.sample(weights = 'range').iloc[0]['name']
    return item
