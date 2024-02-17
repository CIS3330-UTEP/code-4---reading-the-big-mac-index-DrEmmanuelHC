import pandas as pd

big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    query = f"date.str.startswith('{year}') and iso_a3 == '{country_code}'"
    result = df.query(query)
    if result.empty:
        return None  
    mean_price = result['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    query = f"iso_a3 == '{country_code}'"
    result = df.query(query)
    if result.empty:
        return None 
    mean_price = result['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    result = df[df['date'].str.startswith(str(year))]
    if result.empty:
        return None  
    cheapest = result['dollar_price'].idxmin()
    cheapest_mac = df.iloc[cheapest]
    return f"{cheapest_mac['name']}({cheapest_mac['iso_a3']}): ${round(cheapest_mac['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    result = df[df['date'].str.startswith(str(year))]
    if result.empty:
        return None  
    expensive = result['dollar_price'].idxmax()
    expensive_mac = df.iloc[expensive]
    return f"{expensive_mac['name']}({expensive_mac['iso_a3']}): ${round(expensive_mac['dollar_price'], 2) }"

if __name__ == "__main__":
    while True:
        print("\n1. Get Big Mac price by year and country code")
        print("2. Get Big Mac price by country code")
        print("3. Get the cheapest Big Mac price by year")
        print("4. Get the most expensive Big Mac price by year")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            year = input("Enter year: ")
            country_code = input("Enter country code: ").upper()
            price = get_big_mac_price_by_year(year, country_code)
            if price is not None:
                print(f"The mean Big Mac price in {country_code} for the year {year} is {price}.")
            else:
                print("No data found for the specified criteria.")
        elif choice == '2':
            country_code = input("Enter country code: ").upper()
            price = get_big_mac_price_by_country(country_code)
            if price is not None:
                print(f"The mean Big Mac price in {country_code} is ${price}.")
            else:
                print("No data found for the specified country code.")
        elif choice == '3':
            year = input("Enter year: ")
            cheapest_price = get_the_cheapest_big_mac_price_by_year(year)
            if cheapest_price is not None:
                print(cheapest_price)
            else:
                print("No data found for the specified year.")
        elif choice == '4':
            year = input("Enter year: ")
            expensive_price = get_the_most_expensive_big_mac_price_by_year(year)
            if expensive_price is not None:
                print(expensive_price)
            else:
                print("No data found for the specified year.")
        elif choice == '5':
            break
        else:
            print("Invalid choice")