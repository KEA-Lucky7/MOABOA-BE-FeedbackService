FROM python:3.9

# Set work directory
COPY . /src
WORKDIR /src

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# EXPOSE PORT
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]