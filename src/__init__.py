import argparse
import json
import os
from filter import FilteringData
__ENCODING = 'utf-8'

__OLD_PROVINCES_FILE = "data/vietnamlands_old.json"
__NEW_PROVINCES_FILE = "data/vietnamlands_new.json"


def __load_json(file_path):
    """
    Load a JSON file and return its contents as a dictionary.
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r', encoding=__ENCODING) as file:
        data = json.load(file)

    return data

def list_old_provinces(name='', licensePlates=[], subdivision_level=0, order_by=None):
    """
    List all old provinces from the JSON file.
    :return: List of old provinces.
    """
    file_path = os.path.join(os.path.dirname(__file__), __OLD_PROVINCES_FILE)
    data = __load_json(file_path)
    data_filter = FilteringData(data)

    retruned_data = data_filter.filtering_data(name, licensePlates, subdivision_level)
    if (order_by):
        retruned_data = data_filter.ordering_data(order_by)
    return retruned_data


def list_new_provinces(name='', licensePlates=[], subdivision_level=0):
    """
    List all new provinces from the JSON file.
    :return: List of new provinces.
    """
    file_path = os.path.join(os.path.dirname(__file__), __NEW_PROVINCES_FILE)
    data = __load_json(file_path)
    return data



parser = argparse.ArgumentParser(description="Filter provinces data")

parser.add_argument(
    "--name",
    type=str,
    default="",
    help="Name of the province to filter by (case insensitive)",
)
parser.add_argument(
    "--licensePlates",
    type=int,
    nargs="*",
    default=[],
    help="List of license plates to filter by",
)

def check_subdivision_level(value):
    ivalue = int(value)
    if ivalue < 0 or ivalue > 2:
        raise argparse.ArgumentTypeError("subdivision_level must be between 0 and 2")
    return ivalue
parser.add_argument(
    "--subdivision_level",
    type=check_subdivision_level,
    default=0,
    choices=[0, 1, 2],
    help="Subdivision level to filter by (0, 1, or 2)",
)
