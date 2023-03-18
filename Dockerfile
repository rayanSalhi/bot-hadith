FROM python

WORKDIR /usr/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

END ("python", "-m","main.py")

