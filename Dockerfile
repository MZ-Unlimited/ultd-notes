ARG PYTHON_VERSION=3.12-slim

#Prepare base image with OpenSSL Self-signed Certificates.
FROM python:${PYTHON_VERSION} as base
# ARG DOMAIN_NAME=localhost
# ARG DAYS_VALID=1825

WORKDIR /var/task/notes

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/var/task/notes:${PYTHONPATH}"
ENV RUNNING_OS=Type1

# Process requirements
COPY requirements requirements
RUN pip install pip-tools
RUN pip-compile requirements/requirements.in
RUN pip install -r requirements/requirements.txt

COPY . /var/task/notes
RUN chmod +x startup.sh

ENTRYPOINT ["./startup.sh"]
