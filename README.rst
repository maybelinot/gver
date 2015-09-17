
INSTALLATION
============
Example install, using VirtualEnv::

    # install/use python virtual environment
    virtualenv ~/virtenv_scratch --no-site-packages

    # activate the virtual environment
    source ~/virtenv_scratch/bin/activate

    # upgrade pip in the new virtenv
    pip install -U pip setuptools

    # install this package in DEVELOPMENT mode
    python setup.py develop

    # or simply install
    # python setup.py install

ACCESS CREDENTIALS
==================
To allow a script to use Google Drive API we need to authenticate our self 
towards Google.  To do so, we need to create a project, describing the tool 
and generate credentials. Please use your web browser and go to 
`Google console <https://console.developers.google.com>`_ and :

* Click on the button **"Create Project"**.

* A dialog box appears, so give your project a name and an ID and click on **"Create"** button.

* In section **"Boost your app with a Google API"** click on **"Enable an API"** button.

* A table of available APIs is shown. Switch **"Drive API"** to **"ON"** state. Other APIs might be switched off, for our purpose.

* On the left-side menu click on **"APIS & auth"** -> **"Credentials"**.

* In section **"OAuth"** click on **"Create new client ID"** button
      
* A dialog box appears. Select **"Installed application"** item and click on **"Configure consent screen"**.

* From drop-down box select your email address and give your product a name. Then click on **"Save"** button.

* A dialog box  **"Create Cliend ID"** appears. Select **"Installed application"** item as "APPLICATION TYPE" and **"Other"** item as "INSTALLED APPLICATION TYPE".

* Click on **"Create Client ID"** button.

* Click on **"Download JSON"** button and store the downloaded file on your file system. Please be aware, the file contains your private credentials, so take care of the file in the same way you care of your private SSH key; i.e. move downloaded JSON file to **~/.gdrive_private**. 

* Then, the first time you run it your browswer window will open a google authorization request page. Approve authorization and then the credentials will work as expected.
