# Rick and Morty App

This application serves as a simple backend to interact with the Rick and Morty API, providing information about characters.

## Running Locally

To run the application locally, you need Python installed on your machine. Follow these steps:

1. Clone the repository:
```
git clone https://github.com/royhershko/rick_and_morty
cd rick_and_morty
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python app.py
```
The application will start running on `http://localhost:5000`.

## Running with Docker

To run the application using Docker, follow these steps:

1. Build the Docker image:
```
docker build -t rickandmorty-flask-app .
```
3. Run the Docker container:
```
docker run -p 5000:5000 rickandmorty-flask-app
This will start the application inside a Docker container and make it accessible on `http://localhost:5000`.
```

## REST API Endpoints

- `GET /api/characters`  
  Returns a list of characters who are human, alive, and from Earth.

- `GET /api/characters/<char_id>`  
  Returns a single character matching the specified ID.

- `GET /healthcheck`  
  Returns the status of the application, useful for health monitoring.
