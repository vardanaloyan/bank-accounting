"""
In this module we define our Unifiers
Currently implemented:
    1. CSVUnifier class
        which unifies csv files
"""
import csv
import logging
import traceback
import config

logger = logging.getLogger(__name__)


class Unifier:
    """
    Factory class
    Methods defined in this class, should be implemented in each of Unifier classes
    """
    def __new__(cls, input_type, files: list = None):
        input_type = input_type.lower()
        if input_type == "csv":
            return CSVUnifier(files)
        elif input_type == "json":
            return JSONUnifier(files)
        elif input_type == "xml":
            return XMLUnifier(files)
        else:
            raise Exception(f"'{input_type}' type not supported yet")

    def parse_files(self):
        """Skeleton"""
        pass

    def uniform_files(self, parsed_files):
        """Skeleton"""
        pass

    def unify_files(self, unified_files):
        """Skeleton"""
        pass

    def export(self, filename, fmt):
        """Skeleton"""
        pass


class CSVUnifier:
    """
    CSVUnifier class: for unifying csv input files
    """
    def __init__(self, files_paths: list = None) -> None:
        self.files_paths = files_paths
        self.__unified_files = []

    def __repr__(self) -> str:
        return 'CSVUnifier object'

    def parse_files(self) -> list:
        """
        Function loops over the file_path list
        calls 'parse_file' function for parsing the file
        :return: list of tuples, containing rows of csvs and the mapping dict
        """
        files = []
        if self.files_paths:
            for file_path in self.files_paths:
                ret, rows, mapping = self.parse_file(file_path)
                if not ret:
                    logger.error(f"Unable to parse file '{file_path}'")
                    raise Exception(f"Unable to parse file '{file_path}'")
                files.append((rows, mapping))
        else:
            logger.warning("Please import files")
        return files

    def parse_file(self, file_path: str) -> (bool, list, dict):
        """
        Atomic function used in 'parse_files' function,
        used for retrieving the rows of csv file as list of dicts, and guesses the mapping dict

        :param file_path: str
        :return: tuple(bool, list, dict),
            bool -> whether file parsed or not,
            list: content, list of dicts,
            mapping: mapping rule
        """
        try:
            with open(file_path) as f:
                rows = list(csv.DictReader(f))
                if rows:
                    headers = list(rows[0].keys())
                else:
                    headers = []
                mapping = self.match_file_with_bank(headers)
                if not mapping:
                    logger.error(f"Could not find relevant mapping for file '{file_path}'")
                    raise Exception(f"Could not find relevant mapping for file '{file_path}'")
                return True, rows, mapping
        except Exception as ex:
            logger.error(f"Unable to parse file {file_path}")
            logger.error(traceback.format_exc())
            return False, [], {}

    def uniform_files(self, files: list) -> list:
        """
        Executing the mapping, Uniforming files and output new list of uniformed files
        :param files: parsed files-> [content, mapping]
        :return: uniformed files
        """
        uniformed_files = []
        for parsed_file in files:
            uniformed_rows = self.make_uniform_file(parsed_file[0], parsed_file[1])
            uniformed_files.append(uniformed_rows)
        return uniformed_files

    def unify_files(self, uniformed_files: list) -> list:
        """
        Function unifies files
        :param uniformed_files: list of uniformed files
        :return: unified files
        """
        self.__unified_files = []
        for content in uniformed_files:
            self.__unified_files.extend(content)
        return self.__unified_files

    @staticmethod
    def match_file_with_bank(headers: list) -> dict:
        """
        Function loops over the schemes defined in config.BANK_SCHEMES dict
        and searches relevant mapping for the csv file
        :param headers: title list of csv columns
        :return: mapping dict
        """
        for bank, scheme in config.BANK_SCHEMES.items():
            if set(headers) == scheme:
                return config.MAPPING_RULE[bank]

    @staticmethod
    def make_uniform_file(rows: list, mapping: dict) -> list:
        """
        Uniforming the file.
        Function loops over the rows, for each title-key it:
            1. replaces the mapping value if mapping value is string
            2. executes the mapping value giving row as input, if mapping value is function
        :param rows: original rows
        :param mapping: mapping rule dict
        :return: uniformed rows
        """
        uniformed_rows = []
        for row in rows:
            new_row = {}
            for mkey, mval in mapping.items():
                if isinstance(mval, str):
                    new_row[mkey] = row[mval]
                elif callable(mval):
                    new_row[mkey] = mval(row)
            uniformed_rows.append(new_row)
        return uniformed_rows


class JSONUnifier:
    """
    JSONUnifier class: for unifying json input files
    """
    def __init__(self, files_paths: list = None):
        self.files_paths = files_paths
        self.__unified_files = []

    def __repr__(self):
        return "JSONUnifier object"


class XMLUnifier:
    """
    XMLUnifier class: for unifying xml input files
    """
    def __init__(self, files_paths: list = None):
        self.files_paths = files_paths
        self.__unified_files = []

    def __repr__(self):
        return "XMLUnifier object"
