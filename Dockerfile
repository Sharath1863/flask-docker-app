# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the Flask application code
COPY app.py app.py

# Install Python dependencies inline
RUN pip install flask

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
