from pathlib import Path

import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cvamg.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | AMG"
PAGE_ICON = ":wave:"
NAME = "Alejandro Mendoza"
DESCRIPTION = """
Data Engineer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "aaamendoza@gmail.com"
SOCIAL_MEDIA = {
    # "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com/in/AlejandroMendozaGzz"
    # "GitHub": "https://github.com",
    # "Twitter": "https://twitter.com",
}
# PROJECTS = {
#    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
#}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON) 
#,layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.header(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("About me")
st.write(
    """
Hello! Thank you for taking the time to review my information. I am currently working in the area of data engineering as well as in data analysis, 
for this, I use tools such as Python as a programming language and Snowflake as a database. For data analysis in Python I like to use pandas dataframes, 
plotly and Snowpark, as well as different components from both Python and Snowflake. I have tested ML models with Snowflake Cortex functions. 
I have uploaded data to Snowflake using Python. As well as developed a price web scrapping process in Python. 
If you think I can help you with any project you have in mind, do not hesitate to contact me.
"""
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Powershell
- ✔️ Knowledge and experience in business processes
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- ✔️ Programming: Streamlit, Access Login and SignUp (Streamlit-Authenticator), Plotly Graps (Bar, Line, Pie, Sunburst) Combine filters in a Streamlit app (checkbox, sliders, multiselects with expander) to dynamically generate the content of a graph or table (dataframe or AG Table). 
- ✔️ Programming: Python (Pandas, AG Grid), SQL, Powershell
- ✔️ Data Visulization: Plotly, BusinessObjects, PowerBi
- ✔️ Modeling: Snowflake Cortex Function for ML, Linear regression
- ✔️ Databases: Snowflake, Teradata, SQLServer
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("- ▶", "**Data Engineer | Grainger México**")
st.write(" 07/2002 - Present")
st.write(
    """
- ● Construction of a process in Python to load data into Snowflake.
- ● Construction of Web Scraping prototype for prices in Python.
- ● Construction of an ETL tool in PowerShell that pulls information from Teradata, \t SQLServer and Excel Files in Sharepoint OnLine.
- ● Creation of star data model for consumption in PowerBI for Sales, Inventory and product shipped not invoiced (AR) areas.
- ● Participation in data migration to SAP with Grainger USA team.

"""
)
st.write("")

# --- JOB 2
st.write("- ▶", "**Prepaid Project Leader | Cedetel Telefónica**")
st.write(" 11/1997 - 10/2001")
st.write(
    """
- ● Participation in the implementation of the Sixbell Prepaid system
- ● Operation, maintenance and development of the Cedetel system such as: year 2000 adjustments, Caller Pays (CPP) mode, interfaces with telephonic central.

"""
)
st.write("")

# --- JOB 3
st.write("- ▶", "**Business System Analyst | Infosphere, S.A De C.V**")
st.write(" 03/1995 - 11/1997")
st.write(
    """
- ● Adjustments to the FourGen system in Informix 4gl, speed up queries in FourGen reports, working for American clients such as Mens Warehouse, Whole Foods Market. 

"""
)
st.write("")

# --- JOB 3
st.write("- ▶", "**Technical Support / Jr. Analyst | ISOSA**")
st.write(" 02/1993 - 03/1995")
st.write(
    """
- ● Installation and configuration of Unisys Equipment with Unix and Informix. 
- ● Development of Unix Scripts for Support as well as I4gl application for management of computing assets. 

"""
)
st.write("")

# --- JOB 3
st.write("- ▶", "**Consultant | Hylsa Aceros Planos**")
st.write(" 09/1991 - 09/1992")
st.write(
    """
- ● Development of graphics in character mode related to the width measurement of steel rolls with SAS-IMS software for quality area.

"""
)
st.write("")

# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")
