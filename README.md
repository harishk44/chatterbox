**Advanced Generative Chatbot  - Chatterbox**

      This project is an NLP assignment focusing on the design of an advanced generative chatbot using the GPT-2 model. 
      The goal of this project is to create a chatbot that can carry out multi-turn conversations, adapt to context, and handle a variety of topics

**Project Structure**

      The repository contains the following key files:
      
      config.json: Configuration file for the GPT-2 model, including hyperparameters and model architecture details.
      
      generation_config.json: Specifies the configuration used for text generation, including sampling parameters.
      
      vocab.json: The vocabulary file used by the GPT-2 tokenizer to encode and decode text.
      
      chatbotapi.py: Python script to create an API endpoint for interacting with the chatbot using FastAPI.
      
      Chatbot.js: JavaScript file that manages the front-end integration for interacting with the chatbot.
      
      Assignment7_1_ver5_final_team_project_Advanced Generative Chatbot Design.ipynb: Jupyter Notebook that includes the implementation details, experiments, and evaluation of the chatbot.

**Features**

    Model: Uses GPT-2, a generative transformer-based model, to generate responses.
    
    API: FastAPI is used to expose endpoints to interact with the model.
    
    Frontend Integration: ReactJS-based front-end component for an interactive chatbot interface.

**Setup and Installation**

    Clone the repository:

        git clone <repository-url>
        cd <repository-folder>

    Create a virtual environment and activate it:

        python -m venv env
        source env/bin/activate  # On Windows, use 'env\Scripts\activate'

    Install the required dependencies:

        pip install -r requirements.txt

    Run the FastAPI server:

        uvicorn chatbotapi:app --host 0.0.0.0 --port 8000
    
        npm start to start the web interface (Chatbot.js) to integrate with the front-end or run the HTML page to interact with the chatbot.

**Usage**

    API Endpoint: The API can be accessed via the web interface or direct invocation  to interact with the chatbot. For example, you can send a POST request with a prompt, 
    and the chatbot will respond with a generated text.
  
    Front-End: The JavaScript file (Chatbot.js) is used to handle front-end interactions and send user inputs to the backend API.

**Model Files**

    The configuration files (config.json, generation_config.json, vocab.json) are necessary to initialize the GPT-2 model and tokenizer. Ensure that these files are correctly placed in     the directory where the model is being loaded.

**Example**

    Here is an example of interacting with the API:
    
    Send a POST request to the /chat endpoint with the following JSON:
    
    {
      "prompt": "What is Arena football league?"
    }
    
    The API will respond with a generated message from the chatbot:
    
    {
      "response": "The Arena Football League (AFL) was formed on June 18, 1987 in Detroit by the United States Postal Service as a private organization and operated from its original base in suburban Detroit"
    }

**Requirements**

    Python 3.8+
    
    FastAPI
    
    Transformers (HuggingFace)
    
    Node.js (for front-end integration)

**Contributing**

    Feel free to submit issues or pull requests to enhance the chatbot, add new features, or improve the documentation.

**License**

    This project is licensed under the MIT License.
