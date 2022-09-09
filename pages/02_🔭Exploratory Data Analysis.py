# core packages
import streamlit as st
#overflow: hideScrollbar ? "hidden" : "auto",

## Additional Packages
import pandas as pd
import numpy as np
from scipy import linalg
from scipy.sparse.linalg import inv
from scipy.sparse import csc_matrix
from sklearn import utils
from ca import ca

## Data Viz Packages
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.express as px
from plots import plot
from plots import pie
from plots import make_labels_and_names

# Load data
## Load Data
@st.cache
def load_data(data):
	dt = pd.read_pickle(data)
	return dt

## load all the data
dt_age_men = load_data("dt_age_men.pkl")
dt_age_women = load_data("dt_age_women.pkl")
dt_region_men = load_data("dt_region_men.pkl")
dt_region_women = load_data("dt_region_men.pkl")
dt_countryofbirth_men = load_data("dt_countryofbirth_men.pkl")
dt_countryofbirth_women = load_data("dt_countryofbirth_women.pkl")
dt_ethinicity_men = load_data("dt_ethnicity_men.pkl")
dt_ethnicity_women = load_data("dt_ethnicity_women.pkl")
dt_education_men = load_data("dt_education_men.pkl")
dt_education_women = load_data("dt_education_women.pkl")
dt_children_men = load_data("dt_children_men.pkl")
dt_children_women = load_data("dt_children_women.pkl")
dt_civil_men = load_data("dt_civilstatus_men.pkl")
dt_civil_women = load_data("dt_civilstatus_women.pkl")
dt_housing_men = load_data("dt_housing_men.pkl")
dt_housing_women = load_data("dt_housing_women.pkl")
dt_employment_men = load_data("dt_employment_men.pkl")
dt_employment_women = load_data("dt_employment_women.pkl")
dt_income_men = load_data("dt_income_men.pkl")
dt_income_women = load_data("dt_income_women.pkl")
dt_occupation_class = load_data("dt_occupational_class.pkl")
dt_sector = load_data("dt_sector.pkl")
dt_sectorn_2 = load_data("dt_sector_2.pkl")
dt_union = load_data("dt_union.pkl")
dt_ses_group = load_data("dt_ses_group.pkl")
dt_ses_group_emp = load_data("dt_ses_group_employed.pkl")


## Stacked table
dt_age = dt_age_men + dt_age_women
dt_region = dt_region_men + dt_region_women
dt_countryofbirth = dt_countryofbirth_men + dt_countryofbirth_women
dt_ethinicity = dt_ethinicity_men + dt_ethnicity_women
dt_education = dt_education_men + dt_education_women
dt_children = dt_children_men + dt_children_women
dt_civil = dt_civil_men + dt_civil_women
dt_housing = dt_housing_men + dt_housing_women
dt_employment = dt_employment_men + dt_employment_women
dt_income = dt_income_men + dt_income_women

dt_all = pd.concat([dt_age, dt_region, dt_countryofbirth, dt_ethinicity,
	dt_education, dt_children, dt_civil, dt_housing, dt_employment,
	dt_income, dt_occupation_class, dt_sector, dt_union, dt_ses_group])

def make_labels_and_names(X):

    if isinstance(X, pd.DataFrame):
        row_label = X.index.name if X.index.name else 'Rows'
        row_names = X.index.tolist()
        col_label = X.columns.name if X.columns.name else 'Columns'
        col_names = X.columns.tolist()
    else:
        row_label = 'Rows'
        row_names = list(range(X.shape[0]))
        col_label = 'Columns'
        col_names = list(range(X.shape[1]))

    return row_label, row_names, col_label, col_names
# data dict

data_dict_3 = {"Age": [dt_age_men, dt_age_women],
"Region" : [dt_region_men, dt_region_women],
"Country of Birth": [dt_countryofbirth_men, dt_countryofbirth_women],
"Ethnicity": [dt_ethinicity_men, dt_ethnicity_women],
"Civil Status": [dt_civil_men, dt_civil_women],
"Children": [dt_children_men, dt_children_women],
"Income": [dt_income_men, dt_income_women],
"Education": [dt_education_men, dt_education_women],
"Housing": [dt_housing_men, dt_housing_women],
"Employment": [dt_employment_men, dt_employment_women]}

data_dict_1 = {"Socioeconomic Status": dt_ses_group,
"Market Sector": dt_sector,
"Union": dt_union,
"Occupational Classification": dt_occupation_class}
# functions



submenu = st.sidebar.selectbox(" Categories", ["About","Age", 
	"Region", "Country of Birth",
	"Ethnicity", "Civil Status",
	"Children", "Income", "Education",
	"Housing", "Employment", "Socioeconomic Status",
	"Market Sector", "Union", "Occupational Classification",
	"All"])

one_group = ["Socioeconomic Status",
	"Market Sector", "Union", "Occupational Classification",]

three_group = ["Age", 
	"Region", "Country of Birth",
	"Ethnicity", "Civil Status",
	"Children", "Income", "Education",
	"Housing", "Employment",]

all_group = "All"

ca_interpretation = """ 
					- Points that lie close to eachother indicate some form of similarity
					- Points that lie far from one and other indicate some form of difference. You can usually draw interesting conclusions looking at the extreme points on the axis but also on the diagonals of the plot
					- A row and column profile are probably negatively associated if they are on opposite sides of the origin 
					- The further a point from the origin, the stronger their positive or negative association
					- Remember you can expand the plot, download it as a .png, and zoom in and out to get a better view of the plot by clicking the toolbar in the upper right corner of the plot!
					"""

pie_interpretation = """Some people hate on pie charts, especially epidemiologists, 
					they claim bar charts are superior and pie charts are hard to read,
					I like pie charts, and for this data they are perfect and visually pleasing. These
					pie charts just show the proportion of respondents for each political party that the Correspondence Analysis above was based on.
					"""

if submenu == "About":
	st.write("""
	### What is Correspondence Analysis?
	At its core Correspondence Analysis is a method of data analysis for representing tabular data graphically. It's really just a generalization of a scatterplot, but like all generalizations the devil
	is in the details (which is an oxymoron). 

	My intention is to avoid getting lost in simplexes, barycentric properties, conditional probabilities, singular value decomposition, intertia, and chi-squared distances all of which lay at the heart of CA. 
	
	Instead, I just want to present to you a method to represent data in a way that allows for interesting and sometimes hidden and useful interpretations.

	### How to use this app?
	Click on the sidebar and choose the factor you would like to see political sympathies measured on. 
	For most of the factors you can choose to view the analysis by sex or combined. 

	All the figures are interactive! Meaning you can zoom in on them and choose to add or remove rows and columns! 
	For every figure there's an interpretation aid that you can use to help you interpret the plot and draw conclusions!
	
	This is a WIP, so please let me know of any [bugs](election.app.boogaloo@gmail.com)

	##### References and resources for the curious:
	- All you'll ever need is wikipedia: https://en.wikipedia.org/wiki/Correspondence_analysis
	- Big shout out to an OG of CA Francois Husson who wrote one of my favorite books on the subject: https://www.amazon.com/Francois-Sebastien-PagessExploratory-Multivariate-Hardcover/dp/B0051N9DAO 
	- Francois also has a youtube channel with video lectures, hes got a thick accent but the French invented CA so it's the only appropriate way to learn it: https://www.youtube.com/c/HussonFrancois

	""")



for i in three_group:

	if submenu == i:

		submenu = st.sidebar.radio("(by sex)",["Men 🤴", "Women 👸", "Men & Women 👫"])
		if submenu == "Men 🤴":
			dt = data_dict_3[i][0]
			A, B, cp_dt = ca(dt)
			_, row_names, _, col_names = make_labels_and_names(cp_dt)
			with st.expander("Interpretation Tool for Correspondence Analysis"):
				st.write(ca_interpretation)
			fig = plot(A,B,row_names,col_names)
			st.plotly_chart(fig)
			with st.expander("Interpretation Tool for Pie Chart"):
				st.write(pie_interpretation)

			fig = pie(dt)
			st.plotly_chart(fig)
		if submenu == "Women 👸":
			dt = data_dict_3[i][1]
			A, B, cp_dt = ca(dt)
			_, row_names, _, col_names = make_labels_and_names(cp_dt)
			with st.expander("Interpretation Tool for Correspondence Analysis"):
				st.write(ca_interpretation)
			fig = plot(A,B,row_names,col_names)
			
			st.plotly_chart(fig)
			with st.expander("Interpretation Tool for Pie Chart"):
				st.write(pie_interpretation)
			fig = pie(dt)
			st.plotly_chart(fig)

		elif submenu == "Men & Women 👫":
			dt = data_dict_3[i][0]
			dt2 = data_dict_3[i][1]
			dt_tot = dt + dt2
			A, B, cp_dt = ca(dt_tot)
			_, row_names, _, col_names = make_labels_and_names(cp_dt)
			with st.expander("Interpretation Tool for Correspondence Analysis"):
				st.write(ca_interpretation)


			fig = plot(A,B,row_names,col_names)
			st.plotly_chart(fig)
			with st.expander("Interpretation Tool for Pie Chart"):
				st.write(pie_interpretation)
			fig = pie(dt)
			st.plotly_chart(fig)

for j in one_group:

	if submenu == j:

		dt = data_dict_1[j]
		A, B, cp_dt = ca(dt)
		_, row_names, _, col_names = make_labels_and_names(cp_dt)
		with st.expander("Interpretation Tool for Correspondence Analysis"):
				st.write(ca_interpretation)

		fig = plot(A,B,row_names,col_names)
		st.plotly_chart(fig)
		with st.expander("Interpretation Tool for Pie Chart"):
			st.write(pie_interpretation)
		fig = pie(dt)
		st.plotly_chart(fig)

if submenu == "All":
	A, B, cp_dt = ca(dt_all)
	_, row_names, _, col_names = make_labels_and_names(cp_dt)
	with st.expander("Interpretation Tool for Correspondence Analysis"):
				st.write(ca_interpretation)
	fig = plot(A,B,row_names,col_names,row_markers='markers', col_markers='markers+text')
	st.plotly_chart(fig)

	fig = pie(dt_all)
	with st.expander("Interpretation Tool for Pie Chart"):
		st.write(pie_interpretation)
	st.plotly_chart(fig)