import streamlit as st
from sympy import diff,symbols
x, y, z = symbols('x y z')
print(diff(2*x**2, x))
