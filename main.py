#Import all the libraries that are necessary
import pandas as pd
import numpy as np
import os
import seaborn as sns

#Challenge 1

#In this challenge we will use the Temp_States.csv file.
#First import it into a data frame called temp.
temp = pd.read_csv("Temp_States.csv")

#Print temp
print(temp)

#Explore the data types of the Temp dataframe. What type of data do we have? Comment your result.
temp.info()
#The City and State columns are type object and the Temperature column is type float64

#Select the rows where state is New York
print(temp[temp.State=="New York"])

#What is the average of the temperature of cities in New York?
print(temp[temp.State=="New York"].mean())

#We want to know cities and states with Temperature above 15 degrees Celcius
print(temp[temp.Temperature > 15].City)

#We want to know which cities have a temperature above 15 degrees Celcius and below 20 degrees Celcius
print(temp[(temp.Temperature > 15) & (temp.Temperature < 20)].City)

#Find the mean and the standard deviation of the temperature of each state
print(temp.groupby("State").Temperature.mean())


#Challenge 2

#Load the employee.csv file into a DataFrame. Call the dataframe employee
employee = pd.read_csv("Employee.csv")

#Explore the data types of the Employee dataframe. Comment your results
employee.info()
#We have 5 columns with object type: Name, Department, Education, Gender, Title and 2 with int 64 data type: Years and Salary

#Show visually the frequency distribution (histogram) of the employee dataset. In few words describe these histograms?
sns.histplot(employee)
#What's the average salary in this company?
print(employee.Salary.mean())
#What's the highest salary?
print(employee.Salary.max())
#What's the lowest salary?
print(employee.Salary.min())
#Who are the employees with the lowest salary?
print(employee[employee.Salary == employee.Salary.min()])
#Could you give all the information about an employee called David?
print(employee[employee.Name == "David"])
#Could you give only David's salary?
print(employee[employee.Name == "David"].Salary)
#Print all the rows where job title is associate
print(employee[employee.Title == "associate"])
#Print the first 3 rows of your dataframe
print(employee[:3])
#Find the employees who's title is associate and the salary above 55?
print(employee[(employee.Title == "associate") & (employee.Salary > 55)])
#Group the employees based on their number of years of employment. What are the average salaries in each group?
print(employee.groupby("Years").Salary.mean())
#What is the average Salary per title?
print(employee.groupby("Title").Salary.mean())
#Show a visual summary of the data using boxplot. What Are the First and Third Quartiles? Comment your results.
sns.boxplot(data = employee)
first_quart_years = np.percentile(employee.Years,25)
third_quart_years = np.percentile(employee.Years,75)
first_quart_salary = np.percentile(employee.Salary,25)
third_quart_salary = np.percentile(employee.Salary,75)
print(first_quart_years, third_quart_years, first_quart_salary, third_quart_salary)

#Is the mean salary per gender different?
print(employee.groupby(employee.Gender).Salary.mean())
#Find the minimum, mean and the maximum of all numeric columns for each Department.
print(employee.groupby(employee.Department).describe())
#Bonus Question
#For each department, compute the difference between the maximal salary and the minimal salary.


#Challenge 3

#Open the Orders.csv dataset. Name your dataset orders
orders = pd.read_csv("Orders.zip", compression = "zip", index_col= "Unnamed: 0")
#Explore your dataset by looking at the data types and the summary statistics. Comment your results
print(orders.info())
print(orders.describe())
#We have different data types: 2 columns have float64, 8 columns have int64 and 4 columns have onject so more than half of the dataset is a number
#What is the average Purchase Price?
purch_price = orders.Quantity * orders.UnitPrice
print(purch_price.mean())
#What were the highest and lowest purchase prices?
print(purch_price.max())
print(purch_price.min())
#Select all the customers we have in Spain
print(orders[orders.Country == "Spain"].CustomerID.unique())
#How many customers do we have in Spain?
print(len(orders[orders.Country == "Spain"].CustomerID.unique()))
#Select all the customers who have bought more than 50 items ?
cust = orders.groupby(orders.CustomerID).InvoiceNo.count().reset_index()
print(cust[cust.InvoiceNo > 50].CustomerID)
#Select orders from Spain that are above 50 items
ord = orders[orders.Country == "Spain"]
print(ord[ord.Quantity > 50])
#Select all free orders
print(orders[orders.UnitPrice == 0])
#Select all orders that are 'lunch bag'
print(orders[orders.Description.str.contains("lunch bag")])
#Select all orders that are made in 2011 and are 'lunch bag'
print(orders[(orders.Description.str.contains("lunch bag"))&(orders.year == 2011)])
#Show the frequency distribution of the amount spent in Spain.
sns.histplot(data = ord.amount_spent)
#Select all orders made in the month of August
print(orders[orders.month == 8])
#Select how many orders are made by countries in the month of August
ord2 = orders[orders.month == 8]
print(ord2.groupby(ord2.Country).InvoiceNo.count())
#What's the average amount of money spent by country
print(orders.groupby(orders.Country).amount_spent.mean())
#What's the most expensive item?
print(orders[orders.UnitPrice == orders.UnitPrice.max()])
#What was the average amount spent per year ?
print(orders.groupby(orders.year).amount_spent.mean())


