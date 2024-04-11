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

## Deploying to Kubernetes using kubectl

To deploy the application to a Kubernetes cluster, follow these steps:

1. Apply the Kubernetes manifests:
```
kubectl apply -f Deployment.yaml
kubectl apply -f Service.yaml
kubectl apply -f Ingress.yaml
```

2. Access the application:
The application's endpoints will be accessible through the Ingress's IP or hostname. Use the following command to get the Ingress details and find the IP or hostname: `kubectl get ingress`
Once you have the Ingress IP or hostname, you can access the API endpoints. For example, if the Ingress IP is `192.168.99.100`, you can access the `/api/characters` endpoint at `http://192.168.99.100/rickandmorty/api/characters`.

## Deploying to Kubernetes using Helm

1. Package the Helm chart
```
cd helm
helm package rickandmorty
```

2. Install the packaged chart into your Kubernetes cluster:
```
helm install rickandmorty-release rickandmorty-0.1.0.tgz
```

## REST API Endpoints

- `GET /api/characters`  
  Returns a list of characters who are human, alive, and from Earth.

- `GET /api/characters/<char_id>`  
  Returns a single character matching the specified ID.

- `GET /healthcheck`  
  Returns the status of the application, useful for health monitoring.
