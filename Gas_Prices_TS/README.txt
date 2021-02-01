# Diesel forecasting 

These notebooks aiming to explore and answer the question: 
- How much will be the price of any fuel in the next week?
The predictions are based on observed values disclosed by the National Agency of Petroleum Natural Gas and
Biofuels, and it is done over a weekly horizon. 

Despite the main focus here is on price forecasting, there are many interesting questions that
could be addressed by this data, such as:
- How many liters will be sell of any fuel in the next week in a city?
- Is there any relation between cities/regions and fuel consummation or fuel price? if yes, how is it?
- When and where are expected the largest variations on price?
- Is any fuel in specific having an aggressive strategy?

and, of course, the questions proposed for the dataset owner:
- Which states are the cheapest (or most expensive) for different types of fuels in the last record
- State with the largest and smallest number of gas stations
- On average the state with the cheapest and most expensive price of gasoline
- Analyze gasoline growth by regions
- Investigate the evolution of gasoline prices in the last two years:
	By Region
	By States

As an initial step, the predictions are performed on Diesel, 
and the strategy is the following:
 -------------------------------------------------------------------------
| Create a baseline model:
|	the price for the next week is the same as in the previous week
|	metric: root mean squared logarithm error (RMSLE, the relative error between the predicted and true values)
|	Baseline error        -> RMSLE = 0.6646
|
| Create version V1 to hit the baseline error:
|	Choose the target to be modeling: current_price - future_price (mean stationary)
|	feature engineering: Creating more (and more and more) features:
|		daily/monthly/day of the year and week of the year seasonality
|		lag and difference between lags
|		moving average
|		ranking the first lag of differences
| Modeling: 
|	RandomForestRegressor -> RMSLE = 0.6539
|	RandomForestRegressor2-> RMSLE = 0.6855
|	LightGBMRegressor     -> RMSLE = 0.6619
|
| Feature selection:
|	LightGBMRegressor     -> RMSLE = 0.6587
|	RandomForestRegressor -> RMSLE = in progress
|
| hyperparameters optimization:
|	Scikit-Optimize: in progress
|
| Estimate the interval to retrain the model:
|	in progress	
