FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ENV=development \
    PORT=10000

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

ARG BUILD_SHA=local
ENV BUILD_SHA=${BUILD_SHA}

COPY app.py .

RUN useradd --create-home appuser
USER appuser

EXPOSE 10000

CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT} --workers 2 app:app"]
