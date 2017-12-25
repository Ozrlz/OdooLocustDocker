FROM python:2.7

RUN git clone https://github.com/nseinlet/OdooLocust.git /home/ && cd /home/ && \
        pip install -r requirements.txt && \
        python setup.py build && \
        python setup.py install

ADD ./tests/ /home/OdooLocust/tests/

WORKDIR /home/OdooLocust/tests/

EXPOSE 8089

CMD ["locust", "-f", "Manager.py", "Manager"]
