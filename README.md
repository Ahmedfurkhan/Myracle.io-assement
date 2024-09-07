# Myracle.io-assement
# Test Case Instructions Generator

This Streamlit application generates detailed testing instructions for QA engineers based on screenshots and context. It offers two powerful approaches: using Groq's API with LLaMA-3 models and a local implementation of LLaMA 3.1.

## Features

- Upload multiple screenshots of the application interface
- Provide optional context about the feature to be tested
- Choose between Groq API (LLaMA-3 models) and local LLaMA 3.1 implementation
- Generate detailed testing instructions including test case description, pre-conditions, testing steps, and expected results

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ahmedfurkhan/Myracle.io-assement.git
   ```
2. Navigate to the project directory:
   ```
   cd Myracle.io-assement
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
2. Open the provided URL in your web browser.
3. Choose between Groq API and local LLaMA 3.1 implementation.
4. If using Groq API, select the desired model from the dropdown menu.
5. (Optional) Provide context about the feature in the text area.
6. Upload one or more screenshots of the application interface.
7. Click "Generate Testing Instructions" to get the results.

## Prompting Strategy

Both approaches use a carefully crafted prompt to generate testing instructions. The prompt includes:

1. A system message defining the AI's role as a QA expert.
2. User message containing:
   - The provided context about the feature
   - Descriptions of the uploaded screenshots
   - Specific instructions on what to include in the testing instructions

This strategy ensures that the generated instructions are detailed, relevant, and follow a consistent structure.

## Dependencies

- streamlit
- groq
- torch
- transformers
- Pillow

## Configuration

### Groq API
Before running the application with Groq API, make sure to set your Groq API key. Create a `.env` file in the project root directory with the following content:

```
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

### Local LLaMA 3.1
Ensure you have access to the LLaMA model weights and update the `model_name` in the `load_llama_model()` function if necessary.

## Benefits of Using Groq

1. **Ease of Use**: Groq's API simplifies the process of leveraging powerful language models without the need for local setup and management of model weights.

2. **Scalability**: Groq's infrastructure can handle varying loads, making it easier to scale your application as needed.

3. **Up-to-date Models**: Groq regularly updates its models, ensuring you have access to the latest improvements in language model performance.

4. **Reduced Computational Requirements**: By offloading the computation to Groq's servers, you can run the application on less powerful hardware.

5. **Flexibility**: Groq offers multiple LLaMA-3 models, allowing you to choose the best fit for your specific use case.

## Benefits of Local LLaMA 3.1 Implementation

1. **Control**: Full control over the model and its parameters, allowing for fine-tuning and customization.

2. **Privacy**: All processing happens locally, which can be crucial for sensitive data.

3. **No API Costs**: Once set up, there are no ongoing API costs associated with usage.

4. **Offline Capability**: The application can function without an internet connection.

By offering both approaches, this application provides flexibility to users, allowing them to choose the method that best fits their needs, whether it's the convenience and power of Groq's API or the control and privacy of a local LLaMA implementation.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Groq](https://groq.com/) for providing the API used in this project
- [Streamlit](https://streamlit.io/) for the web application framework
- The creators of LLaMA for their groundbreaking work on large language models
