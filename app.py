import streamlit as st
string = "Find largest among 3 given numbers"
st.set_page_config(page_title=string, page_icon="⚖️")

st.title('Find largest among 3 given numbers')
a = st.number_input('Enter first number ')
b = st.number_input('Enter Second number ')
c = st.number_input('Enter Third number ')

if a > b and a > c:
 st.write( str(a)+ " is largest no")
if b > a and b > c:
    st.write(str(b)+" is largest no")
if c > a and c > b:
    st.write(str(c)+ " is largest no")
