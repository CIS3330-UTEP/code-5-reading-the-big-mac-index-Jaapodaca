import pandas as pd 
df = pd.read_csv("./big-mac-full-index.csv")

# print(type(df ["date"][0]))

# query = "date >= '2018-01-02'"
# df = df.query(query)

# print(df)

# file_name = "./big-mac-full-index.csv"
# df = pd.read_csv(file_name)

# for idx, row in df.iterrows():
#     if row['dollar_price'] < 1:
#         print(row['dollar_price'])

smol_df = df.query("index < 10")

def get_new_country_name(row):
    new_country_name = f'{row['name']} ({row['iso_a3"]})']})'
    return new_country_name

smol_df['name'] = smol_df.apply(get_new_country_name, axis=1)
print(smol_df)