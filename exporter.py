"""
In this module we define our Exporters
Currently implemented:
    1. CSVExporter class
        which outputs unified files as csv file
    2. JSONExporter class
        which outputs unified files as json file
"""
import csv
import json
import logging
import traceback

logger = logging.getLogger(__name__)


class CSVExporter:
    """
    CSVExporter class: for exporting output as csv
    """
    def __init__(self, *args, **kwargs):
        """
        Accepts filename parameter for output file.
        In the future you can extend attributes of the class to implement new features
        :param args: not used
        :param kwargs: filename and newline parameters can be used
        """
        self.filename = kwargs.get("filename", "out.csv")
        self.newline = kwargs.get("newline", '')

    def export(self, unified_file: list = None) -> bool:
        """
        Function exports unified files in csv file
        :param unified_file: list of unified files
        :return: True if exported successfully, otherwise raises and exception
        """
        if not unified_file:
            raise Exception("Trying to write empty content")
        try:
            header = unified_file[0].keys()
            with open(self.filename, 'w', newline=self.newline) as output_file:
                dict_writer = csv.DictWriter(output_file, header)
                dict_writer.writeheader()
                dict_writer.writerows(unified_file)
            return True
        except Exception as ex:
            logger.error(f"Error occurred while exporting file '{self.filename}'")
            logger.error(traceback.format_exc())
            raise


class JSONExporter:
    """
    JSONExporter class: for exporting output as json
    """
    def __init__(self, *args, **kwargs):
        """
        Accepts filename parameter for output file.
        In the future you can extend attributes of the class to implement new features
        :param args: not used
        :param kwargs: filename parameter can be used
        """
        self.filename = kwargs.get("filename", "out.json")

    def export(self, unified_file: list = None):
        """
        Function exports unified files in json file
        :param unified_file: list of unified files
        :return: True if exported successfully, otherwise raises and exception
        """
        if not unified_file:
            raise Exception("Trying to write empty content")
        try:
            with open(self.filename, "w") as output_file:
                json.dump(unified_file, output_file, indent=4)

            return True
        except Exception as ex:
            logger.error(f"Error occurred while exporting file '{self.filename}'")
            logger.error(traceback.format_exc())
            raise
