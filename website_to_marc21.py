
import requests
from bs4 import BeautifulSoup
from pymarc import Record, Field
import re
import datetime

# target website
url = 'https://museumsvictoria.com.au/melbournemuseum/at-home/'

# get website data with requests    
r = requests.get(url)
r.status_code
r.headers['content-type']
r.encoding
r.text
# load website data into BS4
soup = BeautifulSoup(r.text, 'html.parser')

# main scritpion function, uses website data to build marc21 records using pymarc
def main():
    
    title = soup.find("meta",  property="og:title")
    url = soup.find("meta",  property="og:url")
    description = soup.find("meta",  property="og:description")
    
    title_data = (title["content"] if title else "No meta title given")
    url_data = (url["content"] if url else "No meta url given")
    description_data = (description["content"] if description else "No description given")
    
    # date and time generated for marc21 field
    date = datetime.datetime.now()
    date_viewed = date.strftime("%m/%d/%Y, %H:%M:%S")
    
    # printing output of website data that will be used in marc21 record
    print(title_data)
    print(url_data)
    print(description_data)
    print(date_viewed)

    # create_marc21_from_website_data
    # Creating records based on supplied data
    record = Record()

    # FIELD TEMPLATE, INCASE YOU NEED TO ADD A NEW FIELD
    # # Adding ??? - ???
    # record.add_field(
    #     Field(
    #         tag = '???',
    #         indicators = ['#','#'],
    #         subfields = [
    #             'a', '...',
    #             'b', '...',
    #             'c', '...'
    #         ]))

    # Adding 040 - Cataloguing source - description conventions
    record.add_field(
        Field(
            tag = '040',
            indicators = ['#','#'],
            subfields = [
                'e', 'RDA',
            ]))

    # Adding 245 - Title statement
    record.add_field(
        Field(
            tag = '245',
            indicators = ['0','1'],
            subfields = [
                'a', title_data,
            ]))

    # Adding 300 - Physical description 
    record.add_field(
        Field(
            tag = '300',
            indicators = ['#','#'],
            subfields = [
                'a', 'Online resource',
                'b', 'Mixed media',
            ]))

    # Adding 336 - Content type 
    record.add_field(
        Field(
            tag = '336',
            indicators = ['#','#'],
            subfields = [
                'a', 'text',
                'b', 'txt',
                '2', 'rdacontent'
            ]))

    # Adding 337 - Media type
    record.add_field(
        Field(
            tag = '337',
            indicators = ['#','#'],
            subfields = [
                'a', 'Computer',
                'b', 'c',
                '2', 'rdamedia'
            ]))

    # Adding 338 - Carrier type
    record.add_field(
        Field(
            tag = '338',
            indicators = ['#','#'],
            subfields = [
                'a', 'Online resource',
                'b', 'cr',
                '2', 'rdacarrier'
            ]))

    # Adding 500 - General note
    record.add_field(
        Field(
            tag = '500',
            indicators = ['#','#'],
            subfields = [
                'a', 'Title from Homepage',
            ]))

    # Adding 520 - Summary
    record.add_field(
        Field(
            tag = '520',
            indicators = ['#','#'],
            subfields = [
                'a', description_data,
            ]))

    # Adding 546 - Language notes
    record.add_field(
        Field(
            tag = '546',
            indicators = ['#','#'],
            subfields = [
                'a', 'In English',
            ]))

    # Adding 588 - Source of description note
    record.add_field(
        Field(
            tag = '588',
            indicators = ['#','#'],
            subfields = [
                'a', date_viewed,
            ]))

    # # Adding 650 - Subject Added Entry-Topical Term
    # record.add_field(
    #     Field(
    #         tag = '650',
    #         indicators = ['#','4'],
    #         subfields = [
    #             'a', 'Subject here',
    #         ]))

    # # Adding 650 - Subject Added Entry-Topical Term
    # record.add_field(
    #     Field(
    #         tag = '650',
    #         indicators = ['#','4'],
    #         subfields = [
    #             'a', 'Subject here',
    #         ]))

    # # Adding 650 - Subject Added Entry-Topical Term
    # record.add_field(
    #     Field(
    #         tag = '650',
    #         indicators = ['#','4'],
    #         subfields = [
    #             'a', 'Subject here',
    #         ]))


    # Adding 710 - Added entry - Corporate name
    record.add_field(
        Field(
            tag = '710',
            indicators = ['2','#'],
            subfields = [
                'a', title_data,
            ]))

    # Adding 856 - Electronic location and access
    record.add_field(
        Field(
            tag = '856',
            indicators = ['#','#'],
            subfields = [
                'U', url_data,
            ]))
    
    # file name based on website og title URL with web characters removed
    file_name = re.sub(r'\W+', ' ', url_data)

    # Writing marc21 file to disc
    with open(file_name + '.mrc', 'wb') as out:
        out.write(record.as_marc())

# OG data check for each URL scraped
x =  title = soup.find("meta",  property="og:title")

if x :
    print("OG tags found, record will be created")
    main()
else:
    print("No OG tags found, sorry we are unable to create a record")
