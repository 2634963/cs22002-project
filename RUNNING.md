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

To run the project in a Docker container, run the following commands in the root of the repository:

```bash
docker build -f Dockerfile -t cs22002-project .
docker run --network=host -p 3000:3000 cs22002-project
```

#### Podman

To run the project in a Podman container, run the following commands in the root of the repository:

```bash
podman build -f Dockerfile -t cs22002-project .
podman run --network=host -p 3000:3000 cs22002-project
```

### Standalone

The project supports running on both Windows and POSIX systems (Linux, macOS, etc).

#### POSIX

To run on POSIX systems (Linux, macOS, etc), switch to the root of the repository and run the following command:

```bash
python3 ./run-nix.py
```

#### Windows

To run on Windows, switch to the root of the repository and run the following command:

```powershell
python3 .\run-win.py
```

## Connecting

To connect to the now running server, connect to the following URL in your browser:

```url
http://127.0.0.1:3000
```