Key creation and running the data upload script
===============================================

# Key generation:

This creates a new key, using your email as the label, with the
RSA encryption algorithm

## Linux/OSX:
`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

-t tells us what type to create, in our case, we will use rsa protocol version 2, it is a key that will work everywhere.
-b is the number of bits

Next, you will be prompted to enter a file to save the key.  For most purposes, the .ssh/ folder under the home
folder is the default and will suffice.

Finally, you will be asked to enter a passphrase.  Press enter to skip this process and continue without a pass phrase


## Windows:
Please download [PuTTYgen](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

1. Open the PuTTYgen program.
2. Select "SSH-2 RSA" for "Type of key to generate".
3. Click the "Generate" button.
4. Move the mouse below the progress bar until it is full.
5. Type a passphrase (optional).
6. Click the "Save private key" button.
7. Copy down the public key to be shared.

# Running the data upload script:
Included in this repository is a bash script named
"upload_data.sh", and within it, is a detailed description
of the command that is to be used to upload CSV files.

Steps to use this script:

1. Ensure that it is executable with this command:
   `chmod +x upload_data.sh`
2. Run it by passing the parameters of servername, username
   .CSV filename
3. Example:
   `./upload_data.sh -s sftp.exampleserver.com -u the-user
   -f /home/the-user/data.csv`
4. If anything is unclear, feel free to get the help info
   by:
   `./upload_data.sh -h` or `./upload_data.sh --help`

-OR-

# Running the python upload script:
Included is a python version for this.  This is a lengthier
tutorial and requires you have `python-virtualenv` installed
on your machine.

1. Install `python-virtualenv` by:
   `sudo apt-get install python-virtualenv`
2. Make a virtualenv:  `virtualenv venv`
3. Activate the virtualenv: `source venv/bin/activate`
4. Install the requirements for this python script:
   `pip install -r requirements.txt`
   The requirements.txt is located in the 'python-upload'
   folder of this project
5. Run the upload_data.py script:
   python upload_data.py <servername> <user> <path to file>
   <path to private key>
6. If I had a server named "sftp.example.com" and my user is
   "superman", with a .CSV located at:
   /home/superman/data.csv and a private key located in:
   /home/superman/.ssh/id_rsa then I would run it as:
   `python upload_data.py sftp.example.com superman
   /home/superman/data.csv/ /home/superman/.ssh/id_rsa`
7.  It is advisable to pass in absolutely paths.

If you experience any unexpected behaviors, please file an
issue with the command you entered to trigger that behavior
and the error output.
