# Documentation 

## 1. Dataset Global Renewable Energy Production (2000-2023)
[Fuente](https://www.kaggle.com/datasets/ahmedgaitani/global-renewable-energy?resource=download)

Dataset Units: Gwh


### Exploratory data analysis:

- `SolarEnergy`: Annual solar energy production in gigawatt-hours (GWh).
- `WindEnergy`: Annual wind energy production in gigawatt-hours (GWh).
- `HydroEnergy`: Annual hydro energy production in gigawatt-hours (GWh).
- `OtherRenewableEnergy`: Annual energy production from other renewable sources (e.g., geothermal, biomass) in gigawatt-hours (GWh).
- `TotalRenewableEnergy`: Total annual renewable energy production in gigawatt-hours (GWh).

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



## 2. Dataset: Global primary energy consumption by source: 1990~2023

[Fuente](https://ourworldindata.org/grapher/global-energy-substitution?time=1990..2023)

Dataset Units: Gwh


### Exploratory data analysis:

### 1. Data type:
```python
RangeIndex: 76 entries, 0 to 75
Data columns (total 13 columns):
 #   Column                                         Non-Null Count  Dtype  
---  ------                                         --------------  -----  
 0   Entity                                         76 non-null     object 
 1   Code                                           76 non-null     object 
 2   Year                                           76 non-null     int64  
 3   Other renewables (TWh, substituted energy)     76 non-null     float64
 4   Biofuels (TWh, substituted energy)             76 non-null     float64
 5   Solar (TWh, substituted energy)                76 non-null     float64
 6   Wind (TWh, substituted energy)                 76 non-null     float64
 7   Hydropower (TWh, substituted energy)           76 non-null     float64
 8   Nuclear (TWh, substituted energy)              76 non-null     float64
 9   Gas (TWh, substituted energy)                  76 non-null     float64
 10  Oil (TWh, substituted energy)                  76 non-null     float64
 11  Coal (TWh, substituted energy)                 76 non-null     float64
 12  Traditional biomass (TWh, substituted energy)  76 non-null     int64  
dtypes: float64(9), int64(2), object(2)
```


### 2.  Identifying null values:
There are no missing values.


### 3.  Identifying duplicates:
There are no duplicates.



## 3. Dataset: Renewable Energy World Wide : 1965~2022 
[Fuente](https://www.kaggle.com/datasets/belayethossainds/renewable-energy-world-wide-19652022/data?select=01+renewable-share-energy.csv)


### 3.1.`12-solar-energy-consumption.csv`:

`definition`: solar energy consumed per year. There are two technologies for solar energy: (1) `mainstream`: photovoltaic which is with solar panels and (2) `solar thermal`: much less used.
💡 It might be interesting to see the variation of generation over time only for countries that we consider ‘key’ in renewable energy production.

### 3.1.1. Data type:
```python

RangeIndex: 8683 entries, 0 to 8682
Data columns (total 4 columns):
 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   Entity                        8683 non-null   object 
 1   Code                          7227 non-null   object 
 2   Year                          8683 non-null   int64  
 3   Electricity from solar (TWh)  8683 non-null   float64
dtypes: float64(1), int64(1), object(2)

```

### 3.1.2.  Identifying null values:

```python
Entity                           0.000000
Code                            16.768398
Year                             0.000000
Electricity from solar (TWh)     0.000000
dtype: float64
```
-- > The column `Code`  has 16.76% missing values. We will complete data through the Tableau tool (with map chart).



### 3.1.3.  Identifying duplicates:
--> no duplicates.


### 3.2.`13-installed-solar-PV-capacity.csv`:

`definition`: Photovoltaic solar power installed per territory (excluding solar thermal power). Units: GW.
💡 It might be interesting to see the variation of generation over time only for countries that we consider ‘key’ in renewable energy production.

### 3.2.1. Data type:
```python
RangeIndex: 1659 entries, 0 to 1658
Data columns (total 4 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Entity          1659 non-null   object 
 1   Code            1243 non-null   object 
 2   Year            1659 non-null   int64  
 3   Solar Capacity  1659 non-null   float64
dtypes: float64(1), int64(1), object(2)
```


### 3.2.2.  Identifying null values:

```python
Entity             0.000000
Code              25.075347
Year               0.000000
Solar Capacity     0.000000
dtype: float64
```
-- > The column `Code`  has 25.07% missing values. We will complete data through the Tableau tool (with map chart).



### 3.2.3.  Identifying duplicates:
--> no duplicates.


### 3.3.`15-share-electricity-solar.csv`:

`definition`: Solar (% electricity): percentage of total electricity produced.
💡 It might be interesting to see the variation of generation over time only for countries that we consider ‘key’ in renewable energy production.

### 3.3.1. Data type:
```python
RangeIndex: 6871 entries, 0 to 6870
Data columns (total 4 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   Entity                 6871 non-null   object 
 1   Code                   5781 non-null   object 
 2   Year                   6871 non-null   int64  
 3   Solar (% electricity)  6871 non-null   float64
dtypes: float64(1), int64(1), object(2)
```


### 3.3.2.  Identifying null values:

```python
Entity                    0.000000
Code                     15.863775
Year                      0.000000
Solar (% electricity)     0.000000
dtype: float64
```
-- > The column `Code`  has 15.86% missing values. We will complete data through the Tableau tool (with map chart).



### 3.3.3.  Identifying duplicates:
--> no duplicates.

 
### 3.4.`08-wind-generation.csv`:

`definition`: wind energy generated in a year and in a specific territory.

💡 It might be interesting to see the variation of generation over time only for countries that we consider ‘key’ in renewable energy production.

### 3.4.1. Data type:
```python
RangeIndex: 8676 entries, 0 to 8675
Data columns (total 4 columns):
 #   Column                       Non-Null Count  Dtype  
---  ------                       --------------  -----  
 0   Entity                       8676 non-null   object 
 1   Code                         7217 non-null   object 
 2   Year                         8676 non-null   int64  
 3   Electricity from wind (TWh)  8676 non-null   float64
dtypes: float64(1), int64(1), object(2)
```


### 3.4.2.  Identifying null values:

```python
Entity                          0.000000
Code                           16.816505
Year                            0.000000
Electricity from wind (TWh)     0.000000
dtype: float64
```
-- > The column `Code`  has 16.81% missing values. We will complete data through the Tableau tool (with map chart).


### 3.4.3.  Identifying duplicates:
--> no duplicates.



### 3.5.`11-share-electricity-wind.csv`:

`definition`: Wind (% electricity): total wind as a percentage of total electricity produced.

💡 It might be interesting to see the variation of generation over time only for countries that we consider ‘key’ in renewable energy production.

### 3.5.1. Data type:
```python
RangeIndex: 6871 entries, 0 to 6870
Data columns (total 4 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Entity                6871 non-null   object 
 1   Code                  5781 non-null   object 
 2   Year                  6871 non-null   int64  
 3   Wind (% electricity)  6871 non-null   float64
dtypes: float64(1), int64(1), object(2)
```


### 3.5.2.  Identifying null values:

```python
Entity                   0.000000
Code                    15.863775
Year                     0.000000
Wind (% electricity)     0.000000
dtype: float64
```
-- > The column `Code`  has 15.86% missing values, there is no code for areas other than countrie (e.g. Africa or EMEA)

### 3.5.3.  Identifying duplicates:
--> no duplicates.
 

### 3.6.`09-cumulative-installed-wind-energy-capacity-gigawatts`:

`definition`: installed wind power per territory in GW.

### 3.6.1. Data type:
```python
RangeIndex: 1540 entries, 0 to 1539
Data columns (total 4 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Entity         1540 non-null   object 
 1   Code           1143 non-null   object 
 2   Year           1540 non-null   int64  
 3   Wind Capacity  1540 non-null   float64
dtypes: float64(1), int64(1), object(2)
memory usage: 48.3+ KB
```


### 3.6.2.  Identifying null values:

```python
Entity            0.000000
Code             25.779221
Year              0.000000
Wind Capacity     0.000000
dtype: float64
```
-- > The column `Code`  has 25.77% missing values, there is no code for areas other than countrie (e.g. Africa or EMEA)


### 3.6.3.  Identifying duplicates:
--> no duplicates.
 