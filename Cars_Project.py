#imported all the libraries I needed
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3


#importing the scv file and understanding the data
cars = pd.read_csv("CarPrice.csv", index_col=0) #car_ID is the index
print(cars.shape) #to understand the data
print(cars.head())

cars_sql = cars[["CarName", "price"]] #Created a df for my relational db
sql = sqlite3.connect("Cars.db") #creating my sql db
s = sql.cursor()

#Creating the cars table, commented out because its already included
#s.execute("CREATE TABLE CARS (CarName text, price number)")
sql.commit()

#getting the data from my df to my db
cars_sql.to_sql("CARS", sql, if_exists="replace", index=False)

#Running a simple command on my db
print(s.execute("SELECT * FROM CARS"))

#Understanding my data
cars_types = cars.dtypes
print("Data Type of each column:")
print(cars_types)

#checking for any missing values
missing_values = cars.isnull().sum()
print(missing_values)

#Dropping any dupilcate car names
cars.drop_duplicates(subset="CarName")
cars_count = cars["CarName"].value_counts() #counting the cars to see how many are left
print(cars_count)

#Sorting and subsetting to find the fastest cars
fastest_cars = cars[["CarName", "horsepower"]]
fastest_cars = fastest_cars.sort_values("horsepower", ascending=False)
print(fastest_cars.head())

#Sorting and subsetting to find the most expensive cars
highest_prices = cars[["symboling", "CarName", "price"]]
highest_prices = highest_prices.sort_values("price", ascending=False)
print((highest_prices.head()))

#Creating a new dataframe and making "symboling" the new index
highest_prices_index = highest_prices.set_index("symboling")
print(highest_prices_index.head())

#Grouping to see which carbody is the most expensive and fastest on average
carbody_price = cars.groupby("carbody")[["horsepower", "price"]].mean()
print(carbody_price)

#Using the for loop to print the column names
for val in cars:
    print(val)

#for loop to print the row labels and row data for the whole dataframe
for label, row in cars.iterrows():
    print(label)
    print(row)

#Merged highest_prices with fastest_cars on the CarName column
highest_prices.merge(fastest_cars, on=["CarName"])
print(highest_prices)

#Creating a function for the values of the car prices
def  price_function():
    print("The average price is: " + str(cars["price"].mean()))
    print("The highest price is: " + str(cars["price"].max()))
    print("The lowest price is: " + str(cars["price"].min()))
    print("The middle price is: " + str(cars["price"].median()))

price_function() #calling the function

#Using seaborns replot function
sns.relplot(data=cars, x="enginesize", y="wheelbase", hue="horsepower")

cars.plot(x="enginesize",
          y="price",
          kind="scatter",
          rot=45)
plt.show()

del carbody_price["horsepower"]
carbody_price.plot(kind="bar",
                   title="Mean price by car body type",
                   rot=90)
plt.show()

cars[cars["fueltype"]=="gas"]["price"].hist(alpha=1)
cars[cars["fueltype"]=="diesel"]["price"].hist(alpha=.8)
plt.legend(["gas", "diesel"])
plt.show()

cars.plot(x="enginesize",
          y="citympg",
          kind="scatter",
          rot=45)
plt.legend(["citympg"])
cars.plot(x="enginesize",
          y="highwaympg",
          kind="scatter",
          rot=45)
plt.legend(["highwaympg"])
plt.show()
