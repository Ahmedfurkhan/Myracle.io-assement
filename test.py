import streamlit as st
from groq import Groq
from PIL import Image

# Initialize Groq client
groq_client = Groq(
    api_key="gsk_PdFpJTXZU4DfBaotVJwwWGdyb3FYKHpivtYkyU9XWgj",
)

# Model selection
MODELS = {
    "LLaMA-3 70B": "llama-3.1-70b-versatile",
    "LLaMA-3 Groq 70B": "llama3-groq-70b-8192-tool-use-preview"
}

def generate_test_instructions(images, context, model):
    """
    Generate testing instructions using the Groq API.
    """
    image_descriptions = [f"Image {i+1}: A screenshot of the application interface." for i in range(len(images))]
    image_description_text = "\n".join(image_descriptions)
    
    prompt = f"""Generate detailed testing instructions for a QA engineer based on the following context and screenshots:

Context: {context}

Screenshots:
{image_description_text}

Please include:
- Description of the test case.
- Pre-conditions (what needs to be set up before testing).
- Testing steps (detailed step-by-step).
- Expected result (what should happen if the feature works correctly).
"""

    chat_completion = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a QA expert tasked with generating detailed testing instructions based on screenshots and context."},
            {"role": "user", "content": prompt}
        ],
        model=model,
        temperature=0.7,
        max_tokens=1000
    )

    return chat_completion.choices[0].message.content

# Streamlit app interface
st.title("Test Instructions Generator")
st.write("Upload screenshots of the feature and provide an optional description to generate testing instructions.")

# Model selection
selected_model = st.selectbox("Select Model", list(MODELS.keys()))

# Context input
context = st.text_area("Optional Context (Describe the feature, if necessary)", "")

# Image uploader (Multiple images allowed)
uploaded_files = st.file_uploader("Upload Screenshots", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Button to process the inputs
if st.button("Generate Testing Instructions"):
    if uploaded_files:
        with st.spinner("Processing the screenshots. Please wait..."):
            images = [Image.open(uploaded_file) for uploaded_file in uploaded_files]
            response = generate_test_instructions(images, context, MODELS[selected_model])
        
        if response:
            st.write("### Generated Testing Instructions:")
            st.write(response)
    else:
        st.error("Please upload at least one screenshot to proceed.")

# Add a footer with information about the model used
#st.markdown("---")
#st.write(f"This app uses Groq's API with the {selected_model} model to generate testing instructions.")
