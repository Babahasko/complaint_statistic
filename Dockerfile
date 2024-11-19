FROM python:3.12
WORKDIR /app

# Add code and project dependencies
COPY requirements.txt ./
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app