FROM sgoblin/python3.4

RUN git clone https://github.com/MahoneyT1/AirBnB_clone_v3.git
WORKDIR /root/AirBnB

RUN pip3 install --upgrade &&\
    pip3 install virtualenv

RUN pip install -r requirements.txt


EXPOSE 5000
