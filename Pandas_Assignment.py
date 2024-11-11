import pandas as pd

data = pd.read_csv('Automobile_data.csv')

df = pd.DataFrame(data)

# Exercise 1: From the given dataset print the first and last five rows
print("ANS 1: ")
print(df.head())
print(df.tail())
print("------------------------------------------------------------------")

# Exercise 2: Clean the dataset and update the CSV file
print("ANS 2: ")
df = df.replace('?', pd.NA)
df = df.replace('n.a', pd.NA)
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())
df['average-mileage'] = df['average-mileage'].fillna(df['average-mileage'].mean())
df['price'] = df['price'].fillna(df['price'].mean())
df['engine-type'] = df['engine-type'].fillna('Unknown')
df['num-of-cylinders'] = df['num-of-cylinders'].fillna('Unknown')
df.to_csv("cleaned_car_data.csv", index=False)
print("Cleaned and stored in a new file!")
print("------------------------------------------------------------------")

# Exercise 3: Find the most expensive car company name
print("ANS 3: ")
max_row = df.loc[[df['price'].idxmax()], ['company', 'price']]
print(max_row)
print("------------------------------------------------------------------")

# Exercise 4: Print All Toyota Cars details
print("ANS 4: ")
toyota_cars = df[df["company"] == "toyota"]
print(toyota_cars)
print("------------------------------------------------------------------")

# Exercise 5: Count total cars per company
print("ANS 5: ")
cars_per_company = df.groupby("company").size().sort_values(ascending=False)
print(cars_per_company)
print("------------------------------------------------------------------")

# Exercise 6: Find each company’s Highest price car
print("ANS 6: ")
highest_price = df.loc[df.groupby("company")["price"].idxmax(), ["company","price"]]
print(highest_price)
print("------------------------------------------------------------------")

# Exercise 7: Find the average mileage of each car making company
print("ANS 7: ")
avg_mileage = df.groupby("company")["average-mileage"].mean()
print(avg_mileage)
print("------------------------------------------------------------------")

# Exercise 8: Sort all cars by Price column
print("ANS 8: ")
sorted_price = df.sort_values(by="price", ascending=False)
print(sorted_price)
print("------------------------------------------------------------------")

# Exercise 9: Concatenate two data frames using the following conditions

# Create two data frames using the following two dictionaries Links to an external site
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
print("ANS 9: ")
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500, 58900]}
df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(japaneseCars)
df_combined = pd.concat([df_german, df_japanese], keys=['Germany', 'Japan'])
print(df_combined)
print("------------------------------------------------------------------")

# Exercise 10: Merge two data frames using the following condition

# Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
print("ANS 10: ")
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

df_price = pd.DataFrame(Car_Price)
df_horsepower = pd.DataFrame(car_Horsepower)
merged_df = pd.merge(df_price, df_horsepower, on='Company')
print(merged_df)
print("------------------------------------------------------------------")