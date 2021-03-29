# website to Marc21 .mrc file download
This repo imports OG tags website data and then writes that data to a valid Marc21 RDA .mrc to local disk file

## Dependencies
* Python Requests library
* BeautifulSoup 4 library
* Pymarc library
* Python Date library
* Python regex library

## Setup
* pip install pymarc
* pip install beautifulsoup4
* pip install requests

## How to use this
1. Open website_to_marc21.py
2. copy the website home address into the 'url' variable on line 9
3. Run script in terminal, via visual studio code debug, or however you like to run your code.
4. If the website has OG (Open graph) tags available, the .mrc file will be createdm named as website address, if no OG tags are available the script will prompt an error, so will not create a .mrc file.

## Marc fields included:
I will add the specific list here here, but all records created comply with MArc21 + RDA standards for website records.

## Future enhancements
* Website array based .mrc file creation
* Python flask server web GUI with address pasting input form
* clipboard web address paste

Enjoy 🐱✌️
