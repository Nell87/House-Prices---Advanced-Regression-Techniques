
#### 0.   INCLUDES / PREPARING DATA ______________________________________ #### 
# Loading Libraries
import pandas as pd  # reading csv 

# Reading datasets
train = pd.read_csv("C:/Sara/GitHub/House Prices - Advanced Regression Techniques/data/train.csv")
test = pd.read_csv("C:/Sara/GitHub/House Prices - Advanced Regression Techniques/data/test.csv")

# Summary
summary = train.describe()
train.shape         # (1460,81)
test.shape          # (1459,80)

del summary

#### 1.   CLEANING / PREPROCESSING ####

#### 1.1. Missing Values __________________________________________________ ####
train_missing = train.isnull().sum() * 100 / len(train)
test_missing = test.isnull().sum() * 100 / len(test)

thresh = 20*train.shape[0]/100
train = train.dropna(axis='columns', thresh=(thresh)) # Let's remove more than 80% missing
                                                      # 81 --> 77 variables
                                                      
variables_train = list(train.columns)
variables_train.remove('SalePrice')                                         
                                                      
test = test[variables_train]

del thresh
del train_missing
del test_missing
del variables_train

#### 2.   EXPLORATORY ANALYSIS ####
train.len()

#### 2.1. DV: SalePrice __________________________________________________ ####
