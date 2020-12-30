__Author__ = 'Niraj Dev Pandey'
__Date__ = '23 December 2020'
__Purpose__ = 'Codding challenge for Senior Software Engineer (Data Focus)'

# import dependencies
import logging
import json
import re
import os

# initialize logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def input_string(string):
    """
    Given the input string, tries to separate them into "street" & "house number" variables

    1. simple case:

    "Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}
    "Musterstrasse 45" -> {"street": "Musterstrasse", "housenumber": "45"}
    "Blaufeldweg 123B" -> {"street": "Blaufeldweg", "housenumber": "123B"}

    2. Complex case:

    "4, rue de la revolution" -> {"street": "rue de la revolution", "housenumber": "4"}
    "200 Broadway Av" -> {"street": "Broadway Av", "housenumber": "200"}
    "Calle Aduana, 29" -> {"street": "Calle Aduana", "housenumber": "29"}
    "Calle 39 No 1540" -> {"street": "Calle 39", "housenumber": "No 1540"}

    :param string: String of address
    :return: Separated address strings into street name and house number

    Sample output:

    [{"street": "Auf der Vogelwiese", "housenumber": "23 b"}]
    [{"street": "rue de la revolution", "housenumber": "4"}]
    [{"street": "Broadway Av", "housenumber": "200"}]
    [{"street": "Calle Aduana", "housenumber": "29"}]
    [{"street": "Calle 39", "housenumber": "No 1540"}]
    [{"street": "Winterallee", "housenumber": "3"}]

    """
    logger.info("Information Extracted...")

    pattern_street = re.compile(r'[A-Za-z]+\s?\w+(?=\s[Nn]o\s\d+$) | [A-Za-z]+\s?\w+\s?[A-Za-z]+\s?[A-Za-z]+',
                                re.X)   # street pattern
    match_street = pattern_street.search(string)

    """ If there are no house numbers provided in the input file, print(NO HOUSE NUMBER!) in the output JSON file """
    numbers_instring = re.findall(r'\d+', string)  # finding how many numbers in the total string

    if len(numbers_instring) > 0:
        pattern_housenumber = re.compile(r'(\d+\s?[A-Za-z]?$) | (^\d+) | [Nn]o+[\s?]+[0-9]+$',
                                         re.X)  # house number pattern
        match_housenumber = pattern_housenumber.search(string)
        fin_housenumber = match_housenumber[0]
    else:
        match_housenumber = ["NO HOUSE NUMBER!"]

    fin_housenumber = match_housenumber[0]
    fin_street = match_street[0]

    print("street: ", fin_street)
    print("housenumber: ", fin_housenumber)

    result = {'street': fin_street, 'housenumber': fin_housenumber}
    if not os.path.exists('result'):
        os.makedirs('result')
    with open(os.path.join('result', json_filename), 'a', encoding='utf8') as outfile:
        json.dump(result, outfile, ensure_ascii=False)
        # outfile.write('\n')


input_filename = input("Enter the path of your file: ")

if os.path.exists(input_filename):
    print("your file has been loaded", input_filename)
else:
    print("I did not find the file at, " + str(input_filename))

input_filename_noformat = re.search(r'(.txt|.dat)', input_filename)  # input filename without the .txt,.dat
json_filename = input_filename[
                0:input_filename_noformat.span()[0]] + '.json'  # creating .json file with same name as input file

file1 = open(input_filename, 'r')
lines = file1.readlines()
for line in lines:
    input_line = line.replace('"', '').strip()  # replacing the " with '
    print("Street name and number is: ", input_line)
    input_string(input_line)
