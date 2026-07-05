# Use a lightweight Python base image
FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output is sent straight to terminal (useful for logging)
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your local Django project files into the container
COPY . /app/

# Expose port 8080 (the port Back4App Containers expects)
EXPOSE 8080

# When the container starts, run migrations, then start the Gunicorn server
CMD python manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:8080