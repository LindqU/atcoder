FROM python:3.11-slim-buster

# Install necessary packages
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    expect \
    && rm -rf /var/lib/apt/lists/*

# Install AtCoder CLI and online-judge-tools
RUN npm install -g atcoder-cli
RUN pip install online-judge-tools

COPY requirements.txt requirements.txt

# Install Python libraries
RUN pip install -r requirements.txt

# Copy helper scripts and core directory
COPY atcoder_helper.py /usr/local/bin/atcoder_helper.py
COPY core /usr/local/lib/python3.8/site-packages/core
RUN chmod +x /usr/local/bin/atcoder_helper.py

# Create contests directory
WORKDIR /atcoder
RUN mkdir -p contests

# Set environment variables
ENV ATCODER_USERNAME=""
ENV LANGAGE=""