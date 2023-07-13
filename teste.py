days = 7
budget = 1000
df['Sum($)'] = df['Sum($)'].astype('int32')
dif = budget - df['Sum($)']
if dif >= 0:
        while dif >= 0:
            days = days + 1
            df['Sum($)'] = df['Return Flight($)'] + df['Hotel per day($)'] * days + df['Total Weekly Car Rental($)']
            dif = budget - df['Sum($)']
            if dif == 0:
                print(df['Sum($)'].min())
                break