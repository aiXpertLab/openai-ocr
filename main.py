import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SHOW TABLES;', ttl=600)

st.write(df)