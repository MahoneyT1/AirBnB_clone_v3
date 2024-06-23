FROM ubuntu:20.04
WORKDIR /api

RUN  python3.4 -m pip install --upgrade 
# Ensure pip is up-to-date
RUN apt install python3

# Copy the current directory contents into the container at /api
COPY . .

# Create a virtual environment
RUN python3 -m venv -p python3.8 /opt/venv
RUN /opt/venv/bin/

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"
EXPOSE 5000
COPY .env .env

CMD [ "python3", "app.py" ]