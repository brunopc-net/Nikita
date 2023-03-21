FROM python:3.11-alpine

# Defining the Author
MAINTAINER Bruno PC

# Using non-root user
RUN adduser -D python
USER python

#Create a working directory
WORKDIR /home/python

# Add the source code into the image
COPY --chown=python:python . .

# Install requirements
ENV PATH="/home/python/.local/bin:${PATH}"
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# Adding src to python path
ENV PYTHONPATH "${PYTHONPATH}:/src"

#Keep the container running before execution
ENTRYPOINT sleep infinity