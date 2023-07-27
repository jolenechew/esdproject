FROM python:3.9
WORKDIR /usr/src/app
COPY twilio.reqs.txt amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r twilio.reqs.txt -r amqp.reqs.txt
COPY ./notification.py ./amqp_setup.py ./
CMD [ "python", "./notification.py" ]