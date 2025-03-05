import streamlit as st
import uv

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

    def convert(self, value, from_unit, to_unit):
        try:
            result = uv.Unit(value, from_unit).to(to_unit)  # Corrected conversion function
            return result.magnitude  # Get the numerical value
        except Exception as e:
            return f"Conversion error: {e}"

# Initialize converter
converter = UnitConverter()

# Custom Styling
st.markdown(
    """
    <style>
        body { font-family: 'Poppins', sans-serif; background-color: #f4f8fb; }
        .stApp { background-color: #ffffff; padding: 25px; border-radius: 15px; box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.15); }
        .stTitle { color: #0d47a1; font-weight: bold; font-size: 30px; text-align: center; }
        .stMarkdown { color: #1565c0; font-size: 18px; text-align: center; }
        .stButton>button { background-color: #1e88e5; color: white; font-weight: bold; border-radius: 10px; padding: 12px; font-size: 16px; }
        .stButton>button:hover { background-color: #1565c0; }
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
st.markdown("<p class='stMarkdown' style='text-align: center;'>Made with ❤️ using Streamlit and UV</p>", unsafe_allow_html=True)
