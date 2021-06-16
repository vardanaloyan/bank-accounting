"""
Bank scheme and mapping configurations
"""
import datetime

BANK_SCHEMES = {
    "bank1": {'timestamp', 'type', 'amount', 'from', 'to'},
    "bank2": {'date', 'transaction', 'amounts', 'to', 'from'},
    "bank3": {'date_readable', 'type', 'euro', 'cents', 'to', 'from'}
}

UNIFORM_SCHEME = ('date', 'transaction', 'amount', 'from', 'to')


def combine_euro_cent(dct):
    return "{:.2f}".format(float(dct["euro"]) + float(dct["cents"])/100)


def uniform_date_fmt_bank1(dct):
    date_time_obj = datetime.datetime.strptime(dct["timestamp"], '%b %d %Y')
    return date_time_obj.date().strftime("%d-%m-%Y")


def uniform_date_fmt_bank3(dct):
    date_time_obj = datetime.datetime.strptime(dct["date_readable"], '%d %b %Y')
    return date_time_obj.date().strftime("%d-%m-%Y")


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
