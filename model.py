from transformers import AutoTokenizer, AutoModelForCausalLM
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_TOKEN")
token="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"
model_id = "model_id = "ibm-granite/granite-3.3-2b-instruct"
model_id = "tiiuae/falcon-7b-instruct"  # or any public LLM

tokenizer = AutoTokenizer.from_pretrained(model_id, token=token)
model = AutoModelForCausalLM.from_pretrained(model_id, token=token)

def generate_response(prompt: str) -> str:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_new_tokens=150)
    return tokenizer.decode(output[0], skip_special_tokens=True)
