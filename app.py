import streamlit as st
import random
st.set_page_config(page_title="growth mindset streamlit app", layout="centered")

st.write("""
This app is a small demonstration of the **Growth Mindset** in action.

### 💡 What's Inside?
- A simple layout
- Interactive widgets
- Motivational quotes
""")
quotes = [
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "Mistakes are proof that you are trying.",
    "Every expert was once a beginner.",
    "Success is the ability to go from one failure to another with no loss of enthusiasm.",
    "Believe you can, and you're halfway there.",
    "Great works are performed not by strength, but by perseverance.",
    "Growth is never by mere chance; it is the result of forces working together."
]

button = st.button("Click to Get A Growth Quote")
if button :
    random_quote=random.choice(quotes)
    st.write(random_quote)