__Author__ = 'Niraj Dev Pandey'
__Date__ = '23 December 2020'
__Purpose__ = 'This file will read text data and extract lines out of it'

# import dependencies
import yaml
import logging
import glob

# initialize logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class DataReader:
    def __init__(self, input_path):
        """
        Function read_text_file will accept one argument as text file path
        :param input_path: directory path to the text file
        :return: list of Lines of the provided text file
        """

        self.input_path = input_path
        self.content = []

    def reader(self):
        """
        reader function will use the path provided in init function
        and extract the data out of those files. You don't need to
        provide specific file path. Just the folder path will work.
        The glob package will automatically find all the text files from
        that provided folder path.
        :return: list of Lines of the provided text file
        """

        logger.info("loading text file to read")
        # Loading all the text file given folder
        files = glob.glob(self.input_path + '*txt')
        print("Loaded file count is : ", len(files))
        for i in files:
            print("Loaded files are: ", i)
            # the [:] index is helpful in case you have just one input text file
            # this helps the loop not to throw any error
            with open(i[:], 'r', encoding='utf8') as file:
                self.content.append(file.readlines())
            logger.info("Loaded text file successfully!")
            logger.info("process finished!")
            # Return all the extracted content in a python list
        return self.content
