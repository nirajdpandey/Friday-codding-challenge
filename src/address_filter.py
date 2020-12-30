__Author__ = 'Niraj Dev Pandey'
__Date__ = '23 December 2020'
__Purpose__ = 'This file is main brain of the project which extract the addresses from given string'

# import dependencies
import logging
import re
# initialize logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class FilterString:

    def __init__(self, string):
        """
        Provide string of addresses and this class will extract
        "street" & "house number".
        :param string: address string
        """
        self.string = string

    def filter_string(self):
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

        Sample output:
        [{"street": "Auf der Vogelwiese", "housenumber": "23 b"}]
        [{"street": "rue de la revolution", "housenumber": "4"}]
        [{"street": "Broadway Av", "housenumber": "200"}]
        [{"street": "Calle Aduana", "housenumber": "29"}]
        [{"street": "Calle 39", "housenumber": "No 1540"}]
        [{"street": "Winterallee", "housenumber": "3"}]

        :return: Separated address strings into street name and house number
        """
        logger.info("Information Gathering Finished!")

        pattern_street = re.compile(r'[A-Za-z]+\s?\w+(?=\s[Nn]o\s\d+$) | [A-Za-z]+\s?\w+\s?[A-Za-z]+\s?[A-Za-z]+',
                                    re.X)  # street pattern
        match_street = pattern_street.search(self.string)

        # If there are no house numbers provided in the input file,
        # print(NO HOUSE NUMBER!) in the output JSON file
        numbers_instring = re.findall(r'\d+', self.string)  # digit counts in given string

        if len(numbers_instring) > 0:
            # In most cases we have: "no" followed by some digits
            pattern_housenumber = re.compile(r'(\d+\s?[A-Za-z]?$) | (^\d+) | [Nn]o+[\s?]+[0-9]+$',
                                             re.X)  # house number pattern
            match_housenumber = pattern_housenumber.search(self.string)
            fin_housenumber = match_housenumber[0]
        else:
            match_housenumber = ["NO HOUSE NUMBER!"]

        fin_housenumber = match_housenumber[0]
        fin_street = match_street[0]
        print("street: ", fin_street)
        print("housenumber: ", fin_housenumber)
        return {'street': fin_street, 'housenumber': fin_housenumber}
