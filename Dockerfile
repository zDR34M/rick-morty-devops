FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
