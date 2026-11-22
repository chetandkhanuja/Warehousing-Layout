import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title='Warehouse Organization Simulation', page_icon='🏭', layout='wide')
st.title('🏭 Warehouse Organization Simulation')
st.caption('Amul and Reliance warehouse organization · Floor-based SKU storage · Animated worker simulation')
html_path = Path(__file__).parent / 'index.html'
html = html_path.read_text(encoding='utf-8')
components.html(html, height=1000, scrolling=True)
