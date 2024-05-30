# Crypto aggregator

## Overview

The project aims to provide aggregated cryptocurrency data from different platforms, calculate potential profits, and display the best deals for transactions.

## Features

- Fetch cryptocurrency prices from multiple platforms.
- Calculate potential profits for different platform combinations.
- Display aggregated data with the best deals for transactions.

## Technologies Used

- Django: Web framework for building the backend server.
- PostgreSQL: Database management system for storing cryptocurrency data.
- Python: Programming language used for backend development.
- HTML/CSS: Frontend technologies for displaying web pages.
- Docker: Containerization tool for managing development and deployment environments.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database:
   
    - Install PostgreSQL on your system.
    - Create a database named `crypto_db`.
    - Set up the database user and password.

5. Configure environment variables:
   
    Create a `.env` file in the project root directory and add the following:

    ```plaintext
    DJANGO_SETTINGS_MODULE=crypto.settings
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the application in your web browser at `http://localhost:8000`.

## Structure

- **crypto/**: Main Django application directory.
  - **models.py**: Defines database models.
  - **views.py**: Contains view functions for handling HTTP requests.
  - **urls.py**: Maps URL patterns to view functions.
  - **templates/**: Contains HTML templates for rendering web pages.
  - **tests.py**: Unit tests for testing application functionality.
- **requirements.txt**: List of Python dependencies.
- **docker-compose.yml**: Docker Compose configuration file for defining services.
- **Dockerfile**: Dockerfile for building the application image.

## Code Examples

### Fetching Cryptocurrency Prices

```python
# crypto/services.py

def fetch_prices(symbol):
    # Implementation to fetch cryptocurrency prices from different platforms
    pass
```

### Calculating Profit

```python
# crypto/views.py

def calculate_profit(request, symbol, amount):
    # Implementation to calculate potential profits for different platform combinations
    pass
```

### Aggregated Data View

```python
# crypto/views.py

def aggregated_data_view(request):
    # Implementation to display aggregated cryptocurrency data with the best deals
    pass
```

## Testing

Run unit tests:

```bash
python manage.py test
```

Ensure all tests pass before deploying the application.

## Deployment

Build Docker images:

```bash
docker-compose build
```

Start Docker containers:

```bash
docker-compose up
```

Access the deployed application in your web browser at [http://localhost:8000](http://localhost:8000).

## Credits

Developed by [Your Name]

Inspired by [Source/Resource]

## License

This project is licensed under the [License Name] License.
