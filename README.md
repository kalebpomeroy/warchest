
First time setup for getting python on your machine


https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-20-04
https://www.freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04/

`pip3 install virtualenvwrapper`
`vim .bashrc`

```export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=/home/<your-user-name>/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh```

`mkvirtualenv warchest`
`which python`

`git clone git@github.com:kalebpomeroy/warchest.git`
`pip install -r requirements.txt`
`flask run`

 This starts [flask](https://flask.palletsprojects.com/en/2.1.x/) running. By
 default, it looks for `app.py` and runs that. It starts a server and stays
 running until you turn it off. It handles all of the HTTP connections for you
 and gives a very consistent and clean way to interact with your application.

With that running you should be able to go to http://localhost:5000 and see the
`Hello, World` text in your browser. This is the core of how all websites work.
Instead of responding with just simple text, modern websites respond with HTML,
Javascript and CSS. Those are important to make it look nice, but don't have any
functional application for the work we'll be doing. You can play around by
putting some of those routes in your browser and seeing your application do
different things for each one.

While this works for humans with a browser, we're actually going to be building
a [REST API](https://www.mindinventory.com/blog/best-practices-rest-api-development/)
that will allow us to communicate with our server in a similar way, but not with
a browser. Instead, we'll use a different client to make requests and manipulate
the data.

`curl http://localhost:5000/hello/robot`
