# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.tree import DecisionTreeRegressor
import streamlit as st
import pandas as pd
from urllib.request import urlopen
import requests
def foo_bar(x):
    return x['buyLink']
def prices(dictionary):
    listPrices = []
    retailPrices = []
    for i in dictionary:
        saleinfo = i['saleInfo']
        if (saleinfo['saleability'] == "FOR_SALE"):
            listPrice = saleinfo['listPrice']
            retailPrice = saleinfo['retailPrice']
            listPrices.append(listPrice['amount'])
            retailPrices.append(retailPrice['amount'])
    df = pd.DataFrame({"list price":listPrices,"retail price":retailPrices})
    regr = DecisionTreeRegressor()
    regr.fit(df[['list price']], df['retail price'])
    st.write(regr.predict([10]))
    st.line_chart(df)
form = st.form(key='my_form')
text_input = label='Enter some text'
submit_button = form.form_submit_button(label='Submit')
form = st.form(key='my-form')
text_input = form.text_input('Enter your name')
submit = form.form_submit_button('Submit')
site = "https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC"
print(requests.get("https://www.googleapis.com/books/v1/volumes?key=AIzaSyCYKIKheo-kxVkwr8Aq3468SbhIfXm_-C4&q=search+terms"))
if submit:
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + text_input.replace(" ","+")+ "&key=AIzaSyCYKIKheo-kxVkwr8Aq3468SbhIfXm_-C4&country=US")
    response_json = response.json()
    #df = pd.DataFrame.from_dict(reponse_json)
    items = response_json['items']
    prices(items)
'''
if submit:
    import urllib.request, json 
    with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=kappa") as url:
        data = json.loads(url.read().decode())
        df = pd.DataFrame.from_dict(pd.DataFrame.from_dict(data['items']))
        df = df[['saleInfo']]
        #st.write(pd.DataFrame.from_dict(df, orient="index"))
        country = ['US']*10
        lp = []
        rp = []
        for i in range(len(df['saleInfo'])):
            if 'listPrice' in df['saleInfo'].iloc[i].keys():
                lp.append(df['saleInfo'].iloc[0]['listPrice']['amount'])
            else:
                lp.append(74 + i)
        for i in range(len(df['saleInfo'])):
            if 'retailPrice' in df['saleInfo'].iloc[i].keys():
                rp.append(df['saleInfo'].iloc[0]['retailPrice']['amount'])
            else:
                rp.append(74 + i)
            #st.write(pd.DataFrame.from_dict(i, orient="index"))
        df['country'] = pd.Series(country).transpose()
        df['listPrice'] = pd.Series(lp)
        df['retailPrice'] = pd.Series(rp)
        st.line_chart(df[['listPrice','retailPrice']])
'''
