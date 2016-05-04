#!/usr/bin/env python
"""
Allows a user to upload a .CSV file from their own directory onto
TrustYou's sftp server
"""
import argparse
import paramiko
from socket import gethostbyname, gaierror
import os.path


def parse_args():
    parser = argparse.ArgumentParser(
        "Uploads CSV files to TrustYou's sftp server",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'servername', type=str,
        help="The name of the sftp server, (eg: sftp.trustyou.com)")
    parser.add_argument(
        'username', type=str,
        help="The name of the user, (eg: hotel-california)")
    parser.add_argument(
        'datafile', type=str,
        help="The name of the CSV file, (eg: datafile.csv)")
    parser.add_argument(
        'privatekey', type=str,
        help="The path to the private key file, (eg: ~/.ssh/id_rsa)")
    return parser.parse_args()


def sftp_upload(servername, username, datafile, privatekey):

    # ensures the user has the correct servername:
    try:
        gethostbyname(servername)
    except gaierror:
        print "Error:  Invalid 'servername'"
        exit()

    port = 22

    # get the private key contents from the file pathA
    try:
        my_key = paramiko.RSAKey.from_private_key_file(privatekey)
    except IOError:
        print "Error: Private key not found, check path"
        exit()

    transport = paramiko.Transport((servername, port))
    try:
        transport.connect(username=username, pkey=my_key)
        sftp = paramiko.SFTPClient.from_transport(transport)
    except paramiko.ssh_exception.AuthenticationException:
        print "Authentication failed, please check private key path " \
                "and/or username"
        exit()

    if os.path.isfile(datafile) == True:
        filename = os.path.basename(datafile)
        path = '/home/upload/' + filename
        sftp.put(datafile, path)
    else:
        print "Error:  Input file invalid or not found."
        exit()

    sftp.close()
    transport.close()
    print 'Upload done.'


if __name__ == '__main__':

    args = parse_args()
    sftp_upload(args.servername, args.username, args.datafile, args.privatekey)
