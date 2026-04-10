# FessUp Internal Documentation

## API

All API endpoints in this application either accept JSON, return JSON, or both.

They are named in camelCase, despite initially being designed in kebab-case, due to the reliance on the Python module system to expose endpoints,
and the lack of hyphen support in it.

The following API endpoints are implemented:

### /api/login

#### Method

POST

#### Accepts

* username
* password

#### Returns

* authToken cookie

[Back](../README.md)