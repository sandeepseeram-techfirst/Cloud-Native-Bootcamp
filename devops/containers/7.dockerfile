FROM alpine:3.11
EXPOSE 5000
MAINTAINER SANDEEP KUMAR SEERAM "seerams@acm.org"

VOLUME ["/app/data"]

# Install python, pip and basic utilities
RUN apk add -U \
        python \
        py-pip \
        ca-certificates \
  && rm -rf /var/cache/apk/* \
  && pip install --no-cache-dir \
          setuptools \
          wheel

ADD . /app
WORKDIR /app
RUN pip install --requirement ./requirements.txt

CMD [ "python", "./local/data.py" ]