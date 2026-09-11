import streamlit as st
st.set_page_config(page_title="Kochi AI", page_icon="🤖")
st.title("🤖 KOCHI AI - All Rounder")
st.write("Made from Kochi at 6:15AM!")

menu = st.selectbox("Choose:", ["Chat with AI", "Photo Scanner", "Study Helper"])

if menu == "Chat with AI":
    q = st.text_input("Ask anything:")
    if q:
        st.success("AI: Great question about '" + q + "'! Your AI is working!")
        st.balloons()
elif menu == "Photo Scanner":
    photo = st.file_uploader("Upload photo", type=["jpg","png","jpeg"])
    if photo:
        st.image(photo)
        st.success("AI Sees your photo!")
else:
    lesson = st.text_area("Paste your lesson:")
    if st.button("Make Questions"):
        st.write("1. What is main idea?")
        st.write("2. Explain in your words")
        st.write("3. Give real example?")
