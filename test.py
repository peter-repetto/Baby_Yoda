# initial imports
import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas
import panel as pn
import plotly.express as px
import numpy as np
#import os
#import seaborn as sns
#import numpy as np
#from datetime import datetime, timedelta

import yoda_simulator as ys

portfolio1 = pd.read_csv('./all_data_pull/Yoda 1 - The World is Your Oyster.csv').set_index('Unnamed: 0')
portfolio2 = pd.read_csv('./all_data_pull/Yoda 2 - Play It Again Sam.csv').set_index('Unnamed: 0')
portfolio3 = pd.read_csv('./all_data_pull/Yoda 3 - Bond James Bond.csv').set_index('Unnamed: 0')
portfolio4 = pd.read_csv('./all_data_pull/Yoda 4 - Have Your Cake And Eat It Too.csv').set_index('Unnamed: 0')
portfolio5 = pd.read_csv('./all_data_pull/Yoda 5 - Show Me The Money.csv').set_index('Unnamed: 0')

years_to_retirement = 30
#portfolio_choice = dropdown.value
initial_investment = 1000 
withdraw_number = 40
withdraw_type = 'fixed amount'
investment_goal = 2500
portfolio = portfolio1
portfolio.iloc[2,:] = portfolio.iloc[2,:]/sum(portfolio.iloc[2,:])

portfolio_dimension = portfolio.shape


    
for stock in range(portfolio_dimension[1]):
    globals()['stock_%s' % stock]= np.random.normal(portfolio.iloc[0,stock], 
                                                    portfolio.iloc[1,stock],
                                                    252*30*500).reshape(252*30,500) 

next_beginning_balance = np.ones((1,500))
Portfolio_30_year = np.ones((1,500))

withdraw_amount = withdraw_number/initial_investment
withdraw_rate = withdraw_number

for year in range(30):
        #initialize for each year
    Portfolio_1_year = np.ones((1,500))

    for month in range(12):
            #initialize for each month
        portfolio_monthly_return = np.zeros((22,500))
        for stock in range(portfolio_dimension[1]):
            stock_month_daily_return = np.concatenate((next_beginning_balance,
                                                        (globals()['stock_%s' % stock][year*12*21+month*21:year*12*21+(month+1)*21])+1), 
                                                        axis = 0)
            midstep1 = np.cumprod(stock_month_daily_return, axis = 0)
            midstep2 = midstep1*portfolio.iloc[2,stock]
            portfolio_monthly_return += midstep2

            #get balance for rebalancing in next loop.
        next_beginning_balance = (portfolio_monthly_return[-1,:]).reshape(1,500)

        Portfolio_1_year = np.concatenate((Portfolio_1_year,portfolio_monthly_return[1:,:]), axis = 0)

    if withdraw_type != 'fixed amount':
        next_beginning_balance = (portfolio_monthly_return[-1,:]).reshape(1,500)*(1-withdraw_rate)
    else:
        next_beginning_balance =(portfolio_monthly_return[-1,:]).reshape(1,500)-withdraw_amount

    Portfolio_30_year = np.concatenate((Portfolio_30_year,Portfolio_1_year[1:,:]), axis = 0)
Portfolio_30_year_simulation = pd.DataFrame(Portfolio_30_year[1:])
 #   return Portfolio_30_year_simulation.iloc[:years_to_retirement*252]*initial_investment

 