# -*- coding: utf-8 -*-

#%% Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import pytz
import datetime as dt

#%% Post-processing
'''
Just some additional code lines to calculate useful indicators and generate plots
'''
def Profile_formatting(stoch_profiles):
    Profile_avg = np.zeros(1440)
    for pr in stoch_profiles:
        Profile_avg = Profile_avg + pr
    Profile_avg = Profile_avg/len(stoch_profiles)
    
    Profile_kW = []
    for kW in stoch_profiles:
        Profile_kW.append(kW/1000)
    
    Profile_series = np.array([])
    for iii in stoch_profiles:
        Profile_series = np.append(Profile_series,iii)
    
    return (Profile_avg, Profile_kW, Profile_series)

def Profile_cloud_plot(stoch_profiles,stoch_profiles_avg):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    for n in stoch_profiles:
        plt.plot(np.arange(1440),n,'#b0c4de')
        plt.xlabel('Time (hours)')
        plt.ylabel('Power (W)')
        plt.ylim(ymin=0)
        #plt.ylim(ymax=5000)
        plt.margins(x=0)
        plt.margins(y=0)
    plt.plot(np.arange(1440),stoch_profiles_avg,'#4169e1')
    plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()


def Profile_series_plot(stoch_profiles_series):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    plt.plot(np.arange(len(stoch_profiles_series)),stoch_profiles_series,'#4169e1')
    #plt.xlabel('Time (hours)')
    plt.ylabel('Power (W)')
    plt.ylim(ymin=0)
    #plt.ylim(ymax=5000)
    plt.margins(x=0)
    plt.margins(y=0)
    #plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()

def Profile_dataframe(Profiles_series, year):
    
    minutes = pd.date_range(start=str(year) + '-01-01', periods = len(Profiles_series), freq='T')
    
    if Profiles_series.ndim == 1:
        Profiles_df = pd.DataFrame(Profiles_series, columns = ['Cooking Profile'])
    else: 
        Profiles_df = pd.DataFrame(Profiles_series)   
    
    Profiles_df.set_index(minutes, inplace = True)
   
    return Profiles_df

def Time_correction(df, country, year):
    
    df_c = copy.deepcopy(df)   
    
    if country == 'EL':
        country = 'GR'
    if country == 'UK':
        country = 'GB'
        
    ind = df_c.index.tz_localize(pytz.country_timezones[country][0], nonexistent = 'NaT', ambiguous='NaT')
    
    ind_utc = ind.tz_convert('utc')
    temp_utc = df_c.set_index(ind_utc)
    
    ind_year = pd.date_range(start=str(year) + '-01-01', end=str(max(temp_utc.index).date()) + ' 23:59:00', freq = ind.to_series().diff().min(), tz = 'utc')
    temp_year = pd.DataFrame([np.nan] * len(ind_year), index = ind_year)
    
    df_utc_final = temp_utc.join(temp_year, how='outer')
    df_utc_final = df_utc_final.dropna(axis=1, how='all')
    df_utc_final = df_utc_final.loc[df_utc_final.index.notnull()]
    df_utc_final = df_utc_final.ffill()
    df_utc_final = df_utc_final[df_utc_final.index >= str(year) + '-01-01']
    
    df_utc_final = pd.DataFrame(df_utc_final)
    
    return df_utc_final

#%% Export individual profiles
'''
for i in range (len(Profile)):
    np.save('p0%d.npy' % (i), Profile[i])
'''

# Export Profiles

def export_series(stoch_profiles_series, country):
    series_frame = pd.DataFrame(stoch_profiles_series)
    series_frame.to_csv('results/output_file_%s.csv' % (country))