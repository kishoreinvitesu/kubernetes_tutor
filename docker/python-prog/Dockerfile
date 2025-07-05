FROM python:3.11-slim

WORKDIR /app

COPY sample-py-program.py .

RUN pip install --no-cache-dir pillow

CMD [ "python", "sample-py-program.py" ]