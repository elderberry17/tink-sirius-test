# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the files to the working directory in the container
COPY download_finetuned_model.py unzip_finetuned_model.py model_functionality.py chat_bot.py requirements.txt config.yaml /app/

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the download_model.py script
RUN python3 download_finetuned_model.py

# Run the unzip_model.py script
RUN python3 unzip_finetuned_model.py

# Specify the command to run the telegram_bot.py file
CMD ["python3", "chat_bot.py"]