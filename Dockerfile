FROM python:3.11-alpine

# Impede que o Python gere arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN set -x ; \
    addgroup -g 33 -S www-data || true ; \
    adduser -u 33 -D -S -G www-data www-data || true

WORKDIR /app
RUN chown www-data:www-data /app
COPY --chown=www-data:www-data . /app/


RUN apk add --no-cache gcc musl-dev linux-headers python3-dev libffi-dev
RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 8000

USER www-data
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo.wsgi:application"]

