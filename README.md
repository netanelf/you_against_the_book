# you_against_the_book

# installation
- apt-get install python3-django
- update run_server.sh to the source location/ port
- if you already have a running server, copy db.sqlite3 to "source location/yatb_django"
- startup can be done with crontab (https://stackoverflow.com/questions/12973777/how-to-run-a-shell-script-at-startup):
- - $ crontab -e
- - @reboot  /home/user/startup.sh
