import streamlit as st

# Image pkgs
from PIL import Image


# load image
img = Image.open("hair.jpg")

st.image(img, use_column_width=True)

st.sidebar.markdown("#")

st.write("""
		 I'm just a data scientist who wishes he still had hair....

		""")

st.write("[Email](election.app.boogaloo@gmail.com)")