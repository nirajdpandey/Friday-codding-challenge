__Author__ = 'Niraj Dev Pandey'
__Date__ = '29 December 2020'
__Purpose__ = 'Test all the feature and capabilities of the project'
__example__ = 'https://kalnytskyi.com/howto/assert-str-matches-regex-in-pytest/'

# import dependencies
import logging
import re
import yaml
import os
import glob
import unittest
import pathlib as pl

# initialize logging
logging.basicConfig(filename='../logname.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

with open('../config.yml') as configuration:
    config = yaml.safe_load(configuration)

input_file = glob.glob('.' + config['data']['path_to_input_file'] + '*')

logger.info("Configuration file has been loaded successfully")

for i in input_file:
    # Iterate over input files and find file name with it's extension
    filename, file_extension = os.path.splitext(i)
    # If file extension is text kind then fine
    # Print an error message
    if ".txt" not in file_extension:
        print("Your input files are not compatible", filename + file_extension)
    else:
        print(filename + file_extension, ": is compatible to processed. You are good to go")


class TestCase(unittest.TestCase):

    def test_1(self):
        """
        This text will verify if given input file path is a valid path
        and it exists.
        :return: Pass if provided path is a fine and exists
        """

        path_first = pl.Path("../data/another_address.txt")
        self.assertEqual((str(path_first), path_first.is_file()), (str(path_first), True))

    def test_2(self):
        """
        This text will verify if given input file path is a valid path
        and it exists.
        :return: Pass if provided path is a fine and exists
        """

        path_second = pl.Path("../data/simple_address.txt")
        self.assertEqual((str(path_second), path_second.is_file()), (str(path_second), True))

    def test_3(self):
        """
        This text will verify if given string has digits in them
        If they contains only the characters the test will fail.
        One example can be to provide: "abc", "xyz". The pass means that
        the provided string contains digits in them. Like: "Berlin 50"
        :return: Pass if value contains digits else fail
        """

        value = "50"
        assert re.match('\d+', value)

    def test_4(self):
        """
        This text will verify if given string has street kind characters in them
        If they contains only the digits the test will fail.
        One example can be to provide: " 50 ", " 55 ". The pass means that
        the provided string contains characters kind data in them. Like: " Berlin "
        :return: Pass if value contains string characters else fail
        """

        value = " Berlin "
        assert re.match('[A-Za-z]+\s?\w+(?=\s[Nn]o\s\d+$) | [A-Za-z]+\s?\w+\s?[A-Za-z]+\s?[A-Za-z]+', value)


if __name__ == "__main__":
    unittest.main(verbosity=2)
