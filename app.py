import streamlit as st
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
from PIL import Image
import io

# Function definitions
def load_llama_model():
    model_name = "huggyllama/llama-13b"  # Replace with the correct LLaMA model if you have it
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    model = LlamaForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
    return model, tokenizer

def generate_test_instructions(images, context, model, tokenizer):
    """
    This function generates testing instructions using LLaMA 3.1 model.
    The images are currently simulated as part of the context.
    """
    # Simulate image processing by embedding a description of the images
    image_description = "Screenshots provided show various UI elements of the feature."

    # Combine the context and image description
    full_prompt = (
        f"Generate detailed testing instructions for a QA engineer based on the following context and screenshots:\n\n"
        f"Context: {context}\n"
        f"{image_description}\n\n"
        "Please include:\n"
        "- Description of the test case.\n"
        "- Pre-conditions (what needs to be set up before testing).\n"
        "- Testing steps (detailed step-by-step).\n"
        "- Expected result (what should happen if the feature works correctly).\n"
    )

    # Tokenize the input
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)

    # Generate a response
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_length=500,
            num_return_sequences=1,
            do_sample=True,
            top_p=0.95,
            temperature=0.7
        )

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Load model once during app startup
@st.cache_resource
def get_model():
    return load_llama_model()

model, tokenizer = get_model()

# Streamlit app interface
st.title("Testing Instructions Generator with LLaMA 3.1")

st.write("Upload screenshots of the feature and provide an optional description to generate testing instructions.")

# Context input
context = st.text_area("Optional Context (Describe the feature, if necessary)", "")

# Image uploader (Multiple images allowed)
uploaded_files = st.file_uploader("Upload Screenshots", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Button to process the inputs
if st.button("Describe Testing Instructions"):
    if uploaded_files:
        # Prepare the images for the multimodal model (currently just simulating)
        images = []
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            images.append(image)

        # Generate test instructions by passing images and context to LLaMA model
        st.write("Processing the screenshots. Please wait...")

        # Call the LLaMA model to generate testing instructions
        response = generate_test_instructions(images, context, model, tokenizer)

        st.write("### Generated Testing Instructions:")
        st.write(response)
    else:
        st.error("Please upload at least one screenshot to proceed.")