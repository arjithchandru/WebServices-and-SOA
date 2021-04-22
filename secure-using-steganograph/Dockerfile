FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get -y install python3.6 python3-pip
ENV LANG C.UTF-8
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get -y install libpq-dev
COPY alg_apply.py /opt/ 
COPY forms.py /opt/
COPY requirements.txt /opt/
COPY static /opt/static
COPY app.py /opt/
COPY templates /opt/templates
WORKDIR /opt/
RUN pip3 install -r requirements.txt
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080