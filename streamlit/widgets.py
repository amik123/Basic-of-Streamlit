import streamlit as st
import pandas as pd

st.title("Text input tutorial")

#two things are happening name is saved to 'name' variable and the text input is displayed in web page
name=st.text_input('Enter your name:')

age=st.slider("Enter your age",0,100,24)
st.write(f"You selected your age as {age}")

options=['Java','Python','C++','dotnet']
choice=st.selectbox('Choose your fav language',options)

st.write(f"Your favourite programming language is {choice}")


if name:
    st.write(f'HELLO {name}!!')

data={'name':['Kamal','Bishal','Amik'],
      'Salary':[50000,250000,65000],
      'age':[25,24,24]}

df=pd.DataFrame(data)
df.to_csv('sampledata.csv')
uploaded_file=st.file_uploader('Choose a csv file',type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

