FROM python:3.11-slim

LABEL maintainer="tu-email@ejemplo.com"
ENV ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    curl gnupg2 apt-transport-https apt-utils \
    build-essential unixodbc-dev \
 && echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
 && apt-get remove -y libodbc2 libodbcinst2 unixodbc-common odbcinst || true \
 && apt-get -f install -y \
 && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
      | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] \
      https://packages.microsoft.com/debian/11/prod bullseye main" \
    > /etc/apt/sources.list.d/mssql-release.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends msodbcsql18 \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

COPY . .
RUN adduser --disabled-password --gecos '' appuser \
 && chown -R appuser:appuser /app

USER appuser
EXPOSE 8000
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
