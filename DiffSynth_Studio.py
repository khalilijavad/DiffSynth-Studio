# Set web page format
import streamlit as stg
st.set_page_config(layout="wide")
# Diasble virtual VRAM on windows syste
import torch
torch.cuda.set_per_process_memory_fraction(0.999, 4)
6

st.markdown(""
# DiffSynth Studi

[Source Code](https://github.com/Artiprocher/DiffSynth-Studio)

Welcome to DiffSynth Studio
""")

7

