# Documentation 

## Global Renewable Energy Production (2000-2023)
[Fuente](https://www.kaggle.com/datasets/ahmedgaitani/global-renewable-energy?resource=download)

Dataset Units: Gwh


### Exploratory data analysis:

### 1. Data type:
```python
RangeIndex: 240 entries, 0 to 239
Data columns (total 7 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Year                  240 non-null    int64  
 1   Country               240 non-null    object 
 2   SolarEnergy           240 non-null    float64
 3   WindEnergy            240 non-null    float64
 4   HydroEnergy           240 non-null    float64
 5   OtherRenewableEnergy  240 non-null    float64
 6   TotalRenewableEnergy  240 non-null    float64
dtypes: float64(5), int64(1), object(1)
```


### 2.  Identifying null values:
There are no missing values.


### 3.  Identifying duplicates:
There are no duplicates.



## Dataset: Renewable Energy World Wide : 1965~2022 
[Fuente](https://www.kaggle.com/datasets/belayethossainds/renewable-energy-world-wide-19652022/data?select=01+renewable-share-energy.csv)


### `12-solar-energy-consumption.csv`:

### 1. Data type:
![alt text](images/im5.png)

--> All `dtypes` are correct.


### 2.  Identifying null values:

![alt text](images/im6.png)

We have same nulls percentage filtering by "MEASURE" == "`KTOE`" or "MEASURE" == "`PC_PRYENRGSUPPLY`":

![alt text](images/im3.png)
![alt text](images/im4.png)



### 3.  Identifying duplicates:
--> no duplicates.


### 4.  Modifications:

Identifying interesting columns in dataset:

- Dataset columns to be deleted:
    - `Indicator`: one unique value == `RENEWABLE`
    - `Frequency`:  one unique value == `A`
    - `Subject`: one unique value == `TOT`
    - `Flagcodes`: 75% nulls
    - `Measure`: we are only interested in the column `PC_PRYENRGSUPPLY` (== `percentage of total primary energy supply`). We delete the other measure.

- Dataset columns interesting:
    - `value`: we rename it as `total_energy_supply`.


