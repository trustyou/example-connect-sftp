#!/bin/bash

usage()
{
cat << EOF
usage: $0 options

Uploads the specified CSV file to TrustYou's sftp server

OPTIONS
  -h Show this message and exit
  -s Specify sftp server
  -u Specify sftp user
  -f Specifies the .CSV filename
EOF
}

while getopts "hs:u:f:" OPTION
do
        case $OPTION in
                h)
                        usage
                        exit
                        ;;
                s)
                        server=$OPTARG
                        ;;
                u)
                        user=$OPTARG
                        ;;
                f)
                        file=$OPTARG
                        ;;
        esac
done

exit_hook()
{
        if [[ "$1" -ne 0 ]]
        then
                echo "Failed with code $1"
                exit $1
        fi
}

sftp "$user"@"$server":/home/upload <<< $'put'" $file"

# Command to upload data onto TrustYou's server:

# Explanation of this command:

#sftp <username>@<server name>:/home/upload <<< $'put ./sample_data.csv'
#1   [-- #2 --] [--- #3 ---]  [--- #4 ---]  #5   #6   [----- #7 -----]


# 1)  The program we are telling our command line to use
#
# 2)  The username/account that has been supplied to you
#
# 3)  This is our sftp server's domain name.  It is an URL
#     that tells the 'sftp' program which server to upload
#
# 4)  This is our sftp server's directory.  Within our
#     server we have many folders, we would like you to
#     upload things into our /home/upload folder.
#
# 5)  This is a "Here string".  It passes the words on the
#     right side the <<< into the standard input of the
#     command, in our case, sftp.
#
# 6)  This tells the sftp what to do.  In our case, we
#     wish to 'put' a file from YOUR local machine, up
#     onto our (TrustYou's) servers.
#
# 7)  The path of the file to be uploaded.
#

# In summary, what this command does in plain english, is:
# "Use sftp, as <username> and upload sample_data.csv from
# the current directory to the /home/upload/ folder of
# a server called sftp.trustyou.com"

exit_hook $?

