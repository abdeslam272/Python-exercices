# Use the latest Python image
FROM python:latest

# Set the working directory
WORKDIR /app

# Copy the Jupyter Notebook file into the container
COPY Barcelona.ipynb .

# Install Jupyter and any other dependencies
RUN pip install jupyter notebook

# Specify the command to start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
