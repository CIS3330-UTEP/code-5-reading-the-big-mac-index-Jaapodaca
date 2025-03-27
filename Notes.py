import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

df['year'] = pd.to_datetime(df['date']).dt.year

def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    data = df[(df['year'] == year) & (df['iso_a3'] == country_code)]
    return round(data['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    data = df[df['iso_a3'] == country_code]
    return round(data['dollar_price'].mean(), 2) 

def get_the_cheapest_big_mac_price_by_year(year):
    data = df[df['year'] == year]
    cheapest = data.nsmallest(1, 'dollar_price')[['name', 'iso_a3', 'dollar_price']].values[0]
    return f"{cheapest[0]}({cheapest[1]}): ${cheapest[2]}"

def get_the_most_expensive_big_mac_price_by_year(year):
    data = df[df['year'] == year]
    most_expensive = data.nlargest(1, 'dollar_price')[['name', 'iso_a3', 'dollar_price']].values[0]
    return f"{most_expensive[0]}({most_expensive[1]}): ${most_expensive[2]}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2010, 'jpn'))
    print(get_big_mac_price_by_country('JPN'))
    print(get_the_cheapest_big_mac_price_by_year(2015))
    print(get_the_most_expensive_big_mac_price_by_year(2015))
