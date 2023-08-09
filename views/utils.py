import json

"""This module has functions that are used in different modules."""


def load_data(file_name="people.json") -> list:
    """Load the information from the json file and returns a list of data .
            Args:
                    file_name (str): It is the file name.
    """
    with open(file_name, "r") as j:
        data = json.load(j)
    j.close()

    return data


def update_file(new_list, file_name="people.json") -> None:
    """Overwrites the information in the file, in the case that the file
    does not exist, it will be created.

        Args:
            new_list (list): It is the list with the updated information.
            file_name (str): It is the file name.
    """
    with open(file_name, "w") as j:
        json.dump(new_list, j)
    j.close()


def search_index_person(records_list, ci) -> tuple:
    """Searches for a particular element in a list by ci and returns a tuple
        with the index and a dictionary.

            Args:
                records_list (list): It is the list with the updated information.
                ci (int): It is ci.
    """
    for index, record in enumerate(records_list):
        if int(record["CI"]) == ci:
            return index, record

    return -1, {}
