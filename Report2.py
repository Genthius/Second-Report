# -*- coding: utf-8 -*-
"""
Created on Tue Dec 6 21:04:02 2022

@author: gm17abn
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def read_file(file_name):
    """
Reads from file and returns two dataframes.

    """
    df = pd.read_excel(file_name,sheet_name="Data",header=3)
    
    df.dropna(how="all", axis=1, inplace=True)
    
    df = df.drop(columns = ["Country Code","Indicator Name","Indicator Code"])
    
    df_t = df.set_index("Country Name").T
    
    return df, df_t

def line(df,labels):
    """
    
    Produces a line graph with the countries specified
    
    """

    countries = ["Germany","Albania","Japan",
                 "Qatar"]
    
    start_year = 1961
    end_year = 2020
    x_numbers = np.arange(start_year,end_year+1,5)
    x_number_str = []
    for i in x_numbers:
        x_number_str.append(str(i))
    plt.figure()
    plt.plot(df[countries],label=countries)
    plt.xlim(str(start_year),str(end_year+1))
    plt.xticks(x_number_str)
    
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.grid()
    plt.legend()
    
    now = datetime.now()
    now_str = now.strftime("%d-%m-%Y_%H-%M-%S")
    name = "line_graph_" + now_str + ".png"
    plt.savefig(name,bbox_inches="tight")
    plt.show()

def bar(df,labels):
    """
    
    Produces a bar chart with the countries specified
    """
    
    decades = [1990,2000,2010]
    str_decades = []
    for i in decades:
        str_decades.append(str(i))
    
    plt.figure(figsize=[24,15])
    bar_width = 1
    
    plt.bar([1990-3,2000-3,2010-3],
            df["United Kingdom"].loc[str_decades],
            label="United Kingdom",width=bar_width)
    plt.bar([1990-2,2000-2,2010-2],
            df["Albania"].loc[str_decades],
            label="Albania",width=bar_width)
    plt.bar([1990-1,2000-1,2010-1],
            df["Qatar"].loc[str_decades],
            label="Qatar",width=bar_width)
    plt.bar([1990,2000,2010],
            df["France"].loc[str_decades],
            label="France",width=bar_width)
    plt.bar([1990+1,2000+1,2010+1],
            df["Japan"].loc[str_decades],
            label="Japan",width=bar_width)
    plt.bar([1990+2,2000+2,2010+2],
            df["Germany"].loc[str_decades],
            label="Germany",width=bar_width)
    
    plt.xticks(decades)
    plt.legend(prop={'size': 15})
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    now = datetime.now()
    now_str = now.strftime("%d-%m-%Y_%H-%M-%S")
    name = "bar_chart_" + now_str + ".png"
    plt.savefig(name,bbox_inches="tight")
    plt.show()

def heat_map(country, df_1,df_2,df_3,df_4, labels):
    """

    Produces a heatmap with the countries specified
    """
    dfs = [df_1[country],df_2[country],df_3[country],df_4[country]]


    main_df = pd.concat(dfs,axis=1,join="inner")
    main_df.columns.values[0:4] = labels
    
    main_df = main_df.corr(method="pearson")


    fig, ax = plt.subplots(figsize=(len(labels),len(labels)))
    im = ax.imshow(main_df, interpolation='nearest')
    
    fig.colorbar(im, orientation='vertical', fraction = 0.05)
    
    
    plt.title(country)
    
    ax.set_xticks([0,1,2,3], labels=labels)
    ax.set_xticklabels(labels,rotation=35,ha="right",
                       rotation_mode="anchor")
    ax.set_yticks([0,1,2,3], labels=labels)
    
    for i in range(4):
        for j in range(4):
            ax.text(j, i, round(main_df.to_numpy()[i, j], 2),
                    ha="center", va="center", color="black")
    now = datetime.now()
    now_str = now.strftime("%d-%m-%Y_%H-%M-%S")
    name = "heat_map_" + now_str + ".png"
    plt.savefig(name,bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    gdp_df, gdp_df_t = read_file("GDPPERCAP.xlsx")
    pop_df, pop_df_t = read_file("Population growth.xlsx")
    for_df, for_df_t = read_file("Forest Area.xlsx")
    green_df,green_df_t = read_file("Greenhouse gases.xlsx")
    growth_df, growth_df_t = read_file("GDP growth.xlsx")
    pop_growth_df, pop_growth_df_t = read_file("Population Growth.xlsx")
    

    line(pop_df_t,["Year","Population Growth"])
    line(growth_df_t,["Year","GDP Change %"])
    
    heat_map("Albania",green_df_t,gdp_df_t,pop_df_t,for_df_t,
            ["Greenhouse gases","GDP Per Capita",
             "Population Growth","Forest Area"])
    heat_map("Germany",green_df_t,gdp_df_t,pop_df_t,for_df_t,
            ["Greenhouse gases","GDP Per Capita",
            "Population Growth","Forest Area"])

    bar(gdp_df_t,["Year","GDP per Capita"])
    bar(green_df_t,["Year","Greenhouse Gases"])
           
    
