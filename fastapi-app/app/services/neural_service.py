#type: ignore
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from ..config import settings
import torch

class NeuroService:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.is_loaded = False
    
    async def load_model(self):
        try:
            #load_model
            self.tokenizer = GPT2Tokenizer.from_pretrained(settings.MODEL_PATH)
            self.model = GPT2LMHeadModel.from_pretrained(settings.MODEL_PATH)
            
            self.model.to(settings.DEVICE)
            self.is_loaded = True
        except Exception as e:
            raise Exception("error while load model: {e}")
        
    async def generate_response(self, message: str) -> str:
        if not self.is_loaded:
            await self.load_model()
        
        try:
            #tokenizer
            prompt = f"Пользователь: {message}\nКоуч:"
            inputs = self.tokenizer(prompt, return_tensors="pt")
            inputs = inputs.to(settings.DEVICE)

            #model
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=settings.MAX_LENGTH,
                    num_return_sequences=1,
                    temperature=settings.TEMPERATURE,
                    do_sample=settings.DO_SAMPLE,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            #decode
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            if prompt in response:
                response = response[len(prompt):].strip()
            else:
                response = full_response.split("Коуч:")[-1].strip()
            
            response = response.split("Пользователь:")[0].strip()
            
            return response if response else "Расскажите подробнее о вашей ситуации."
        
        except Exception as e:
            return f"sorry, error: {e}"

neuro_service= NeuroService()
