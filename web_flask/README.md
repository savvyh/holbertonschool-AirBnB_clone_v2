# AirBnB clone - Web framework
![image](https://github.com/savvyh/holbertonschool-AirBnB_clone_v2/assets/139894873/df449852-06a0-4ffb-8da5-ca3505fe4dfa)

# General :bell_pepper:
This project will cover understanding what a Web Framework is, learning how to build a web framework using Flask, defining routes in Flask, understanding the concept of routes, handling variables within routes, understanding templates, creating an HTML response in Flask using a template, creating dynamic templates with loops and conditions, and displaying data from a MySQL database in HTML.
![image](https://github.com/savvyh/holbertonschool-AirBnB_clone_v2/assets/139894873/cffa85f8-5f68-432b-9f0b-017fd32c7bca)

## Requirements 👍
Python Script :
* We are not allowed to import module.
* Respect the pycodestyle.
* All files must be executable.
* Use #!/usr/bin/python3.
* The shell should work like this in interactive mode but also in non-interactive mode.

HTML/CSS Files : 
* All files should end with a new line.
* The code should be W3C compliant and validate with W3C-Validator.
* All CSS files should be in the styles folder.
* All images should be in the images folder.
* Not allowed to use !important or id (#... in the CSS file)
* All tags must be in uppercase

Install Flask : 
`$ pip3 install Flask`

## Tasks :clapper:
0. Hello Flask ! 
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Route `/`: display “Hello HBNB!”
    - Use the option `strict_slashes=False in the route definition

1. HBNB
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Route `/`: display “Hello HBNB!”
    - Route `/hbnb` : display “HBNB”
    - Use the option `strict_slashes=False` in the route definition

2. C is fun!
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Route `/`: display “Hello HBNB!”
    - Route `/hbnb`: display “HBNB”
    - Route `/c/<text>`: display “C ” followed by the value of the text variable (replace underscore `_` symbols with a space "")
    - Use the option `strict_slashes=False` in the route definition

3. Python is cool!
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Route `/`: display “Hello HBNB!”
    - Route `/hbnb`: display “HBNB”
    - Route `/c/<text>`: display “C ” followed by the value of the text variable (replace underscore `_` symbols with a space "")
    - Route `/python/<text>`: display “Python ”, followed by the value of the text variable (replace underscore `_` symbols with a space "")
        - The default value of `text` is “is cool”
    - Use the option `strict_slashes=False` in the route definition

4. Is it a number?
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Route `/`: display “Hello HBNB!”
    - Route `/hbnb`: display “HBNB”
    - Route `/c/<text>`: display “C ” followed by the value of the text variable (replace underscore `_` symbols with a space "")
    - Route `/python/<text>`: display “Python ”, followed by the value of the text variable (replace underscore `_` symbols with a space "")
        - The default value of `text` is “is cool”
    - Route `/number/<n>`: display “n is a number” only if `n` is an integer
    - Use the option `strict_slashes=False` in the route definition.

5. Number template
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Route `/`: display “Hello HBNB!”
    - Route `/hbnb`: display “HBNB”
    - Route `/c/<text>`: display “C ” followed by the value of the text variable (replace underscore `_` symbols with a space "")
    - Route `/python/<text>`: display “Python ”, followed by the value of the text variable (replace underscore `_` symbols with a space "")
        - The default value of `text` is “is cool”
    - Route `/number/<n>`: display “n is a number” only if `n` is an integer.
    - Route `/number_template/<n>`: display a HTML page only if `n`  is an integer:
        - H1 tag: “Number: n” inside the tag BODY
    - Use the option `strict_slashes=False` in the route definition.

6. Odd or even?
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Route `/`: display “Hello HBNB!”
    - Route `/hbnb`: display “HBNB”
    - Route `/c/<text>`: display “C ” followed by the value of the text variable (replace underscore `_` symbols with a space "")
    - Route `/python/<text>`: display “Python ”, followed by the value of the text variable (replace underscore `_` symbols with a space "")
        - The default value of `text` is “is cool”
    - Route `/number/<n>`: display “n is a number” only if `n` is an integer.
    - Route `/number_template/<n>`: display a HTML page only if `n`  is an integer:
        - H1 tag: “Number: n” inside the tag BODY
    - Route `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer:
        - H1 tag: “Number: n is even|odd” inside the tag BODY
    - Use the option `strict_slashes=False` in the route definition.

7. Improve engines
    - Before using Flask to display HBNB data, update `FileStorage`, `DBStorage` and `State`.

8. List of states
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
    - After each request remove the current SQLAlchemy Session.
    - Import `100-hbnb.sql`
    - Use the option `strict_slashes=False` in the route definition.

9. Cities by states
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Load all cities of a `State`
    - After each request remove the current SQLAlchemy Session.
    - Routes : 
        - `/cities_by_states` : display a HTML page: (inside the tag BODY)
            - H1 tag: “States”
            - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
            - LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name
            - LI tag: description of one City: <city.id>: <B><city.name></B>
    - Use the option `strict_slashes=False` in the route definition.

10. States and State
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Load all cities of a `State`
    - After each request remove the current SQLAlchemy Session.
    - Routes : 
        - `/states`: display a HTML page: (inside the tag BODY)
            - H1 tag: “States”
            - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
            - LI tag: description of one State: <state.id>: <B><state.name></B>
        - `/states/<id>`: display a HTML page: (inside the tag BODY)
            - If a State object is found with this id:
            - H1 tag: “State: ”
            - H3 tag: “Cities:”
            - UL tag: with the list of City objects linked to the State sorted by name (A->Z)
            - LI tag: description of one City: <city.id>: <B><city.name></B>
        - Otherwise:
            - H1 tag: “Not found!”
    - Use the option `strict_slashes=False` in the route definition.

11. HBNB filters
    - Write a script that starts a Flask web application
    - Application must be listening on `0.0.0.0`, port `5000`
    - Load all cities of a `State`
    - After each request remove the current SQLAlchemy Session.
    - Routes : 
        - `/hbnb_filters`: display a HTML page from  `0x01. AirBnB clone - Web static`
            - Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles
            - Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images
            - Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.
            - Use 6-index.html content as source code for the template 10-hbnb_filters.html
            - State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)
    - Use the option `strict_slashes=False` in the route definition.

## Authors 🧞‍♀️
Sarah Boutier 
