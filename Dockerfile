# syntax=docker/dockerfile:1
FROM python:3.7
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
RUN python3 -m pip install -r requirements.txt
COPY . /app/

# RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
#     chown -R appuser /app
# USER appuser

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi"]
