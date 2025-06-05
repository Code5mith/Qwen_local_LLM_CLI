# Qwen Local LLM

A lightweight terminal application powered by **Qwen2.5-0.5B-Instruct**, a local language model  developed by Alibaba Cloud. It features a FastAPI backend (`qwen_api.py`) for text generation and a client script (`prompt_loop.py`) for interactive prompting via the terminal.Very friendly and responsive in low-resource enviromnents can delivers fast, accurate responses for general queries or specific use cases (coding assistance).

## Features
- **Local LLM**: Runs Qwen2.5-0.5B-Instruct (~1GB) offline on CPU.
- **FastAPI Backend**: Exposes `/qwen` endpoint for text generation.
- **Terminal Client**: Interactive CLI for sending prompts and viewing responses.
- **Lightweight**: Optimized for ~1-2GB RAM usage after initial loading stage.

## Requirements
- Python 3.12+
- ~4GB RAM (model: ~1-2GB)
- Internet for initial model download once downloaded model works completely offline

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/code5mith/Qwen_local_LLM_CLI.git
   cd Qwen_local_LLM_CLI
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv qwen_env
   source qwen_env/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn transformers torch accelerate sentencepiece pydantic requests
   ```
## Usage
1. **Start the API Server**:
   ```bash
   uvicorn qwen_api:app --host 0.0.0.0 --port 8001
   ```
    - Running this for first time will automatically download Qwen2.5-0.5B-Instruct to your local mechine download size (~ 5GB maximum)

2. **Run the Terminal Client**:
   In a new terminal:
   ```bash
   source qwen_env/bin/activate
   python client_prompt.py
   ```
   - Enter prompts, type `exit` or press CTRL-C to quit.


## Project Structure
- `qwen_api.py`: FastAPI backend with Qwen2.5-0.5B-Instruct to run model.
- `prompt_loop.py`: Terminal client for interactive prompting via API.
- `README.md`: Project documentation.

## Performance
- **RAM**: ~1-2GB for model, ~2-4GB total.
- **Startup**: ~2-4 minutes for model loading.
- **subsequent requests**: depending on the complexty of the prompt time will vary .

## Acknowledgments
- [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) by Alibaba Cloud.
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
