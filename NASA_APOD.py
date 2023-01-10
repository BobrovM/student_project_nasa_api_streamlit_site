import requests
import streamlit as st


url = "https://api.nasa.gov/planetary/apod?" \
      "api_key=m6hzdHVjmNhxaA9hFRWEJOkdZeOvNj0E6EIXVgAd"

response = requests.get(url)
content = response.json()
picture = requests.get(content["url"])


st.set_page_config(layout="wide")

st.title("NASA - Astronomy Picture Of the Day")

st.title(content["title"])

st.header(content["date"])

st.image(picture.content)

st.write(content["explanation"])

st.write("Copyright: " + content["copyright"])
