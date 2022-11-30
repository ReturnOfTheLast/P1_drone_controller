FROM python:3.10

RUN pip install flask djitellopy

COPY . .

CMD python app.py
