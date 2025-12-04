#type: ignore
from transformers import AutoModelForCausalLM, AutoTokenizer
from ..config import settings
import torch
import re


class NeuroService:
        
    def __init__(self) -> None:
        self.model = None
        self.tokenizer = None
        self.is_loaded: bool = False

    async def load_model(self) -> None:
        try:
            #load_model
            self.tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_PATH)
            self.model = AutoModelForCausalLM.from_pretrained(
                    settings.MODEL_PATH,
                    dtype=torch.float16,
                    device_map="auto",
                    )
            
            self.is_loaded = True
         
        except Exception as e:
            raise Exception(f"error while load model: {e}")
        
    async def generate_response(self, message: str) -> str:
        if not self.is_loaded:
            await self.load_model()
        
        try:
            #tokenizer
            prompt = f"""
Ты — технический ассистент. Отвечай кратко и информативно.

Формат:
1. Прямой ответ на вопрос
2. Конкретные примеры если нужны
3. Без вводных слов и повторов

Если вопрос расплывчатый — уточни детали.
Если не знаешь — скажи "Не могу помочь с этим вопросом".

ВОПРОС ПОЛЬЗОВАТЕЛЯ:{message}

ОТВЕТ:
            """
            inputs = self.tokenizer(prompt, return_tensors="pt")
             
            #model
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=settings.MAX_LENGTH,
                    num_return_sequences=1,
                    temperature=settings.TEMPERATURE,
                    do_sample=settings.DO_SAMPLE,
                    pad_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=settings.REPETITION_PENALTY,
                )      
            #decode
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            if "ОТВЕТ:" in response:
                response = response.split("ОТВЕТ:")[-1].strip()

            response = re.sub(r'http\S+', '', response)
            response = re.sub(r'\d{4}-\d{2}-\d{2}', '', response)
            response = re.sub(r'Блог:.*', '', response)
            response = re.sub(r'\n+', ' ', response)
             
            return response if response else "Расскажите подробнее о вашей ситуации."
         
        except Exception as e:
            return f"sorry, error: {e}"

neuro_service = NeuroService()

