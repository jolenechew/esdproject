FROM python:3-slim
WORKDIR /usr/src/app
COPY stripe.reqs.txt amqp.reqs.txt http.reqs.txt ./
RUN python -m pip install --no-cache-dir -r stripe.reqs.txt -r amqp.reqs.txt -r http.reqs.txt
COPY ./payment.py ./amqp_setup.py ./
CMD [ "python", "./payment.py" ]
