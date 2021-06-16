"""
Unifier module for bank accounting
"""
import csv
import glob
import logging

logger = logging.getLogger(__name__)

class Unifier:
    """
    Unifier class
    """
    def __init__(self):
        self.__imported_files = None

    def __repr__(self):
        return 'Unifier object'

    def import_files(self, glob_pattern: str) -> bool:
        self.__imported_files = glob.glob(glob_pattern)

    def parse_imported_files(self):
        if self.__imported_files:
            for file_path in self.__imported_files:
                resp = self.parse_input_file(file_path)
                if not resp:
                    logger.error(f"Unable to parse file '{file_path}'")
                    raise Exception(f"Unable to parse file '{file_path}'")
        else:
            logger.warning("Please import files")

    def parse_input_file(self, file_path: str) -> bool:
        if file_path.endswith(".csv"):
            return self.parse_csv_file(file_path)

    def parse_csv_file(self, file_path):
        with open(file_path) as f:
            reader = list(csv.DictReader(f))
            if reader:
                headers = list(reader[0].keys())
            else:
                headers = []
            print(headers)
        return True

    def match_file_with_bank(self):
        pass

    def match_csv_with_bank(self):
        pass

    def make_uniform(self):
        pass

    def accumulate(self):
        pass

    def export(self):
        pass

    def flow(self):
        self.import_files("*.csv")
        self.parse_imported_files()


if __name__ == "__main__":
    a = Unifier()
    a.flow()
