FROM arm32v7/python:3

# Set the working directory
WORKDIR /hal

# Install necessary system-level packages for I2C and SMBus
RUN apt-get update && apt-get install -y \
    python3-smbus \
    i2c-tools

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip3 install flask RPi.GPIO smbus

# Expose the API port
EXPOSE 8000

# Command to run the HAL API
CMD ["python", "hal_api.py"]
