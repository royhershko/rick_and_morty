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
cd yamls

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


## GitHub Actions Workflow for Rick and Morty App

The project includes a GitHub Actions workflow defined in `.github/workflows/deploy-to-k8s.yaml`. This workflow automates the process of building the Docker image, setting up a Kubernetes cluster using Kind, deploying the Rick and Morty application to this cluster, and testing its endpoints.

### Workflow Details

#### Jobs and Steps

1. **Checkout Code**
   - The workflow starts by checking out the code of the repository, making it available for subsequent steps.
2. **Set Up Docker Buildx**
   - Prepares the Docker Buildx environment, which enhances the building of Docker images with additional features.
3. **Build Docker Image**
   - Builds the Docker image for the Rick and Morty Flask application using the Dockerfile in the repository.
4. **Setup Kind**
   - Initializes a Kind cluster within the GitHub Actions runner. Kind creates a Kubernetes cluster by running containers as nodes.
5. **Load Docker Image to Kind**
   - Transfers the built Docker image into the Kind cluster, allowing it to be used for deployment.
6. **Apply Kubernetes Manifests**
   - Deploys the application to the Kind cluster by applying the Kubernetes manifests found in the `k8s/` directory of the repository.
7. **Check Deployment Rollout Status**
   - Ensures the deployment process completes successfully by monitoring the rollout status of the Kubernetes deployment.

8. **Test Application Endpoints**
   - Verifies the application's functionality by testing its endpoints. This step uses `curl` commands to make HTTP requests to the application's service within the Kind cluster.

### What Each Step Achieves

- **Build and Test Phases**: The initial steps focus on building the Docker image and setting up the Kubernetes environment, essential for running the application in a containerized manner.
- **Deployment Phase**: The application is deployed to the Kubernetes cluster, mimicking a production-like environment for testing.
- **Validation Phase**: The final step tests the application's endpoints, ensuring that the deployment was successful and the application behaves as expected in the Kubernetes environment.
