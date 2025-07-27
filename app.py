# app.py
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

@st.cache_resource
def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        "Jasur05/phi2-legal",  # ← your HF repo
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained("Jasur05/phi2-legal")
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

st.set_page_config(page_title="Legal Chatbot", layout="centered")
st.title("🤖 Phi-2 Legal Assistant")

pipe = load_model()

# Input box
user_input = st.text_area("Ask a legal question:", height=100)
if st.button("Submit") and user_input.strip():
    with st.spinner("Generating answer..."):
        instruction = (
         "Give a clear, concise, and legally accurate answer to the following question. "
         "If relevant, cite legal clauses or examples. Answer in plain language suitable for the general public."
        )
        prompt = f"Instruction: {instruction}\nInput: {user_input}\nOutput:"
        result = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7)[0]["generated_text"]

        # Extract only the first output after "Output:"
        try:
            only_first_output = result.split("Output:")[1].split("Output:")[0].strip()
        except IndexError:
            only_first_output = "Sorry, something went wrong in generating the answer."

        # Display result
        st.markdown("### 📘 Answer")
        st.write(only_first_output)

