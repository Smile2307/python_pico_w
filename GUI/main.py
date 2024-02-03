import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

st_autorefresh(interval=5000)

st.title("Pico_W_職能發展協會專案")
st.header("雞舍:red[溫度]和:blue[光線]狀態")
st.divider()

#url='https://blynk.cloud/external/api/get?token=V4RM4y9Q0-JaqBbF4ut1sHoO1lef-6Z3&v1&v2&v0'

url=f'https://blynk.cloud/external/api/get?token={api_key}&v1&v2&v0'

response = requests.request("GET",url)
if response.status_code == 200:
    all_data = response.json()
    st.info(f'LED:{all_data["v0"]}')
    st.warning(f'可變電阻:{all_data["v1"]}')
    st.warning(f'光線:{all_data["v2"]}')
    st.snow()
else:
    st.write("連線失敗,請等一下再試")
