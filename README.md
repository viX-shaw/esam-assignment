ESAM
-----------------------------

ABOUT
    
    Take Home Assignment from eSamudaay

    The application uses FastAPI, web framework for building APIs
    with Python 3.6+ based on standard Python type hints.

    Data validation out of the box using models was the core
    feature for which the framework was chosen.


DEPENDENCIES

    Use a virtual environment to setup the following deps

    $ python3 -m venv ~/esam
    $ source ~/esam/bin/activate

    Use the requirements.txt file to install the deps

    $ pip install -r requirements.txt

RUN

    $ uvicorn server:app --host 127.0.0.1 --port 9001

    For running the server we use an ASGI server named uvicorn
    Try out the API at localhost:9001/docs FastAPI generates out of the box
    for quick testing.