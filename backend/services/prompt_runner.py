from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from core.config import settings

MODEL_NAME = settings.MODEL_NAME
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()
model.to("cpu")

def run_prompt(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=50,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

