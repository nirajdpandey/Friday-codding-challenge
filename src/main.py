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
logging.basicConfig(filename='../logname.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


with open('../config.yml') as configuration:
    config = yaml.safe_load(configuration)

logger.info("Configuration file has been loaded successfully")
output_path = config['data']['path_to_result_file']
input_path = config['data']['path_to_input_file']

read = DataReader(input_path)
read = read.reader()  # Load DataReader class and provide path
# From DataReader class using reader function which
# Extract all the lines given text files
logger.info("cleaning existing json file for fresh update")

if not os.path.exists(output_path):
    with open(output_path, "w"):  # create file if not exists already
        pass
os.remove(output_path)
# We don't want duplicate as we are appending to the Json file
# This will delete the existing data and fill the new one's everytime

for line in read:  # Iterate over all files
    for i in line:  # Iterate over every lines on the files
        input_line = i.replace('"', '').strip()  # removing undesirable character
        print("===" * 15)
        print("Street name and number is: ", input_line)
        # use filter_string to separate street and house number
        result = FilterString(input_line)
        result = result.filter_string()
        # Open a file from config and append the result to it
        with open(output_path, 'a', encoding='utf8') as outfile:
            json.dump(result, outfile, ensure_ascii=False)
            # using new line for every entry. makes data looks better
            outfile.writelines('\n')
