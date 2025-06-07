from transformers import AutoTokenizer, AutoModelForCausalLM
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_TOKEN")

model_id = "ibm-granite/granite-3.3-2b-instruct"  # ✅ Or use another public model

tokenizer = AutoTokenizer.from_pretrained(model_id, token=token)
model = AutoModelForCausalLM.from_pretrained(model_id, token=token)
