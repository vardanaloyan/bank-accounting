"""
Bank scheme and mapping configuration
"""
import datetime

# For unknown matching file's content with known bank
BANK_SCHEMES = {
    "bank1": {'timestamp', 'type', 'amount', 'from', 'to'},
    "bank2": {'date', 'transaction', 'amounts', 'to', 'from'},
    "bank3": {'date_readable', 'type', 'euro', 'cents', 'to', 'from'}
}

# Final Scheme
UNIFORM_SCHEME = ('date', 'transaction', 'amount', 'from', 'to')
UNIFORM_DATE_FMT = "%d-%m-%Y"


def combine_euro_cent(dct: dict) -> str:
    """
    Function combines cents with euro by the following formula amount = euro + cents/100
    :param dct: row of csv file
    :return: str
    """
    return "{:.2f}".format(float(dct["euro"]) + float(dct["cents"])/100)


def uniform_date_fmt_bank1(dct: dict) -> str:
    """
    Unified date
    :param dct: row of csv file
    :return: str
    """
    date_time_obj = datetime.datetime.strptime(dct["timestamp"], '%b %d %Y')
    return date_time_obj.date().strftime(UNIFORM_DATE_FMT)


def uniform_date_fmt_bank3(dct: dict) -> str:
    """
    Unified date
    :param dct: row of csv file
    :return: str
    """
    date_time_obj = datetime.datetime.strptime(dct["date_readable"], '%d %b %Y')
    return date_time_obj.date().strftime(UNIFORM_DATE_FMT)


# Used in <unifier.CSVUnifier.match_file_with_bank> function for matching the file with the corresponding bank
MAPPING_RULE = {
    "bank1": {
        UNIFORM_SCHEME[0]: uniform_date_fmt_bank1,
        UNIFORM_SCHEME[1]: "type",
        UNIFORM_SCHEME[2]: "amount",
        UNIFORM_SCHEME[3]: "from",
        UNIFORM_SCHEME[4]: "to"
    },
    "bank2": {
        UNIFORM_SCHEME[0]: "date",
        UNIFORM_SCHEME[1]: "transaction",
        UNIFORM_SCHEME[2]: "amounts",
        UNIFORM_SCHEME[3]: "from",
        UNIFORM_SCHEME[4]: "to"
    },
    "bank3": {
        UNIFORM_SCHEME[0]: uniform_date_fmt_bank3,
        UNIFORM_SCHEME[1]: "type",
        UNIFORM_SCHEME[2]: combine_euro_cent,
        UNIFORM_SCHEME[3]: "from",
        UNIFORM_SCHEME[4]: "to"
    }
}
