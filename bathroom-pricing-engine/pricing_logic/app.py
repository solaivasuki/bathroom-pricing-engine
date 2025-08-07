# app.py
import streamlit as st
from pricing_engine import calculate_total_cost

st.set_page_config(page_title="Bathroom Pricing Engine", layout="centered")
# Add this near the top of app.py
st.markdown("""
    <style>
    .stApp {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton > button {
        background-color: #0072ff;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)





st.title("🚿 Bathroom Renovation Pricing Engine")
st.markdown("Get an instant estimate for renovation tasks based on your area and city.")

task = st.selectbox("Select Task", ["wall_painting", "floor_tiling", "plumbing", "electric_work"])
area = st.number_input("Enter Area (in sq. meters)", min_value=1.0, step=0.5)
city = st.text_input("Enter City", value="default")

if st.button("Calculate Total Cost"):
    result = calculate_total_cost(task, area, city)
    
    st.subheader("🧾 Estimate Breakdown")
    st.write(f"**Task**: {result['task']}")
    st.write(f"**City**: {result['city']}")
    st.write(f"**Area**: {result['area']} sq.m")
    st.write(f"**Estimated Hours**: {result['hours']}")
    st.write(f"**Material Cost**: ₹{result['material_cost']:.2f}")
    st.write(f"**Labor Cost**: ₹{result['labor_cost']:.2f}")
    st.write(f"**VAT Rate**: {result['vat_rate']*100:.1f}%")
    st.write(f"**VAT Amount**: ₹{result['vat_amount']:.2f}")
    st.markdown(f"### 💰 Total Cost: ₹{result['total_cost']:.2f}")
