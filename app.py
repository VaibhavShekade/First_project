import streamlit as st

st.title("Innomatics Data App")

st.subheader("Rice Production")

socials  = ["LinkedIn", "Github", "GMail"]
linkedin = "https://www.linkedin.com/in/vaibhav-shekade-a78bb11ba/"
github   = "https://github.com/VaibhavShekade"
mail     = "shekadevaibhav2002@gmail.com"

with st.expander(label='Check my Socials Links',expanded=True):
	a = st.selectbox("Socials", socials)
	if a =="LinkedIn":
		st.write(linkedin)
	elif a =="Github":
		st.write(github)
	elif a=="GMail":
		st.write(mail)