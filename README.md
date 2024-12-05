# Quotes Website on Django
This project is a Django-based web application inspired by the site [Quotes to Scrape](https://quotes.toscrape.com/), with additional features and functionalities.

## Features
### User Registration and Authentication
- Users can register and log in to the website.
### Author and Quote Management
- Registered users can add new authors to the website.
- Registered users can also add new quotes and associate them with existing authors.
### Public Access
- The list of quotes and individual author pages are available for viewing without requiring user authentication.
### Additional Features
- Tags: Clicking on a tag displays all quotes associated with it.
- Pagination: Users can navigate through the list of quotes using "Next" and "Previous" buttons.

## Running the Project with Docker
To run this project using Docker, follow these steps:

1. Ensure Docker is installed on your machine.
You can download it from [Docker's official website](https://www.docker.com/get-started).

2. Clone this repository.
```bash
git clone <repository-url>
cd <repository-name>
```
3. Create a `.env` file in the root of the project and provide the necessary configuration. An example `.env` file:
```dotenv
# Django
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL
DB_NAME=authors_and_quotes
DB_USER=your-db-username
DB_PASSWORD=your-db-password
DB_HOST=db
DB_PORT=5432

# Email configuration
EMAIL_USER=your-email@example.com
EMAIL_PASS=your-email-password
SMTP_SERVER=smtp.example.com
EMAIL_PORT=587
FRONTEND_URL=http://127.0.0.1:8000
SITE_NAME=Quotes Website
```
4. Run Docker Compose.
In the root directory, where the `docker-compose.yml` file is located, execute:
```bash
docker compose up --build
```
5. Access the Website.
Once the containers are running, the site will be available at:
http://127.0.0.1:8000/
6. Stop the Containers.
To stop the application, press `Ctrl+C` or run:
```bash
docker compose down
```

## Notes
Email functionality (e.g., for password reset) is configured using the environment variables in the `.env` file.
The project uses PostgreSQL as its database. You must already have the database created.

### Migrate the database schema
If the database is empty, run the following after starting the containers:

```bash
docker compose exec web poetry run python manage.py migrate
```
### Create a superuser
To access the Django admin panel, create a superuser:
```bash
docker compose exec web poetry run python manage.py createsuperuser
```
### Stop and remove containers
To stop and clean up Docker containers:
```bash
docker compose down
```


