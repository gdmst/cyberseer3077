FROM python:3.8.0
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
RUN mkdir -p /usr/src/app/static/font
RUN mkdir -p /usr/src/app/templates
COPY ./* /usr/src/app/
COPY ./templates/* /usr/src/app/templates/
COPY ./static/* /usr/src/app/static/
COPY ./static/font/* /usr/src/app/static/font/
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "index.py"]