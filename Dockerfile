FROM python:3.6.8-stretch
ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt
RUN /bin/bash -c "source common.env"

CMD ["python", "cron.py"]
