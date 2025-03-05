import streamlit as st
import pint

# Set page configuration first
st.set_page_config(page_title="Universal Unit Converter", layout="centered")

class UnitConverter:
    def __init__(self):
        self.unit_categories = {
            "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
            "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
            "Temperature": ["celsius", "fahrenheit", "kelvin"],
            "Time": ["second", "minute", "hour", "day"],
            "Volume": ["liter", "milliliter", "gallon", "cup", "pint"],
        }
        self.ureg = pint.UnitRegistry()

    def convert(self, value, from_unit, to_unit):
        try:
            quantity = self.ureg.Quantity(value, from_unit)
            result = quantity.to(to_unit)
            return result.magnitude  # Get the numerical value
        except Exception as e:
            return f"Conversion error: {e}"

# Initialize converter
converter = UnitConverter()

# Custom Styling
st.markdown(
    """
    <style>
           body { font-family: 'Arial', sans-serif; background-color: #f4f4f4; }
        .stApp { background-color: #ffffff; padding: 20px; border-radius: 10px; }
        .stTitle { color: #2C3E50; font-weight: bold; }
        .stMarkdown { color: #34495E; }
        .stButton>button { background-color: #2980B9; color: white; font-weight: bold; border-radius: 5px; }
        .stButton>button:hover { background-color: #1F618D; }
        .stSelectbox, .stNumberInput { background-color: #e3f2fd; border-radius: 10px; padding: 10px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='stTitle'>🌍 Universal Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='stMarkdown'>Convert between different units easily and efficiently.</p>", unsafe_allow_html=True)

# Select category
category = st.selectbox("Select a unit category:", list(converter.unit_categories.keys()))

# Select input and output units
col1, col2 = st.columns(2)
with col1:
    input_unit = st.selectbox("From:", converter.unit_categories[category])
with col2:
    output_unit = st.selectbox("To:", converter.unit_categories[category])

# Input value
to_convert = st.number_input("Enter value:", min_value=0.0, format="%.4f")

# Conversion logic
if st.button("Convert", use_container_width=True):
    result = converter.convert(to_convert, input_unit, output_unit)
    if isinstance(result, (float, int)):
        st.success(f"{to_convert} {input_unit} = {result:.4f} {output_unit}")
    else:
        st.error(result)

# Footer
st.markdown("---")
st.markdown("<p class='stMarkdown' style='text-align: center;'>Made By ❤️ KANWAL YOUSUF</p>", unsafe_allow_html=True)