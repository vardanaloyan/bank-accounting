"""
Unifier module for bank accounting
"""
import csv
import glob
import logging

import config

logger = logging.getLogger(__name__)

class Unifier:
    """
    Unifier class
    """
    def __init__(self):
        self.__imported_files = None
        self.__uniformed_files = []

    def __repr__(self):
        return 'Unifier object'

    def import_files(self, glob_pattern: str) -> bool:
        self.__imported_files = glob.glob(glob_pattern)

    def parse_imported_files(self):
        files = []
        if self.__imported_files:
            for file_path in self.__imported_files:
                resp = self.parse_input_file(file_path)
                if not resp[0]:
                    logger.error(f"Unable to parse file '{file_path}'")
                    raise Exception(f"Unable to parse file '{file_path}'")
                files.append((resp[1], resp[2]))
        else:
            logger.warning("Please import files")
        return files

    def uniform_files(self, files):
        for parsed_file in files:
            uniformed_rows = self.make_uniform_csv(parsed_file[0], parsed_file[1])
            self.accumulate(uniformed_rows)

    def parse_input_file(self, file_path: str) -> tuple:
        if file_path.endswith(".csv"):
            return self.parse_csv_file(file_path)
        else:
            raise Exception("Waiting for csv extension files")

    def parse_csv_file(self, file_path):
        with open(file_path) as f:
            reader = list(csv.DictReader(f))
            if reader:
                headers = list(reader[0].keys())
            else:
                headers = []
            mapping = self.match_csv_with_bank(headers)
            return True, reader, mapping

    @staticmethod
    def match_csv_with_bank(headers: list) -> dict:
        for bank, scheme in config.BANK_SCHEMES.items():
            if set(headers) == scheme:
                return config.MAPPING_RULE[bank]

    @staticmethod
    def make_uniform_csv(rows: list, mapping: dict) -> list:
        uniformed_rows = []
        for row in rows:
            new_row = {}
            for mkey, mval in mapping.items():
                if isinstance(mval, str):
                    new_row[mkey] = row[mval]
                else:
                    new_row[mkey] = mval(row)
            uniformed_rows.append(new_row)
        return uniformed_rows

    def accumulate(self, uniformed_file):
        self.__uniformed_files.extend(uniformed_file)

    def export(self, filename, fmt):
        if fmt == "csv":
            header = self.__uniformed_files[0].keys()
            with open(filename, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, header)
                dict_writer.writeheader()
                dict_writer.writerows(self.__uniformed_files)

    def flow(self):
        self.import_files("input/bank*.csv")
        files = self.parse_imported_files()
        self.uniform_files(files)
        self.export("output/out.csv", "csv")


if __name__ == "__main__":
    a = Unifier()
    a.flow()
