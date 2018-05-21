FROM python:3.6.5


RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
COPY ./ /app/

CMD python -u -m start_listening