import streamlit as st
from sympy import *
x, y, z = Symbols('x y z')
st.write(diff(2*x**2, x))
