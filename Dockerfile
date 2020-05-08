FROM python:3.8.0
RUN mkdir -p /usr/src/app
COPY ./* /usr/src/app/
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "index.py"]
