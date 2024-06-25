FROM sgoblin/python3.4

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/MahoneyT1/AirBnB_clone_v3.git
WORKDIR /root/AirBnB

RUN pip install --upgrade pip && pip install virtualenv

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

FROM python:3.4

# Install system dependencies


# Clone your repository and set up working directory
RUN git clone https://github.com/MahoneyT1/AirBnB_clone_v3.git ~/AirBnB
WORKDIR /root/AirBnB

# Install pipenv
RUN pip install --upgrade pip && pip install virtualenv

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt