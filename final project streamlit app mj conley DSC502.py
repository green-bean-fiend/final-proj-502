import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Chlamydia')
dfc1 = pd.read_csv("C:\Users\User\Documents\df1c.csv")

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(dfc1)

cols = ['Indicator','Year','Geography','Pop','PopDenEST','Cases','Rate per 100000','Abst']


df00=(df1c.loc[df1c['Abst'] == 0])
df11=(df1c.loc[df1c['Abst'] == 1])

st.markdown('---')
st.subheader('\nSelectbox')
option = st.selectbox(
    'Select Sexual Education Status',
    ('Abstinence- Only', 'NonAbstinence- Only'))
st.write('You selected:', option)
if option == 'Abstinence- Only'
    cases= df11['Rate per 100000']
    state= df11['Geography']
    fig = plt.figure(figsize =(10, 7))
    plt.barh(state, cases)
    plt.title("Cases of Chlamydia by State, Abstinence- Only")
    plt.xlabel('Rate of Cases Per 100,000')
    plt.show()
    
else:
    cases= df00['Rate per 100000']
    state= df00['Geography']
    fig = plt.figure(figsize =(10, 7))
    plt.barh(state, cases)
    plt.title("Cases of Chlamydia by State, Non- Abstinence- Only")
    plt.xlabel('Rate of Cases Per 100,000')
    plt.show()


