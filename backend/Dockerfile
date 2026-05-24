FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install kaggle

COPY . .

EXPOSE 7860

CMD ["sh", "-c", "python train.py && uvicorn main:app --host 0.0.0.0 --port 7860"]