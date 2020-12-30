__Author__ = 'Niraj Dev Pandey'
__Date__ = '23 December 2020'
__Purpose__ = 'Main file which execute every other supporting python scripts'

# import dependencies
import logging
import json
import yaml
import os
from read_text_file import DataReader
from address_filter import FilterString

# initialize logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

with open('config.yml') as configuration:
    config = yaml.safe_load(configuration)

logger.info("Configuration file has been loaded successfully")
read = DataReader(config['data']['path_to_input_file'])
# Load DataReader class and provide path
read = read.reader()
# From DataReader class using reader function which
# Extract all the lines given text files
logger.info("cleaning existing json file for fresh update")
# We don't want duplicate as we are appending to the Json file
# This will delete the existing data and fill the new one's everytime
os.remove(config['data']['path_to_result_file'])

for line in read:
    # Iterate over all files
    for i in line:
        # Iterate over every lines on the files
        input_line = i.replace('"', '').strip()  # removing undesirable character
        print("===" * 15)
        print("Street name and number is: ", input_line)
        # use filter_string to separate street and house number
        result = FilterString(input_line)
        result = result.filter_string()
        # Open a file from config and append the result to it
        with open(config['data']['path_to_result_file'], 'a', encoding='utf8') as outfile:
            json.dump(result, outfile, ensure_ascii=False)
            # using new line for every entry. makes data looks better
            outfile.write('\n')
