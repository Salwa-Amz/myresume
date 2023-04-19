import streamlit as st
from PIL import Image

with open("test.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# AMZIL Salwa,
# Mohammadia School of Engineers.
##### *Resume* 
''')

image = Image.open('W.png.png')
st.image(image, width=150)


st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)


st.sidebar.markdown("""
<nav class="navbar navbar-dark" style="background-color: #16A2CB;">
  <ul class="navbar-nav flex-column">
      <li class="nav-item">
        <a class="nav-link" href="#summary">Summary</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#school-projects">School Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills-and-languages">Skills and Languages</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#interests">Interests</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact-me">Contact me</a>
      </li>
  </ul>
</nav>
""", unsafe_allow_html=True)

#####################
# Navigation
# Open the PDF file in binary mode
pdf_file = open('cv pdf.pdf', 'rb')

with open('cv pdf.pdf', 'rb') as pdfFile:
    pdf_bytes = pdfFile.read()
    st.sidebar.download_button('Download cv PDF', data=pdf_bytes, file_name='cv pdf.pdf', mime='application/pdf')


# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

st.markdown('''## Summary ''')
st.info('''
- An industrial engineer graduate, seeking a position that will allow for putting my
diverse theoritical knowledge alligned with my work experience and flexible
personality to bring value into your company.
''')

st.markdown('''
## Education
''')

txt('**Bac+5 Engengineering Diploma** (Industrial engineering), *Mohammadia school of engineers*, Rabat',
'2020-2023')
st.markdown('''
- Speciality: `Project management`
''')

txt('**Bac +2** (Technology and industrial sciences), *Réda Slaoui Preparatory Classes For Grandes École*, Agadir',
'2018-2020')
st.markdown('''
- NCT(CNC) Rank: `27`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**BI- Data analyst Intern**, Bu-Logistics OCP Group,'' Competitors tracking and pricing, Rabat',
'`2023 - 5 months`')
st.markdown('''
- Collected competitors' data from different sources, monitored sales and
established field connections.
- Analyzed Data using Excel, oracle, power Bi etc
- Interpreted results and dressed competitor's sales, market and logistics
strategy
- Built a predictive model with python/UML
- Built a Streamlit application interface
- Implemented the predictive results to adjust the pricing strategy
''')
txt('**Logistics service Intern**, CMCP IP, Transit department monitoring, Agadir',
'`2022 - 2 months`')
st.markdown('''
- Collected and rectified Data from excel reports and field observations
- Used VBA to organize and automate excel spreadsheets
- Analyzed transport process KPIsL using correlation tests in R studio
- Developed monitoring Dashboards on Power bi
''')
txt('**Processes and Mail Methods Reengineering Service Intern**, Poste Maroc, Optimizing the workflow, Rabat',
'`2022 - 4 months(alternance)`')
st.markdown('''
- Constructed a Gantt Diagram in excel using VBA code
- Analyzed the workflow performance using the cycle time compared to the takt time
- Proposed ergonomic solutions and lean tools : Kanban - 5S - Muda - Poka yoke 
''')
txt('**Maintenance and design department Intern**, Copag, Taroudant',
'`2021 - 1 month`')
st.markdown('''
- Studied a recent juice installation and created its P&ID piping and
instrumentation diagram using autocad
''')

#####################
st.markdown('''
## School Projects
''')

txt('**Design methodology**', ' ')
st.markdown('''
- Realization of a mobile application using the Waterfall process, steps :
- Business model 
- Market definition
- Quality function deployment 
- Multi-criteria analysis 
- Uml diagrams(conception) 
- tests and conclusions.
''')
txt('**Big Data Project**',' ')
st.markdown('''
- Using different machine  learning approaches
Supervised/Unsupervised, regression/classification to better fit a certain data sets.
''')
txt('**Financial Risk management Project**',' ')
st.markdown('''
- Conduct a technical analysis using trends and statistical indicators applied on TESLA stocks
''')
txt('**Quality Control Project**',' ')
st.markdown('''
Using different quality control tools:
- Paretto diagram
- Ishikawa diagram
- Control charts (Developed using R)
- Design of experiments 
to monitor a certain dataset performance 
''')
txt('**Study highlights**',' Important courses ')
st.markdown('''
- Major project management
- lean management
- Marketing b to b 
- Finance
- HSSE 
- Innovation
- Risk management
''')

st.markdown('''
## Skills and Languages
''')
txt3('Programming', '`Python`, `R`, `VB`')
txt3('Data processing/visualization', '`SQL`, `Office tools`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Model deployment', '`streamlit`')
txt3('Languages', '`English`,`French`,`Arabic`')

#####################
st.markdown('''
## Interests
''')
txt('My Interests are:', '')
st.markdown('''
- Knitting
- Manga/Anime
''')

#####################
st.markdown('''
## Contact me
''')
txt3('Mail Address', '`salwaamzil@student.emi.ac.ma`')
txt3('Phone nuber', '`0766514332`')
txt3('Address', '`Avenue Ibn Sina B.P 765 ,Agdal Rabat`')
