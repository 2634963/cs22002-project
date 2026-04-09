# FessUp

## Prerequisites

To run this project in its entirety, the following software is required:
* Python 3
* Python Requests Library
* Flask
* A modern web browser with JavaScript enabled

Additionally, to run the project in a container:
* Docker or Podman

## Running

The application can be run either in a container, or standalone.

### Containerised (Recommended)

The application can be run in either a Docker or Podman container.

#### Docker

To run the project in a Docker container, run the following commands:

```bash
docker build -f Dockerfile -t cs22002-project .
docker run -p 5000:5000 cs22002-project
```

#### Podman

To run the project in a Podman container, run the following commands:

```bash
podman build -f Dockerfile -t cs22002-project .
podman run -p 5000:5000 cs22002-project
```

### Standalone (Windows)

To run the project, switch to the root of the repository and run the following command:
```powershell
python3 ./run.py
```