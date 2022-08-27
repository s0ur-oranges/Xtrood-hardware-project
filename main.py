# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st
import time

x = np.array([2, 2.1, 2.2, 2.3, 2.4, 2.5]).reshape((-1, 1))
y = np.array([4.2, 5, 5.3, 5.7, 6, 6.9])

model = LinearRegression()
model.fit(x , y)


def extrude(nozzle):
    a= model.predict(nozzle)

    return a


def progressbar():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)


st.title('Xtrood App')
st.write('Finding the optimal strip width for you')

st.sidebar.subheader("Enter a single value (nozzle diameter) : ")
text = st.sidebar.text_area("Enter a value between 2 to 3 in place of the default value..",
                              value=2.3 ,
                              height=500, max_chars=None, key=None)

arr=np.array([text]).reshape(-1 , 1)

if (st.sidebar.button('Enter')):
    progressbar()
    
    if nozzle<1.5 or nozzle>3.5:
        st.write("Please enter a value between 2 and 3")
                 
    else:
        result=np.round(extrude(arr)[0] , 2)
        st.write(result)
