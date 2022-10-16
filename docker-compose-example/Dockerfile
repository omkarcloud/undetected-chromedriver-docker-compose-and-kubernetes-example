FROM ultrafunk/undetected-chromedriver:latest

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install  -r requirements.txt

RUN mkdir app
WORKDIR /app
COPY . /app

CMD ["python", "undetected-chromedriver.py"]