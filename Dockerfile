# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container with correct ownership
COPY --link --chown=1000 . .

# Create a cache directory for Hugging Face Hub and set permissions
RUN mkdir -p /tmp/cache/
RUN chmod a+rwx -R /tmp/cache/

# Set Hugging Face Hub cache directory environment variable
ENV HF_HUB_CACHE=HF_HOME

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1 PORT=7860

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
