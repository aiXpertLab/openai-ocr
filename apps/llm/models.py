import  streamlit as st

def pick_model():
    model = st.radio(
        "Select the model you want to use",
        ["OpenAI", "DeepSeek", "Llama", "Palm", "GPT-3"],
        index=0
    )
    return model
