import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))) + "..")
from graph_logic import GraphApp
from config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

st.set_page_config(page_title="Startup & Funding Ecosystem Graph")

st.title("Startup & Funding Ecosystem")
st.markdown("Visualize relationships between startups, founders, investors, and sectors.")

# Neo4j connection
app = GraphApp(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)

tab1, tab2, tab3 = st.tabs(["Add Data", "Create Relationships", "View All Startups"])

with tab1:
    st.subheader("Add Entities")
    entity_type = st.selectbox("Select Entity Type", ["Startup", "Founder", "Investor", "Sector"])

    if entity_type == "Startup":
        name = st.text_input("Startup Name")
        year = st.number_input("Founded Year", min_value=1900, max_value=2100)
        location = st.text_input("Location")
        if st.button("Create Startup"):
            app.create_startup(name, year, location)
            st.success("Startup created!")

    elif entity_type == "Founder":
        name = st.text_input("Founder Name")
        age = st.number_input("Age", min_value=18, max_value=100)
        exp = st.number_input("Years of Experience", min_value=0, max_value=50)
        if st.button("Create Founder"):
            app.create_founder(name, age, exp)
            st.success("Founder created!")

    elif entity_type == "Investor":
        name = st.text_input("Investor Name")
        firm = st.text_input("Firm")
        inv_type = st.selectbox("Type", ["Angel", "VC", "Corporate", "Private Equity"])
        if st.button("Create Investor"):
            app.create_investor(name, firm, inv_type)
            st.success("Investor created!")

    elif entity_type == "Sector":
        name = st.text_input("Sector Name")
        if st.button("Create Sector"):
            app.create_sector(name)
            st.success("Sector created!")

with tab2:
    st.subheader("Link Startup with...")
    s_name = st.text_input("Startup Name (Existing)")
    f_name = st.text_input("Founder Name")
    i_name = st.text_input("Investor Name")
    sec_name = st.text_input("Sector Name")

    if st.button("Link to Founder"):
        app.link_startup_to_founder(s_name, f_name)
        st.success("Linked to Founder!")

    if st.button("Link to Investor"):
        app.link_startup_to_investor(s_name, i_name)
        st.success("Linked to Investor!")

    if st.button("Link to Sector"):
        app.link_startup_to_sector(s_name, sec_name)
        st.success("Linked to Sector!")

with tab3:
    st.subheader("All Startup Data")
    data = app.get_all_startups()
    st.dataframe(data)

# Close connection on exit
app.close()