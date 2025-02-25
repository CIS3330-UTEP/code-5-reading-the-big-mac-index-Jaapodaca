import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    data = df[(df['date'].str.contains(str(year))) & (df['iso_a3'].str.lower() == country_code.lower())]
    return round(data['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    data = df[df['iso_a3'].str.lower() == country_code.lower()]
    return round(data['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    data = df[df['date'].str.contains(str(year))]
    cheapest = data.loc[data['dollar_price'].idxmin()]
    return f"{cheapest['name']}({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    data = df[df['date'].str.contains(str(year))]
    expensive = data.loc[data['dollar_price'].idxmax()]
    return f"{expensive['name']}({expensive['iso_a3']}): ${round(expensive['dollar_price'], 2)}"

if __name__ == "__main__":
    pass # Remove this line and code your user interface

print(get_big_mac_price_by_year(2010, 'usa'))
print(get_big_mac_price_by_country('jpn'))
print(get_the_cheapest_big_mac_price_by_year(2015))
print(get_the_most_expensive_big_mac_price_by_year(2015))