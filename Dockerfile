FROM ubuntu 
WORKDIR /api

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.4 python3.4-venv python3.4-dev python3-pip

# Ensure pip is up-to-date
RUN python3.4 -m pip install --upgrade pip

# Copy the current directory contents into the container at /api
COPY . .

# Create a virtual environment
RUN python3.4 -m venv /opt/venv
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY .env .env

CMD [ "python3", "app.py" ]