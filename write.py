import pandas as pd
import numpy as np
import nltk
import streamlit as st

def writeData(csvDocument, column1, column2):
     
    for index, row in data.iterrows():
        if (pd.isna(row[1])):
            print("Word index: " + str(index))
            print("Word: " + row[0]) # row of 0 is equivilent to row named 'orthography'
            transcript = input("Please enter IPA transcription for the above row")
            if transcript == "exit": # exit code out of the loop
                break
            else:
                data.loc[index, column2] = transcript
                # super helpful important link about copies and views in pandas:
                # (came from an error message)
                # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
                data.to_csv(csvDocument, index=False) # write to the file every time
                
        else:
            continue # if it already has a value, no need to rewrite!
        

csvString = st.text_input("Please enter the name of the .csv file (include '.csv' in the string): ")

if csvString:
    df = pd.read_csv('firstHundred.csv')

    st.write("Here is your data so far: ")
    st.write(df)

column0 = st.text_input("Please enter the name of the first (furthest left) column: ")

column1 = st.text_input("Please enter the name of the second (second to furthest left) column: ")
        

st.title("Write IPA transcriptions to dev training set!!")



