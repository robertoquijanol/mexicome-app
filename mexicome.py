# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:36:00 2020

@author: rober
"""
import pandas as pd
import numpy as np

#%% info covid

csv = 'covid_mexico.csv'


df = pd.read_csv(csv, encoding ='latin-1')



df['Date'] = df['Date'].str.replace('/', '.')


def covid_casos(ciudad):
    ciudades = ['MÉRIDA', 'PUERTO VALLARTA', 'CANCÚN', 'GUANAJUATO', 'LOS CABOS', 'ACAPULCO', 'SAN MIGUEL DE ALLENDE', 'CHAPALA', 'PUERTO ESCONDIDO', 'TIJUANA', 'MAZATLÁN', 'PUERTO PEÑASCO', 'PUEBLA', 'OAXACA']
    if ciudad in ciudades:
        casos = df.loc[(df['Municipality'])==ciudad, 'Active'].sum()
        print("The number of active cases in", ciudad, "is:", casos)
    elif ciudad == 'CIUDAD DE MÉXICO':
        casos1 = df.loc[(df['State'])==ciudad, 'Active'].sum()
        print("The number of active cases in", ciudad, "is:", casos1)                        
    else:            
        print("Information not available for this city")
        
#%% info inseguridad

csv_seg = 'idm_ago2020.csv'

df_seg = pd.read_csv(csv_seg, encoding='latin-1')

     
def inseg_casos(ciudad, delito):
    ciudades_seg = ['Mérida', 'Puerto Vallarta', 'Cancún', 'Guanajuato', 'Los Cabos', 'Acapulco de Juárez', 'San Miguel De Allende', 'Chapala', 'Puerto Escondido', 'Tijuana', 'Mazatlán', 'Puerto Peñasco', 'Puebla', 'Oaxaca de Juárez']
    #delitos = ['Homicidio doloso', 'Secuestro', 'Robo a casa habitación', 'Robo a transeúnte en vía pública', 'Feminicidio', 'Violación simple', 'Acoso sexual']
    if ciudad in ciudades_seg:
        municipios = pd.DataFrame(df_seg.loc[(df_seg['Municipio']== ciudad) & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
        suma = municipios.iloc[:,9:21].sum().sum().astype(int)
        print("The number of cases of",delito,"in",ciudad,"is",suma)
    elif ciudad == "Ciudad de México":
        cdmx = pd.DataFrame(df_seg.loc[(df_seg['Entidad']== 'Ciudad de México') & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
        suma1 = cdmx.iloc[:,9:21].sum().sum().astype(int)
        print("The number of cases of",delito,"in",ciudad,"is",suma1)
        
        
        
#%% extra para checar info
        
df_seg.columns

df.isna().sum()

df_seg['Tipo de delito'].value_counts()

df_seg['Entidad'].value_counts()

df_seg['Año'].value_counts()

#%% RUN TO GET MEXICOME INFORMATION


input("Welcome to Mexicome! Press enter to continue: ")

ciudades = ['MÉRIDA', 'PUERTO VALLARTA', 'CANCÚN', 'GUANAJUATO', 'LOS CABOS', 'ACAPULCO', 'SAN MIGUEL DE ALLENDE', 'CHAPALA', 'PUERTO ESCONDIDO', 'TIJUANA', 'MAZATLÁN', 'PUERTO PEÑASCO', 'PUEBLA', 'OAXACA']


print("Top 15 destinations in Mexico:")

print(ciudades)

ciudad = input("Please choose your destination: ")

print(ciudad)

covid_casos(ciudad)

input("Press enter to continue for criminality information: ")

print("Top 15 destinations in Mexico:")

ciudades_seg = ['Mérida', 'Puerto Vallarta', 'Cancún', 'Guanajuato', 'Los Cabos', 'Acapulco de Juárez', 'San Miguel De Allende', 'Chapala', 'Puerto Escondido', 'Tijuana', 'Mazatlán', 'Puerto Peñasco', 'Puebla', 'Oaxaca de Juárez']

print(ciudades_seg)

ciudad = input("Please enter destination: ")

print("List of crimes:")
delitos = ['Homicide', 'Kidnapping', 'House burglary', 'Car robbery', 'Feminicide', 'Rape', 'Sexual harassment']

print(delitos)


delito = input("Plese enter specific crime: ")

inseg_casos(ciudad, delito)
#%%
