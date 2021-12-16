import streamlit as st
import sympy
x, y, z = symbols('x y z')
st.write(sympy.diff(2*x**2, x))
