# Qwen  installation 
from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from pydantic import BaseModel
import torch
import whisper

# fastapi 
app = FastAPI()

# Load the Whisper model tiny variant.
whisper_model = whisper.load_model("tiny")

#Load Qwen model and tokenizer (CPU-only)
model_name = "Qwen/Qwen2.5-0.5B-Instruct"   # model name  

#Define request model
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 512

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except Exception as e:
    print("error loading tokenizer :", e)
    exit(1)

# model instance 
try:
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,   # Reduce memory usage
        device_map="cpu",   # Force CPU
        low_cpu_mem_usage=True  # Optimize for CPU
    )

except Exception as e:
    print("Error loading model ", e)
    exit(1)

@app.post("/qwen")
async def generate(request: PromptRequest):

    try:
        messages = [
            {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. Provide accurate and helpful responses."},
            {"role": "user", "content": request.prompt}
        ]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer([text], return_tensors="pt").to("cpu")
        outputs = model.generate(**inputs, max_new_tokens=512)
        response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

        return {"response" : response}

    except Exception as e:
        print("Qwen never responded error occured! :", e)
        exit(1)

