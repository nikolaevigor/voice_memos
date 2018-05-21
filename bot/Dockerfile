FROM python:3.6.5


RUN mkdir /app
COPY ./bot /app/
RUN pip install -r /app/requirements.txt
WORKDIR /app

CMD python -u -m start_listening