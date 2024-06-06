# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Tunakaribisha Mabingwa kwa Mbio Za Mamilii hapa Camp Toyoyo. 
        
         """)

msgs = ['Karibu Ndakas, leo unakaa best. Tuishie pale mbele tutulie kama mabingwa',
        'Karibu sana Shine Kenya ni Tifi sana kukucheki, endelea kupiga hustle yako safi, sisi wote tukue mabingwa!',
        'Nacheki luku ni diriba, hustle pia imekubali. Muokalize tushine ka mabingwa' ]


f_name = st.text_input('Andika Jina')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name + " " + msg)
