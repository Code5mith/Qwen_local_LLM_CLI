# Qwen Local LLM

A lightweight terminal application powered by **Qwen2.5-0.5B-Instruct**, a local language model running on CPU. It features a FastAPI backend (`qwen_api.py`) for text generation and a client script (`prompt_loop.py`) for interactive prompting via the terminal. Built for low-resource environments like WSL, it delivers fast, accurate responses for coding and general queries.

## Features
- **Local LLM**: Runs Qwen2.5-0.5B-Instruct (~1GB) offline on CPU.
- **FastAPI Backend**: Exposes `/qwen` endpoint for text generation.
- **Terminal Client**: Interactive CLI for sending prompts and viewing responses.
- **Error Handling**: Robust model loading and API error management.
- **Lightweight**: Optimized for ~1-2GB RAM usage.

## Requirements
- Python 3.12+
- WSL or Linux-based system
- ~4GB RAM (model: ~1-2GB)
- Internet for initial model download

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/qwen-local-llm.git
   cd qwen-local-llm
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

4. **Download Model**:
   - Qwen2.5-0.5B-Instruct (~1GB) downloads automatically on first run to `~/.cache/huggingface/`.

## Usage
1. **Start the API Server**:
   ```bash
   uvicorn qwen_api:app --host 0.0.0.0 --port 8001
   ```

2. **Run the Terminal Client**:
   In a new terminal:
   ```bash
   source qwen_env/bin/activate
   python prompt_loop.py
   ```
   - Enter prompts, type `exit` or press CTRL-C to quit.

3. **Example API Call**:
   ```bash
   curl -X POST http://localhost:8001/qwen -H "Content-Type: application/json" -d '{"prompt": "Write a Python function to reverse a string", "max_tokens": 512}'
   ```

## Project Structure
- `qwen_api.py`: FastAPI backend with Qwen2.5-0.5B-Instruct for text generation.
- `prompt_loop.py`: Terminal client for interactive prompting via API.
- `README.md`: Project documentation.
- `LICENSE`: MIT License.

## Performance
- **RAM**: ~1-2GB for model, ~2-4GB total.
- **Startup**: ~2-4 minutes for model loading.
- **Inference**: ~1-3 seconds per prompt.

## License
MIT License. See `LICENSE` for details.

## Contributing
Contributions welcome! Fork the repo, create a branch, and submit a pull request. Report issues or suggest features via GitHub Issues.

## Acknowledgments
- [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- Code generated with assistance from **Grok** by xAI.