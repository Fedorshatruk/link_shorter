FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y locales && \
    echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    python -m pip install poetry==1.3.1 && \
    poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN python -m pip install --upgrade pip && poetry install --no-root
COPY ./ /app/
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 80
