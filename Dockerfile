FROM python:3.9

LABEL maintainer="vashchukmaksim@gmail.com"

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

EXPOSE 8000

COPY ./main.py /home/root/app/main.py
COPY ./.env /home/root/app/.env

WORKDIR /home/root/app
CMD ["python", "main.py"]
