FROM python:3.11

# Set working directory to where manage.py lives
WORKDIR /app/my_blog

# Copy everything (outer folder) into container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ensure Python can find inner my_blog module
ENV PYTHONPATH=/app/my_blog/my_blog

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_blog.wsgi:application"]