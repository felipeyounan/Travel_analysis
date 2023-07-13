#1) If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
#2) How does the answer to the previous question chance if you change the duration of the trip to 4 days, 10 days or 2 weeks?
#3) If your total budget for the trip is $1000, wicth city should you visit to maximize the duratation of your trip? Which city should you visit if you want to minimize the duration?
#4) How does the answer to the previous question change if your budget is $600, $2000 or $1500
import pandas as pd
import numpy as np 

data = pd.read_excel('Data Exercise 1.xlsx')
df = pd.DataFrame(data)
df

days = int(input('how many days will you travel? '))
budget = int(input('what is your budget for this trip? '))

def cost_of_trip(days, budget):
    data = pd.read_excel('Data Exercise 1.xlsx')
    df = pd.DataFrame(data)

    df['Total Hotel expense($)'] = df['Hotel per day($)']*days
    rest_of_div = days % 7
    if rest_of_div >= 0:
        while rest_of_div >= 0:
            rest_of_div = days % 7
            if rest_of_div == 0:
                week = days / 7
                break
            days = days + 1
        if rest_of_div != 0:
            week = (days - 1) / 7
    df['Total Weekly Car Rental($)'] = df['Weekly Car Rental($)'] * week
    df['Sum($)'] = df['Return Flight($)'] + df['Total Hotel expense($)'] + df['Total Weekly Car Rental($)']
    mi = df[df['Sum($)'] == df['Sum($)'].min()]
    len(mi)
    if len(mi) >= 1:
        cost = mi['Sum($)'].to_string(index=False)
        place = mi['City'].to_string(index=False)
        print('If you are planning to stay 1-week long, for the least cost, you will spend ${}  in {}'.format(cost, place))
        print(f'here, check the informatoins')
        print(mi)
    #budget
    df['Sum($)'] = df['Sum($)'].astype('int')
    df['dif'] = budget - df['Sum($)']
    budget
    df
        
    while (df['dif'].any() > 0) == True:
        df['Sum($)'] = df['Return Flight($)'] + df['Hotel per day($)'] * days + df['Weekly Car Rental($)'] * week
        df['dif'] = budget - df['Sum($)']
        if (df['dif'] == 0).any():
            mi2 = df[df['dif'] == df['dif'].min()]
            city = df['City'].to_string(index=False)
            print(mi2)
            print(f"To maximize your stay You'll be for ", days, "days in",city )
            break
        days += 1


cost_of_trip(days,budget)