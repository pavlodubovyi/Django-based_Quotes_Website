# Start with a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the Poetry files first for dependency resolution
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Make migrations and run Django
CMD ["poetry", "run", "python3", "quotes_site/manage.py", "runserver", "0.0.0.0:8000"]