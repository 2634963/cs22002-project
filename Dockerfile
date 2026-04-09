# Use Python 3.12 (<= 3.11 has a bug in fstrings which breaks this project's code)
FROM python:3.12-slim

# Set working dir
WORKDIR /app

# Copy the project into the container
COPY . .

# Install all required dependencies
RUN pip install -r requirements.txt

# Run Flask at port 5000
EXPOSE 5000

CMD ["flask", "run", "-p", "5000", "--host=0.0.0.0", "--debug"]