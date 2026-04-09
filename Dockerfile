# Use Python 3.12 (<= 3.11 has a bug in fstrings which breaks this project's code)
FROM python:3.12-slim

# Set working dir
WORKDIR /app

# Copy the project into the container
COPY . .

# Install all required dependencies
RUN pip install -r requirements.txt

# Run Flask at port 3000
EXPOSE 3000
CMD ["python3", "run-nix.py"]