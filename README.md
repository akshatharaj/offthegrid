# OffTheGrid 

OffTheGrid(SF) is a Django application that fetches vendors info (from their website)
and their events (from their facebook page), stores that data in MySQL and presents 
that information compiled in a useful format for the user. Use this site to check 
upcoming events, vendors showing in those events and such.


## Installation

### Clone the repository

    $ cd ~/Code
    $ git clone git@github.com:akshatharaj/offthegrid.git

### Make a new virtual environment

    $ virtualenv --no-site-packages --distribute ~/Code/env
    $ cd ~/Code/env
    $ . bin/activate
    $ pip install -U distribute

### Install offthegrid and all its dependencies

    $ cd ~/Code/offthegrid
    $ ./build.bash develop
    $ pip install requirements.txt

Also, please edit the settings file to add database connection settings

### Then run

    $ python manage.py migrate
    $ python manage.py fetchdata (this loads all vendor and event info into database)


### Functionality
    Event listing page (which is also the home page) shows a listing of all upcoming events.
    Clicking on any one event shows complete event information and participating vendors. 
    Clicking on one of the participating vendors display complete vendor information and events
    the vendor has participated at (most recent first).

    There is also a vendor listing page that displays all vendors (ones that participated in most
    events in the last month first). Clicking on one of the vendors displays complete vendor information

