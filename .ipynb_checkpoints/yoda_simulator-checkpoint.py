import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

np.random.seed(42)

def portfolio_by_retirement(portfolio, initial_investment, withdraw_type, withdraw_number, years_to_retirement):
    portfolio_dimension = portfolio.shape
    
    for stock in range(portfolio_dimension[1]):
        globals()['stock_%s' % stock]= np.random.normal(portfolio.iloc[0,stock], 
                                                        portfolio.iloc[1,stock],
                                                        252*30*500).reshape(252*30,500) 
    
    #initialize variables
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
                portfolio_monthly_return += np.cumprod(stock_month_daily_return, axis = 0)*portfolio.iloc[2,stock]

            #get balance for rebalancing in next loop.
            next_beginning_balance = (portfolio_monthly_return[-1,:]).reshape(1,500)

            Portfolio_1_year = np.concatenate((Portfolio_1_year,portfolio_monthly_return[1:,:]), axis = 0)

        if withdraw_type != 'fixed amount':
            next_beginning_balance = (portfolio_monthly_return[-1,:]).reshape(1,500)*(1-withdraw_rate)
        else:
            next_beginning_balance =(portfolio_monthly_return[-1,:]).reshape(1,500)-withdraw_amount

        Portfolio_30_year = np.concatenate((Portfolio_30_year,Portfolio_1_year[1:,:]), axis = 0)
    Portfolio_30_year_simulation = pd.DataFrame(Portfolio_30_year[1:])
    return Portfolio_30_year_simulation.iloc[:years_to_retirement*252]*initial_investment


def quantile_chart(portfolio, initial_investment, withdraw_type, withdraw_number, years_to_retirement):

    daily_quantiles = portfolio_by_retirement(portfolio,initial_investment, withdraw_type, withdraw_number, years_to_retirement).quantile(q=(0.10,0.5,0.9), axis = 1).T

    return daily_quantiles.plot(title = f"Investment of ${initial_investment}, withdraw {withdraw_type} by {withdraw_number} in {years_to_retirement} years.", 
                     figsize=(10,5))

def simulation_chart(portfolio, initial_investment, withdraw_type, withdraw_number, years_to_retirement):
    return portfolio_by_retirement(portfolio,initial_investment, withdraw_type, withdraw_number, years_to_retirement).plot(legend = False, title = "Portfolio simulation", figsize = (15,10))

def confidence_interval(portfolio, initial_investment, withdraw_type, withdraw_number, years_to_retirement):
    plt.figure() # this is top-level container for all plot elements, make sure to close it when not suing any more.
    investment_ending_price = portfolio_by_retirement(portfolio,initial_investment, withdraw_type, withdraw_number, years_to_retirement).iloc[-1]
    quantile_result = investment_ending_price.quantile(q=[0.05, 0.95])
    investment_ending_price.plot(kind = 'hist', title="90% confidence interval for tails")
    plt.axvline(quantile_result.iloc[0], color='r')
    plt.axvline(quantile_result.iloc[1], color='r')
    return plt