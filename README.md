# gdelt_mining
My own little scripts to consume and analyze the GDELT project's data

##To run scripts
* Go through scripts and change path, host, username, password, etc. values
* There are a few required python packages, please refer to imports for complete list

##GDELT Documentation
* Gdelt 2.0: http://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/
* Get latest gdelt files every 15 minutes at http://data.gdeltproject.org/gdeltv2/lastupdate.txt

##Scripts to consume event data
* gdelt.sql to create table in mysql
* gdelt_miner.sh to pull csv file every 15 minutes (you should set up a cron job)
* gdelt_transfer.py to transfer the filtered events to mysql table (again, cron job)