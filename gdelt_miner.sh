#!/bin/bash

#First remove the event files
sudo rm /PATH/TO/latest_gdelt_events.csv
sudo rm /PATH/TO/latest_gdelt_events.csv.zip


#Get url towards latest GDELT update
content_regex="export.CSV.zip"
content=$(curl -v --silent http://data.gdeltproject.org/gdeltv2/lastupdate.txt --stderr - | grep $content_regex)

IFS=' ' read -a content_components <<< "$content"
latest_gdelt_url="${content_components[2]}"


#Get name of compressed file
IFS='/' read -a url_components <<< "$latest_gdelt_url"
compressed_file_name="${url_components[4]}"


#Get name of csv file
IFS='.' read -a file_components <<< "$compressed_file_name"
csv_file_name="${file_components[0]}.${file_components[1]}.${file_components[2]}"


#Download and extract latest events
curl $latest_gdelt_url > /PATH/TO/latest_gdelt_events.csv.zip
unzip -p "/PATH/TO/latest_gdelt_events.csv.zip" $csv_file_name > /PATH/TO/latest_gdelt_events.csv