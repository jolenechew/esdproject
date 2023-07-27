FROM python:3.9
WORKDIR /usr/src/app
COPY stripe.reqs.txt amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r stripe.reqs.txt -r amqp.reqs.txt
COPY ./refund.py ./amqp_setup.py ./invokes.py  ./
CMD [ "python", "./refund.py" ]