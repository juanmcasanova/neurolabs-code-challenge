# Using this as a base for ease, in a more real project it would be better to create a fork to
# ensure the image is updated and to customize it exactly as needed (for example, we would be able
# to actually use Python 3.10)
FROM thecodingmachine/nodejs:v2-18-bullseye

USER root

# Install Pip (https://pip.pypa.io/en/stable/)
RUN apt-get update && apt-get install -y python3-pip

# Install pipenv (https://github.com/pypa/pipenv)
RUN pip3 install pipenv

USER docker
