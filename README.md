# Trading Crypto Bot

This will be linked to the kucoin api in either sandbox mode or in production mode. At the moment it is hard coded for sandbox mode.

## Requirements

Uses python3 and pipenv to install the reqirements in Pipfile.

## Algortihm

Version 1 will be very simple. It will analyse the last N days moving average. Check the gradient of this, and compare it with the current value and current gradient over X hours.

## Work to do

1. Save all the data into a database
1. ML time series prediction
