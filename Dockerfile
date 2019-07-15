FROM python:2.7.14-alpine3.6

# Update the packages
RUN apk update

# Install the ansible dependancies
RUN apk add gcc libffi-dev musl-dev openssl-dev sshpass make
# RUN apk add py-crypto python-dev

# Create td4a directory, copy files over and cd to it

RUN mkdir /td4a

COPY . /td4a

WORKDIR "/td4a"

# Install td4a
RUN python setup.py install

# Clear out extras
RUN rm -rf /var/cache/apk/*

# Start td4a
CMD [ "td4a-server" ]
