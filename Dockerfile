FROM python:3.6.8-stretch
ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

ENV TZ='Asia/Tokyo'

CMD ["python", "cron.py"]
