"""
Unifier Application (UApp) for bank accounting
"""
import glob
import logging
from exporter import CSVExporter, JSONExporter
from unifier import Unifier

logger = logging.getLogger(__name__)


class UApp:
    """
    Unifier Application class
    """
    def __init__(self):
        self.__imported_files = None
        self.__uniformed_files = []
        self.input_type = None
        self.unifier_object = None

    def __repr__(self):
        return 'Unifier object'

    def import_files(self, glob_pattern: str) -> bool:
        """
        Function for importing files for unifying using glob pattern format
        Inside the function we guess the input file type, by analyzing glob pattern
        using str.endswith function.
        :param glob_pattern: str
        :return: bool

        .. todo:: Implement better algorithm for guessing the file type

        """
        self.__imported_files = glob.glob(glob_pattern)
        if glob_pattern.lower().endswith(".csv"):
            self.input_type = "csv"
        else:
            self.input_type = None
        if len(self.__imported_files) == 0 or self.input_type is None:  # in case of not implemented or Absence of files
            logger.warning("Please import (allowed) files")
            return False
        return True

    def create_unifier(self, input_type: str) -> Unifier:
        """
        Function is part of Factory method design pattern implementation.
        It accepts input_type parameter and creates relevant class
        :param input_type: "csv"
        :return: Unifier object
        """
        return Unifier(input_type, self.__imported_files)

    def flow(self):
        """
        Flow implementation
        :return: None
        """
        ret = self.import_files("input/bank*.csv")
        if ret:
            unifier = self.create_unifier(self.input_type)
            parsed_files = unifier.parse_files()
            uniformed_files = unifier.uniform_files(parsed_files)
            unified_files = unifier.unify_files(uniformed_files)
            out_writer = CSVExporter(filename="output/output.csv")
            # out_writer = JSONExporter(filename="output/output.json")
            out_writer.export(unified_files)


if __name__ == "__main__":
    a = UApp()
    a.flow()
