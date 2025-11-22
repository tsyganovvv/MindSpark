#type: ignore
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from ..config import settings
import torch
import re

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
            prompt = f"""Ты - профессиональный AI-коуч. Твоя задача - помогать людям в личностном росте.

Пользователь: {message}

Ты должен ответить как коуч: поддерживающе, с эмпатией, задавая уточняющие вопросы и давая практические советы. Будь кратким (2-3 предложения).

Коуч:"""
            inputs = self.tokenizer(prompt, return_tensors="pt")
            inputs = inputs.to(settings.DEVICE)

            #model
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=200,  # Увеличил немного
                    num_return_sequences=1,
                    temperature=0.8,  # Чуть более креативно
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=1.5,  # Штраф за повторения
                    no_repeat_ngram_size=2,  # Запрет повторяющихся фраз
                    early_stopping=True
                )
            #decode
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            if prompt in response:
                response = response[len(prompt):].strip()
            else:
                response = full_response.split("Коуч:")[-1].strip()
            
            response = response.split("Пользователь:")[0].strip()

            #clean
            response = re.sub(r'http\S+', '', response)
            response = re.sub(r'\d{4}-\d{2}-\d{2}', '', response)
            response = re.sub(r'Блог:.*', '', response)
            response = re.sub(r'\n+', ' ', response)
            
            return response if response else "Расскажите подробнее о вашей ситуации."
        
        except Exception as e:
            return f"sorry, error: {e}"

neuro_service= NeuroService()
