# FessUp Internal Documentation

## Frontend

The frontend for this application is written in plain HTML, CSS and Javascript.

### Structure

The core structure of each page is defined with HTML5 files in the pages/ directory.

### Styling

Styling for this application is handled exclusively by external CSS stylesheets, located in the stylesheets/ directory.

There is a common stylesheet for every page, along with extra stylesheets for each unique component, such as the navbar and login container.

### Functionality

Frontend functionality is handled by scripts written in JavaScript, located in the scripts/ directory. For example, to login

### Templating

We have a very barebones templating system, used to include common elements such as the navbar in every page.

The templating system is written in JavaScript, runs on the frontend, and is just a single function which takes the path of the HTML to include, and the element ID to include it in.

The reason a more advanced templating system such as Jinja was not used is because only very simple templating tasks are performed, such as including a navbar in all pages,
and the extra overhead would adversely affect performance for no gain.

### API Communication

The frontend communicates with the API by using the modern JavaScript ```fetch()``` function.

[Back](../README.md)