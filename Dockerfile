FROM python

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install  --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "init_db.py"]