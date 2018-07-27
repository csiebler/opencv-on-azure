FROM jjanzic/docker-python3-opencv:latest

RUN mkdir /opencv; pip install azure-storage

COPY *.py /opencv/
COPY run.sh /opencv/

WORKDIR /opencv

ENTRYPOINT ["./run.sh"]