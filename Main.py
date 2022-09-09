import streamlit as st

# Image pkgs
from PIL import Image


# load image
img = Image.open("valvaka22.jpg")

st.image(img, use_column_width=True)

st.sidebar.markdown("# It's time to choose a new dear leader 🇸🇪 ")

st.write("""
		### This is a Exploratory Data Analysis App for Political Parties 2022.
		I've refrained from offering my interpretation of the analysis and instead opted to give the reader
		the tools to interpret the results themselves. Politics can be contensious and I just really like
		the math behind correspondence analysis and wanted to apply it to something that people care about and of course above all I did it for the fame and glory. 

		The colors I choose for the plots were chosen for interpretibility and their visual appeal (I wanted to make it look good and simple I tried giving each party it's own color but it looked to messy)
		
		[Comments and Criticisms](election.app.boogaloo@gmail.com) are more than welcome, I just started this project this week and have had to rush
		it to launch it before the weekend, so it's a work in progress. 
		#### Datasource
		- https://www.scb.se/publikation/47473
		#### App Content
		EDA Section: Correspondence Analysis and Pie charts for 9 categories of political
		parties by age, sex, and sociodemographic factors and aggregate.

		About Section: Contact and Information about me.
		""")
