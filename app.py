

import streamlit as st
string = "Find largest among 3 given numbers"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Find largest among 3 given numbers')
a = int(st.number_input('Enter first number '))
b = int(st.number_input('Enter Second number '))
c = int(st.number_input('Enter Third number '))

  if a > b and a > c:
    largest = a:st.write("A is larger no")
 
  if b > a and b > c:
    largest = b:st.write("B is larger no")
 
   if c > a and c > b:
    largest = c:st.write("C is larger no")
    
