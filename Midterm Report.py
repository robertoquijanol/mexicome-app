#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:01:35 2020

@author: jeanpierresalendres
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:36:00 2020

@author: Maria Covarrubias
Roberto Quijano
Jean Pierre Salendres
"""

#MEXICOME
# Midterm Report: Summary of Porject's current status
# Code Packages: Install the required packages 
# The panda package will help us create data frames and manipulate the data.
# Numpy offers tools to work with numerical data and create matrix data structures. 
 
import pandas as pd
import numpy as np

#%%Part 1: Retrieving Coronavirus Data from the Web

#The goal will be to use official government data from the site:
# https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico
# However, the page has been out of service for the past week. 
# In the meantime, we will be using a dataset that compiles coronavirus 
# data from Mexico by 1) city (for the 14 cities we are covering in the country)
# and 2) by municipalities within Mexico City.
# The data has daily records, for days that have a coronavirus ocurrence. 
# Days with no coronavirus active cases are not recorded.

# Step 1: Read Coronabvirus CSV file

# The following csv is the temporary file we are using.
# We will simply add a 'download' webscraping modality to read the
# government's csv file once their website is up and running. 

######(look at simon munzert's code and try to add this for saturday)


csv = 'covid_mexico.csv'

# Step 2: Create a data frame from the csv file. 

df = pd.read_csv(csv, encoding ='latin-1')

df['Date'] = df['Date'].str.replace('/', '.')

# Step 3: Create if-else statement to retrieve city-specific 
# coronavirus information. 

# In the code below, we define an object to hold the if-else statement ("covid_casos).
# We break the statement into two parts: one for the 14 cities and one for
# Mexico City. Since the latter is the capital, the data for it is recorded
# by municipality within the city. 

# We will need to retrive this data with a different statement 
# ("elif" statement) than data for the the other cities ("if" statement).

# A ".sum()" function will add all the days (unique rows in the csv) 
# where the city reports active coronavirus cases. This will give us the total 
# active cases for the city. Moreover, for Mexico City, the sum function will add 
# all daily rows with active cases from each of its 16 municipalities. 

# Lastly, we will have an "else" statement for selected cities where there is
# no data or as a backup in case there is a retrieval error.


def covid_casos(ciudad):
    ciudades = ['MÉRIDA', 'PUERTO VALLARTA', 'CANCÚN', 'GUANAJUATO', 'LOS CABOS', 'ACAPULCO', 'SAN MIGUEL DE ALLENDE', 'CHAPALA', 'PUERTO ESCONDIDO', 'TIJUANA', 'MAZATLÁN', 'PUERTO PEÑASCO', 'PUEBLA', 'OAXACA']
    if ciudad in ciudades:
        casos = df.loc[(df['Municipality'])==ciudad, 'Active'].sum()
        print("El número de casos activos en", ciudad, "es:", casos)
    elif ciudad == 'CIUDAD DE MÉXICO':
        casos1 = df.loc[(df['State'])==ciudad, 'Active'].sum()
        print("El número de casos activos en", ciudad, "es:", casos1)                        
    else:            
        print("Error in retriveing data selected") 
        
#%%Part 2: Retrieving Criminal Data from the Web
# #The goal will be to use official government data from the site:
# https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva

# Step 1: Read Crime CSV file

# The following csv is the current website file we are using.
# We will simply add a 'download' webscraping modality to read the most recent
# government csv file. 

######(look at simon munzert's code and try to add this for saturday)

csv_seg = 'idm_ago2020.csv'

# Step 2: Create a data frame from the csv file. 

df_seg = pd.read_csv(csv_seg, encoding='latin-1')

# Step 3: Create if-else statement to retrieve city-specific 
# crime information. 

# In the code below, we define an object to hold the if-else statement ("inseg_casos).
# We break the statement into two parts once again: one for the 14 cities in our list and one for
# Mexico City. Since the latter is the capital, it is recorded in an "entity" (entidad) 
# column and not in the "Municipio" column as it is for the 14 other cities. 

# We will need to retrive the Mexico City data with a different statement 
# ("elif" statement) than data for the the other cities ("if" statement).

#Moreover, we create a list of seven crimes that can be categorized as violent 
# and being of particular interest to tourist safety. These include Homicides,
# kidnappings, burglary, pickpocketing, femicide, and rape. 

#Step 4: Creating statements to retrive desired information 

# First, For the 14 cities in the first part, we explicitely retrieve data for the 14 
# cities, for the subtype of crime of interest, and recent data of 2019 and 2020.
# Second, we make a sum of this data for rows 9 to 21 of the csv file for the 12 months 
# of the year. Lastly, we turn this result into an integer. 

# Moreover, for Mexico City, we repeat this structure but retrive from the mexico city column. 

# Lastly, we will have an "else" statement as a backup in case there is a data retrieval error.
     
def inseg_casos(ciudad, delito):
    ciudades_seg = ['Mérida', 'Puerto Vallarta', 'Cancún', 'Guanajuato', 'Los Cabos', 'Acapulco de Juárez', 'San Miguel De Allende', 'Chapala', 'Puerto Escondido', 'Tijuana', 'Mazatlán', 'Puerto Peñasco', 'Puebla', 'Oaxaca de Juárez']
    delito = ['Homicidio doloso', 'Secuestro', 'Robo a casa habitación', 'Robo a transeúnte en vía pública', 'Feminicidio', 'Violación simple', 'Acoso sexual']
    if ciudad in ciudades_seg:
        municipios = pd.DataFrame(df_seg.loc[(df_seg['Municipio']== ciudad) & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
        suma = municipios.iloc[:,9:21].sum().sum().astype(int)
        print("El número de casos de",delito,"en",ciudad,"es",suma)
    elif ciudad == "Ciudad de México":
        cdmx = pd.DataFrame(df_seg.loc[(df_seg['Entidad']== 'Ciudad de México') & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
        suma1 = cdmx.iloc[:,9:21].sum().sum().astype(int)
        print("El número de casos de",delito,"en",ciudad,"es",suma1)
    else:            
        print("Error in retriveing data selected")    
        
        
#%% Part 3: Data validation checks

# We have a few codes to check the number of columns, sums, types of crime available,
# number of geographical entities, and years available in the data. 

df_seg.columns

df.isna().sum()

df_seg['Tipo de delito'].value_counts()

df_seg['Entidad'].value_counts()

df_seg['Año'].value_counts()



        
        

