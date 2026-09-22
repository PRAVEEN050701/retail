FROM python:3.14-slim

WORKDIR /app

COPY app/ /app/

RUN useradd -m appuser

USER appuser

EXPOSE 8081

HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8081/health')" || exit 1

CMD ["python", "app.py"]