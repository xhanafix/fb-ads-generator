import streamlit as st
from src.fb_ad_copy_generator import FacebookAdGenerator

def main():
    st.title("Facebook Ad Copy Generator 🚀")
    
    generator = FacebookAdGenerator()
    
    if 'variants' not in st.session_state:
        st.session_state.variants = generator.generate_variants()
    
    if st.button("Jana Iklan Baru"):
        st.session_state.variants = generator.generate_variants()
    
    for variant in st.session_state.variants:
        with st.expander(f"Iklan {variant['number']}"):
            st.text_area("", value=variant['content'], height=200, key=f"ad_{variant['number']}")
            if st.button("Salin", key=f"copy_{variant['number']}"):
                st.write("✅ Iklan telah disalin!")

if __name__ == "__main__":
