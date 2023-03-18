FROM python

WORKDIR /usr/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

CMD ["python", "-m","main.py"]

