# Start from Python 3.10 base image
FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gconf-service \
    libasound2 \
    libatk1.0-0 \
    libcairo2 \
    libcups2 \
    libfontconfig1 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libpango-1.0-0 \
    libxss1 \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    wget \
 && rm -rf /var/lib/apt/lists/*


# Set environment variables
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

# Set working directory
WORKDIR $APP_HOME

# Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the application
CMD ["uvicorn", "app.main:app", "--workers", "1", "--port", "8080", "--host", "0.0.0.0"]