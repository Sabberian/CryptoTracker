# CryptoTracker

CryptoTracker is an educational project showcasing a FastAPI backend with Docker containerization and a React frontend. The project follows a microservices architecture. Key features include:

- **Backend Architecture:** FastAPI for the backend, utilizing SQLAlchemy for database operations.
- **Frontend Technology:** React for the web interface.
- **Containerization:** Docker is used for containerization, simplifying deployment and ensuring consistency across environments.

## Project Functions

- **Cryptocurrency Tracking:** Monitor cryptocurrency prices in real-time by the 1 hour timescale.
- **Notification System:** Set thresholds for specific cryptocurrencies and receive email notifications when they are reached.
- **Custom Currency Support:** Add your custom currency to the API via [http://localhost:8080/api/currency/](http://localhost:8080/api/currency/).
- **Interactive Documentation:** Explore API endpoints and usage details at [http://localhost:8080/docs](http://localhost:8080/docs).

## Getting Started

**Prerequisites:**
    Ensure that Docker and Docker Compose are installed on your machine.
    
### Setting up the Backend

1. Navigate to the `/backend` directory.
2. Create a `.env` file with the following content:
    ```
    JWT_SECRET_KEY=your_secret_key
    EMAIL_PASSWORD=your_email_password
    ```
   Replace `your_secret_key` with any string for JWT token encryption and `your_email_password` with your third-party application email password in the format "hell owor ldhe llow" (four words separated by spaces).

### Running the Project

1. Open a terminal and navigate to the project root directory.
2. Run the following command to build and start the Docker containers:
    ```
    docker-compose up --build
    ```
3. The application will be accessible at [http://localhost:3000](http://localhost:3000).

Explore the API and web interface at [http://localhost:3000](http://localhost:3000). For detailed API documentation, visit [http://localhost:8080/docs](http://localhost:8080/docs).
