# import libraries
from IPython.display import display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_dataset (csv_file):
    """Function to return dataframes if filename is given"""
    base_path = os.getcwd() +'/store-sales-time-series-forecasting/'
    dataset = pd.read_csv(base_path + csv_file)
    return dataset

def datetime(df, col):
    df["date"] = pd.to_datetime(df[col])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.day_of_week
    df["day_name"] = df["date"].dt.day_name()
    df["quarter"] = df["date"].dt.quarter
    df["is_leap_year"] = df["date"].dt.is_leap_year
    return df


def dataAnalysis():
   """Function to do EDA step by step """
   # Load different datasets
   train = load_dataset("train.csv")
   test = load_dataset("test.csv")
   oil = load_dataset("oil.csv")
   stores = load_dataset("stores.csv")
   transactions = load_dataset("transactions.csv")
   holiday_events = load_dataset("holidays_events.csv")

#    #displaying the head of  dataset
   display(train.head())
   display(test.head())

   #checking for nan values in dataset
   print(train.isna().sum())
   print(test.isna().sum())

   train = datetime(train, "date")
   test =  datetime(test, "date")
   
   display(train.head())
   display(test.head())




if __name__ == "__main__":
    dataAnalysis()
    



   
