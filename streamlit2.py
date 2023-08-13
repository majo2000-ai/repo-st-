import streamlit as st
import pandas as pd
import numpy as np
import base64
import io
from io import BytesIO, StringIO
#import xlsxwriter 
import os

def main():
    st.title('AV Analysierer')
    st.markdown('Version 0.1.0\n&copy;')
    st.header("Berechnung")
    
    st.write("Hallo")
    with open("Datenanforderung.pdf", "rb") as f:
        btn = st.download_button(label="Download Datenanforderung", data=f, file_name="http://majo2000.bplaced.net/python/Datenanforderung.pdf")
    
    textcontents = """
    Nr,ArtikelNr, InvWert, InvBestand, Abgang
    1,456,10200, 2200, 856
    """

    st.download_button(label="Download CSV", data = textcontents, file_name="Template.csv", mime="text/csv")
if __name__ == "__main__":
    main()