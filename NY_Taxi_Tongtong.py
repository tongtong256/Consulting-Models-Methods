import numpy as np
import pandas as pd
import pandas_profiling as pp
import matplotlib.pyplot as plt 


# import worksheet through panda
taxi = pd.read_csv(r'C:\Users\tongt\Desktop\Consulting Models and Methods\sample_taxis.csv')

print("Answer to Tip_Amount_01:\n")

# count the number of rows which satisfy "tip_amount > 0.15 * fare_amount"
tips_more_than_15pct_fare = len(taxi[taxi.tip_amount > 0.15 * taxi.fare_amount])
print(tips_more_than_15pct_fare)


print("\nAnswer to Tip_Amount_02:\n")

#  describe() provides the summary statistics
print(taxi.tip_amount.describe())


# Generate a detailed report of all the columns
report = pp.ProfileReport(taxi)
report.to_file('profile_report.html')


months = [] # create a new list to store the month value of each row
for date in taxi.tpep_pickup_datetime.values: # for loop in pickup dates
	# Each date is formatted as Year-Month-Day, split it by '-' and get only the month
	split_str = date.split('-') 
	# the 2nd element of each date is the month, store it for each row
	mon = split_str[1]
	# Get the month value of each row, now we have the new list of months
	months.append(mon)

# Add a new column 'months' to the dataset and save it as a new file
column_values = pd.Series(months)
taxi.insert(loc=2, column='months', value=column_values)
taxi.to_csv('taxi_new.csv')


print("\nAnswer to Seasonality_01:\n")

# summary statistics on tip_amount vary by months
month_tips = pd.DataFrame({'months': months, 'tip_amount': taxi.tip_amount})
print(month_tips.groupby(['months']).describe())


print("\nAnswer to Seasonality_02:\n")

# create a new dataframe includes two columns: months & passenger_count
month_passengers = pd.DataFrame({'months': months, 'passenger_count': taxi.passenger_count})

# get the numbers of trips with more than 1 customer vary by months
trips_more_than_one_passenger = month_passengers[month_passengers['passenger_count'] > 1]
trips_more_than_one_summary = trips_more_than_one_passenger.groupby(['months']).count()
print(trips_more_than_one_summary)

# visualization - bar chart
trips_more_than_one_summary.plot.bar()
plt.ylabel('Numbers of trips with more than 1 passenger')
plt.title('Numbers of trips with more than 1 passenger vary by months')
plt.show()



print("\nAnswer to Seasonality_03:\n")

# summary statistics on fare_amount vary by months
month_fare = pd.DataFrame({'months': months, 'fare_amount': taxi.fare_amount})
print(month_fare.groupby(['months']).describe())



