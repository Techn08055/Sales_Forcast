## Introduction
aslkjfdskf
The following is self learning project to analyse the sales in asote using the kaggle dataset  [Sales Forecast](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/code)

## How To Start
You can easily follow the steps and analyse the dataset and train the initial model using the repo now

* Clone the repo:
`git clone https://github.com/Techn08055/Sales_Forcast.git`

* Download the dataset : [Sales Forecast](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/code)

* You can create a conda env we are using Python 3.8

* Install dependencies: `conda create --name <env> --file requirements.txt`

Now you can run the jupyter notebook [First_Cycle.ipynb](First_Cycle.ipynb) to start nalysing the dataset and train your initial model.

### Issues:

* Most features related to train dataset like holiday_events & cluster_names are not available for test dataset and is assumed to be `0`. Proper feature Engineering is required to improve the performnce.

* Over looked the time factor and only trained using XGBoost

* Ignored other factors such as uil price and calamities.

