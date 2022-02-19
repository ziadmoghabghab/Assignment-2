
import streamlit as st
import pandas as pd
import numpy as np

button1 = st.sidebar.button("Life Expectancy and BMI")
button2 = st.sidebar.button("Life Around The World")
button3 = st.sidebar.button("Histogram of Deaths Under 5 and Alcohol")
button4 = st.sidebar.button("Population of Developed And Undeveloped Coutnries")

st.title("MSBA 325 Assignment 2")
st.header("Ziad Moghabghab")
st.header("ID: 202224793")

df = pd.read_csv('https://raw.githubusercontent.com/ziadmoghabghab/Assignment-2/msba325/Life%20Expectancy%20Data.csv')
import plotly.express as px

adult_mortality_mean=df['Adult Mortality'].mean()
df['Adult Mortality'].fillna(adult_mortality_mean, inplace=True)


figure1 = px.scatter(df, x=' BMI ', y='Life expectancy ', animation_frame='Year' , animation_group = 'Country', size='Adult Mortality', color='Status', hover_name='Country', range_y=[0,100])
if st.checkbox('Show Life Expectancy vs BMI'):
    st.subheader('Life Expectancy vs BMI')
    st.write(figure1)
    st.audio('https://raw.githubusercontent.com/ziadmoghabghab/Assignment-2/msba325/Recording1.m4a')


adult_mortality_mean=df['Adult Mortality'].mean()
df['Adult Mortality'].fillna(adult_mortality_mean, inplace=True)

lifeexp_mean=df['Life expectancy '].mean()
df['Life expectancy '].fillna(lifeexp_mean, inplace=True)


figure2 = px.choropleth(df, locations='Country',color='Life expectancy ', animation_frame='Year' ,color_continuous_scale=px.colors.sequential.Plasma , hover_name='Country')
if st.checkbox('Show Life Expectancy Around The World'):
    st.subheader('Life Expectancy Around The World')
    st.write(figure2)
    st.audio('https://raw.githubusercontent.com/ziadmoghabghab/Assignment-2/msba325/Recording2.m4a')

adult_mortality_mean=df['Adult Mortality'].mean()
df['Adult Mortality'].fillna(adult_mortality_mean, inplace=True)

lifeexp_mean=df['Life expectancy '].mean()
df['Life expectancy '].fillna(lifeexp_mean, inplace=True)


figure3 =px.histogram(df,y='under-five deaths ', x='Alcohol', color='Status', range_x=[6,14], range_y=[0,10000])
if st.checkbox('Show Relation Between Deaths Of Children Under 5 And Alcohol'):
    st.subheader('Relation Between Deaths Of Children Under 5 And Alcohol')
    st.write(figure3)
    st.audio('https://raw.githubusercontent.com/ziadmoghabghab/Assignment-2/msba325/Recording3.m4a')

adult_mortality_mean=df['Adult Mortality'].mean()
df['Adult Mortality'].fillna(adult_mortality_mean, inplace=True)

lifeexp_mean=df['Life expectancy '].mean()
df['Life expectancy '].fillna(lifeexp_mean, inplace=True)


figure4 = px.bar(df,x='Status', y='Population', color='Status', animation_frame='Year', hover_name='Country', range_y=[0, 4000000000])
if st.checkbox('Show Population Of Developed And Undeveloped Coutnries Over Time'):
    st.subheader('Population Of Developed And Undeveloped Coutnries Over Time')
    st.write(figure4)
    st.audio('https://raw.githubusercontent.com/ziadmoghabghab/Assignment-2/msba325/Recording4.m4a')
