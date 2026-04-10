# FessUp Internal Documentation

## High-Level Structure

The system is composed of four independent components, which work together to form the final FessUp application.

These are:
* The frontend
* The backend
* The API
* The database

The frontend is composed of plain HTML, CSS and Javascript, and is what the user interacts with. It communicates with the backend through its API endpoints to enable the user to interact with the system.

The backend uses the Flask server software, and its primary job is to respond to API requests, acting as an intermediary between the frontend and the MySQL database, which actually stores all of the data required for the operation of the system.

The API is part of the backend and defines how the frontend should communicate with the backend.

The database is a traditional relational database using the SQLite library, and it handles the storage of all of the data used by the system. It contains data on users, posts, and comments.

## Component Documentation

Click:
* [Here](./frontend/README.md), for frontend documentation
* [Here](./backend/README.md), for backend documentation
* [Here](./api/README.md), for API documentation
* [Here](./database/README.md), for database documentation

[Back](../README.md)