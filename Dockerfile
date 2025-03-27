# Use Python as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (use Keyeb’s secret management)
ENV INSTAGRAM_USERNAME=""
ENV INSTAGRAM_PASSWORD=""
ENV INSTAGRAM_APP_ID=""
ENV INSTAGRAM_APP_SECRET=""

# Run the bot
CMD ["python", "main.py"]
