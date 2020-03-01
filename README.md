# Robo Retirer
## Team Member 
* Peter Repetto
* Junwei Luo
* Ninoslav Vasic
* Troy Draizen 
* Kevin Qiu 
* Jeff Slentz

## Project Description 

Planning on creating a dashboard to help people, based off their risk tolerance, when they will be able to retire.  The Dashboard will allow the user to select parameters in regards to their goals.  The Dashboard will then output various financial metrics to help the user understand how feasible their goal is.  

## Major files to be used:

1. Portfolio datafiles: There are 5 csv files in 'all data pull' folder representing the 5 portfolios compsed by portfolio managers.  These five portfolios will be picked by investors through yoda-simulators to show the investment performance.

2. Yoda_simulator.py: This simulator calculates portfolio performance based on users' input.  Users can also use simulator to calculate withdraw/deposit amount/rate to achieve certain investment goal.

3. Baby Yoda Dashboard Final.ipynb: User-interface of the retirement-planning robo.  It will allow users to input initial investment, investment goal and withdraw/deposit amount, and then inform users what they need to do.

4. Final Baby Yoda Presentation.pptx: Presentation for whole project.

## Reasearch Questions to Answer

1. What do my future portfolio returns look like?

2. In n years, what are the percentile bands around the projected returns?

3. If I withdraw n% from the portfolio each year, how will effect my overall portfolio? 

4. Depending on my risk tolerance, am I taking an adequate amount of risk?  Or too much or too little risk? 

5. How correlated does my portfolio look? 

## Datasets to be used

* Iex Finance 
* Yahoo Finance
* User's Preference 
* Quandl 
* Fred 

## Rough Breakdown of Tasks 

* Build a Skeleton of the project tasks
* Pull in the data from various sources 
* Clean the data 
* Merging the data into a datafrane
* Peforming analysis on dataframe i.e. returns, risk stats, correlation
* Build dashboard 
* Pilot testing of the dashboard
* Live Production








