Usage
-----

    sudo pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:80
    # Or whatever port you want to start dev server on
    # Make sure nothing else is running on that port

Populating the database
-----------------------

We worked hard collecting and scraping data from different sources, geocoding data to get exact location information.
This additional data needs to be inserted into the database separately.


    # Get initial data into the database
    python trasfer_data.py

    # Adding names of majors corresponding to major info
    python import_majors.py

    python import_books.py

    # Coordinates for each building at OSU pouplated into the database. (lat, lon)
    python import_coordinates.py