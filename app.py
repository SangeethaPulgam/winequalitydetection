import streamlit as st
import joblib
model=joblib.load('wine-quality')
st.title('WINE QUALITY DETECTION')
ip=st.text_input('enter the type')
op=model.predict([ip])
if st.button('predict'):
     st.title(op[0])


