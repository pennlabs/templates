FROM python:3-slim

MAINTAINER Penn Labs

# Install build dependencies
RUN apt-get update && apt-get install --no-install-recommends -y default-libmysqlclient-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install pipenv 

WORKDIR /app/

# Copy project dependencies
COPY Pipfile* /app/

# Install project dependencies
RUN pipenv install --system

# Copy project files
COPY . /app/
COPY --from=frontend /app/build/ /app/frontend/build/

# Collect static files
RUN python /app/manage.py collectstatic


ENTRYPOINT ["python", "/app/manage.py", "migrate", "--noinput"]

CMD ["uwsgi", "--ini", "/app/setup.cfg"]
