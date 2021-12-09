import streamlit as st
import pandas as pd
def foo_bar(x):
    return x['buyLink']
form = st.form(key='my_form')
text_input = label='Enter some text'
submit_button = form.form_submit_button(label='Submit')
form = st.form(key='my-form')
text_input = form.text_input('Enter your name')
submit = form.form_submit_button('Submit')
if submit:
    import urllib.request, json 
    with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q="+str(text_input.replace(" ","+"))) as url:
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