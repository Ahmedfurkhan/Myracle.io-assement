# Myracle.io-assement
# Test Case Instructions Generator

This Streamlit application generates detailed testing instructions for QA engineers based on screenshots and context using Groq's API.

## Features

- Upload multiple screenshots of the application interface
- Provide optional context about the feature to be tested
- Choose between different LLaMA-3 models
- Generate detailed testing instructions including test case description, pre-conditions, testing steps, and expected results

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ahmedfurkhan/Myracle.io-assement.git
   ```
2. Navigate to the project directory:
   ```
   cd test-instructions-generator
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
3. Select the desired model from the dropdown menu.
4. (Optional) Provide context about the feature in the text area.
5. Upload one or more screenshots of the application interface.
6. Click "Generate Testing Instructions" to get the results.

## Prompting Strategy

The application uses a carefully crafted prompt to generate testing instructions. The prompt includes:

1. A system message defining the AI's role as a QA expert.
2. User message containing:
   - The provided context about the feature
   - Descriptions of the uploaded screenshots
   - Specific instructions on what to include in the testing instructions

This strategy ensures that the generated instructions are detailed, relevant, and follow a consistent structure.

## Dependencies

- streamlit
- groq
- Pillow (PIL)

## Configuration

Before running the application, make sure to set your Groq API key. You can do this by creating a `.env` file in the project root directory with the following content:

```
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Groq](https://groq.com/) for providing the API used in this project
- [Streamlit](https://streamlit.io/) for the web application framework
