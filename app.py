import streamlit as st
import joblib
model_nb=joblib.load('vect')
st.title('WINE QUALITY DETECTION')
ip=st.text_input("enter the type:")
op=model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
