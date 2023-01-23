# # -*- coding: utf-8 -*-
# """
# Created on Thu Jan 19 13:18:10 2023

# @author: ShorY
# """
# import streamlit as st
# import pandas as pd
# from streamlit_option_menu import option_menu




# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# # 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

# 3. CSS style definitions
# selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "green"},
#     }
# )

































import streamlit as st
import time
import pandas as pd
import numpy as np
import subprocess

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")



if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

# st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
# st.markdown("""  <nav>
#     <div class="navbar navbar-inverse navbar-fixed-top">
#         <div class="container-fluid">
#             <div class="navbar-header">
#                 <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
#                     <span class="icon-bar"></span>
#                     <span class="icon-bar"></span>
#                     <span class="icon-bar"></span>
#                 </button>
#                 <a class="navbar-brand" runat="server" href="http://biz.markiting.net/Links/home.html">Mark-it-ing</a>
#             </div>
#             <div class="navbar-collapse collapse">
#                 <ul class="nav navbar-nav">
#                     <li><a runat="server" href="http://biz.markiting.net/Links/home.html">Home</a></li>
#                     <li><a runat="server" href="https://ads.google.com/aw/overview/" target="_blank">Google Ads</a></li>
#                     <li><a runat="server" href="https://leader.leadercapital.net/" target="_blank">CRM Leader Capital</a></li>
#                     <li><a runat="server" href="https://gcmforex.leadercapital.net/" target="_blank">CRM GCM Forex</a></li>
#                     <li><a runat="server" href="https://bi.leadercapital.net/" target="_blank">Bi Leader Capital</a></li>
#                 </ul>
#             </div>
#         </div>
#     </div>
# </nav>
# <br>   """,unsafe_allow_html=True)
    
col1,col2,col3 = st.columns([1,2,1])
    
col1.markdown("#Welcome to my channel")
col1.markdown("Here is some info on the app")
#st.button("try new page",on_click=subprocess.run(["python", "example_1.py"]))



def change_photo_state():
    st.session_state["photo"]="done"

uploaded_photo = col2.file_uploader("Upload a photo",on_change = change_photo_state)
camera_photo = col2.camera_input("Take a photo",on_change = change_photo_state)

# if st.button('run other script'):
#     st.write('Why hello there')
#     st.title('Uber pickups in NYC')

#     subprocess.run(["python", "script.py"])





if st.session_state["photo"] == "done":
    progress_bar = col2.progress(0)
    
    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed + 1)
    col2.success("Photo uploaded successfully!")
    col3.metric(label="Temperature", value="60 C", delta = "3 C")
    
    with st.expander("Click to read more"):
        st.write("Hello here are more details on this topic that you were interested in.")
        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)            
        
        
        
st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)       
