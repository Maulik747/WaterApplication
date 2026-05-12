
import streamlit as st
import requests

BACKEND_URL = "http://backend:8000"

st.set_page_config(page_title="Skeleton App")

st.title("FastAPI + Streamlit App")

name = st.text_input("Enter your name", "Developer")

if st.button("Call Backend"):
    response = requests.get(
        f"{BACKEND_URL}/hello",
        params={"name": name}
    )

    if response.status_code == 200:
        data = response.json()
        st.success(data["message"])
    else:
        st.error("Backend request failed")

st.divider()

st.subheader("Age Calculator")

birth_year = st.number_input(
    "Enter your year of birth",
    min_value=1900,
    max_value=2100,
    value=2000,
    step=1
)

if st.button("Calculate Age"):
    response = requests.get(
        f"{BACKEND_URL}/calculate-age",
        params={"year_of_birth": birth_year}
    )

    if response.status_code == 200:
        data = response.json()
        st.success(f"Your age is approximately {data['age']} years")
    else:
        st.error("Age calculation failed")