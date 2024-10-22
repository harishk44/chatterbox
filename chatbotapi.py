from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import GPT2Tokenizer, AutoModelForCausalLM
import torch

# Load the trained model and tokenizer
model_path = '/Users/harish/Documents/USD-Sandiego/AAI520/module7/model/drive-download-20241021T115805Z-001'
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# Set pad_token to eos_token to avoid padding-related warnings
tokenizer.pad_token = tokenizer.eos_token
model.eval()

app = FastAPI()

# Add CORS middleware to allow the React app to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for added security.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    context: str = ""  # Set an empty string as the default if no context is provided
    question: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API"}

@app.post("/get_response/")
def get_chatbot_response(request: ChatRequest):
    print(f"Received request: context={request.context}, question={request.question}")
    
    # Prepare input text with a more explicit format
    #if request.context:
    #    input_text = f"Context: {request.context}\nQuestion: {request.question}\nAnswer:"
    #else:
    #    input_text = f"Question: {request.question}\nAnswer:"

    #input_text = f" Provide a concise and accurate answer to the following question.\nQuestion: {request.question}\nAnswer:"
    input_text = f"Question: {request.question}\nAnswer:"

    
    print(f"####input_text####={input_text}")
    
    # Tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', truncation=True, padding=True, max_length=256)
    attention_mask = inputs['attention_mask']

    # Make prediction
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs['input_ids'],
            attention_mask=attention_mask,
            max_new_tokens=100,  # Adjust this based on the expected response length
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,  # Enable sampling
            temperature=0.6,  # Lower value for more deterministic response
            top_k=30,  # Lower top_k to limit randomness
            top_p=0.85,  # Adjust nucleus sampling for quality
            repetition_penalty=1.2, 
        )

    
    # Decode response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"response{response}")

    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
