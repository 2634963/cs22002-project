# FessUp Internal Documentation

## Backend

The backend for this application is written in Python using the Flask framework.

### Routing

The site routing for the project is handled by app.py. It will serve any file available in the source tree, with a few exceptions:

* Access to the root is forbidden, due to the SQLite database being stored there.
* Access to the admin dashboard is gated, only if the user has a valid admin auth token will it be accessible.
* Any endpoint beginning with "admin" is gated, and are only accessible to users with a valid admin auth token.
* Any file beginning with "__" is forbidden. These are internal implementation details.

The MIME type of the file to send is also determined by the file extension on the backend.

[Back](../README.md)