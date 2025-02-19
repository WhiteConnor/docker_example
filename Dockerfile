# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Update and install Python and necessary development tools
RUN apt-get update && \
  apt-get install -y python3 python3-pip python3-setuptools python3-dev python3-wheel

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first, to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN apt-get install -y $(grep -Eo '^\S+' requirements.txt | xargs)

# Copy the current directory contents into the container at /app
COPY . /app

# Run app.py when the container launches
CMD ["python3", "script.py"]
