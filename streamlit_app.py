import streamlit as st
import numpy as np
import pandas as pd
import pickle
import time
#from matplotlib import pyplot as plt
#from matplotlib.ticker import Funcformatter
#import seaborn as sns

st.set_page_config(layout="wide")

#df_database = pd.read_csv("./data/outputCSV.csv")

####################
### INTRODUCTION ###
####################

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Caldomus')
with row0_2:
    st.text("")
    st.subheader('Interactieve web interface door [Innoforte](https://www.innoforte.nl)')
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("In deze web applicatie is het mogelijk om te bekijken wat de impact is van isolatie en renovatie voor uw gasverbruik, elektraverbruik2, co2 uitstoot én uw portemonnee")
    st.markdown("Elon")
    st.markdown("^^^^^^^")
