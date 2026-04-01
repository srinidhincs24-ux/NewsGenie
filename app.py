import streamlit as st
from workflow import process_query

st.title("🧞 NewsGenie")
st.write("Your AI-powered news assistant")

query = st.text_input("Ask your question:")

category = st.selectbox(
    "Select News Category",
    ["technology", "business", "sports"]
)

if st.button("Submit"):
    if query:
        response = process_query(query, category)
        st.write(response)
    else:
        st.warning("Please enter a query")