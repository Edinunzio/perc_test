"""
Percolate Coding Challenge!
Normalize entries from data/sample-Liz.in to JSON on data/result.out
$ cd perc_test/app
$ python formatter.py
"""
import time
import json
from functools import wraps


def timefn(fn):
    """
    profiling/logging helper measuring execution speed
    :param self: function
    :return: str: print statement
    """

    @wraps(fn)
    def measure_time(*args, **kwargs):
        """
        prints time elapsed per wrapped function in console
        """
        beg = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print "@timefn:" + fn.func_name + " took " + str(end - beg) + " seconds"
        return result

    return measure_time


class Formatter(object):
    """
    formatter
    :returns result.out
    """

    def __init__(self):
        self.entries = []
        self.errors = []
        self.line_count = None
        self.entry_count = None


    @staticmethod
    def read_file(filename):
        """
        reads file
        f = _fm.read_file(filename)
        :param filename: str
        :return: txt: str
        """
        with open(filename, 'r') as opened_file:
            txt = opened_file.read()
        opened_file.close()
        return txt

    @timefn
    def get_entries_by_line(self, file_contents):
        """
        grabs content of each line and appends to list
        container = _fm.get_entries_by_line(file_contents)
        :param file_contents: str
        :return: container: list
        """
        _entries = file_contents.split("\n")
        container = []
        for _entry in _entries:
            item = _entry.split(",")
            container.append(item)
        # stores line_count for test_line_count_equals_entry_count
        self.line_count = len(container)
        return container

    @timefn
    def validate_entries(self, container):
        """
        validates each entry
        valid formats:
            1. lastname, firstname, (###)-###-####, color, #####
            2. firstname lastname, color, #####, ### ### ####
            3. firstname, lastname, #####, ### ### ####, color
        invalid entries are appended to self.errors
        output = _fm.validate_entries(container)
        :param container: list
        """
        for entry in container:
            entry_index = container.index(entry)
            _entry = {}
            if len(entry) == 4:
                name = entry[0].split(" ")
                _entry["first_name"] = self.validate_str(name[0], entry_index)
                _entry["last_name"] = self.validate_str(name[1], entry_index)
                _entry["color"] = self.validate_str(entry[1], entry_index)
                _entry["zipcode"] = self.validate_zipcode(entry[2], entry_index)
                _entry["phonenumber"] = self.validate_phonenumber(entry[3], entry_index)
                self.validate_entry(_entry)
            elif len(entry) == 5:
                if "(" in entry[2]:
                    _entry["first_name"] = self.validate_str(entry[1], entry_index)
                    _entry["last_name"] = self.validate_str(entry[0], entry_index)
                    _entry["color"] = self.validate_str(entry[3], entry_index)
                    _entry["zipcode"] = self.validate_zipcode(entry[4], entry_index)
                    _entry["phonenumber"] = self.validate_phonenumber(entry[2], entry_index)
                    self.validate_entry(_entry)
                else:
                    _entry["first_name"] = self.validate_str(entry[0], entry_index)
                    _entry["last_name"] = self.validate_str(entry[1], entry_index)
                    _entry["color"] = self.validate_str(entry[4], entry_index)
                    _entry["zipcode"] = self.validate_zipcode(entry[2], entry_index)
                    _entry["phonenumber"] = self.validate_phonenumber(entry[3], entry_index)
                    self.validate_entry(_entry)
            else:
                self.errors.append(container.index(entry))

    def validate_entry(self, _entry):
        """
        checks if any attributes == None
        :param _entry: dict
        """
        if None not in _entry.itervalues():
            self.entries.append(_entry)

    def validate_phonenumber(self, phone, ind):
        """
        normalizes phone output
        invalid phone are letters or lengths not equal to 10
        phonenumber = self.validate_phonenumber(phone, ind)
        :param phone: str
        :param ind: int
        :return: phone: str or None
        """
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        phone = phone.replace("-", "")
        phone = phone.replace(" ", "")
        try:
            phone = str(int(phone))
            if len(phone) == 10:
                return str(phone[0:3]) + "-" + str(phone[3:6]) + "-" + str(phone[6:])
            else:
                self.errors.append(ind)
                return None
        except ValueError:
            self.errors.append(ind)

    def validate_zipcode(self, zipcode, ind):
        """
        normalizes zipcode output
        invalid zipcode are letters or lengths not equal to 5
        zipcode = self.validate_zipcode(zipcode, ind)
        :param zipcode: str
        :param ind: int
        :return: zipcode: str or None
        """
        zipcode = zipcode.replace(" ", "")
        try:
            zipcode = str(int(zipcode))
            if len(zipcode) == 5:
                return str(zipcode)
            else:
                self.errors.append(ind)
                return None
        except ValueError:
            self.errors.append(ind)

    def validate_str(self, label, ind):
        """
        normalizes string output
        tests if string could be an integer
        invalid if type is not string
        string = self.validate_str(name[0], container.index(entry))
        :param label: string
        :param ind: int
        :return: label: str or None
        """
        try:
            label = int(label)
            self.errors.append(ind)
            return None
        except ValueError:
            if type(label) == str:
                return label.strip()
            else:
                self.errors.append(ind)
                return None

    def format_output(self):
        """
        formats output to json
        :return: results: str
        """
        # remove duplicate errors
        self.errors = list(set(self.errors))
        # stores entry_count for test_line_count_equals_entry_count
        self.entry_count = len(self.entries) + len(self.errors)
        # sorting entries alphabetically ascending by last name
        sorted_entries = sorted(self.entries, key=lambda k: k["last_name"], reverse=False)
        self.entries = sorted_entries
        output = {"entries": self.entries, "errors": self.errors}
        # formatting to json per requirements
        results = json.dumps(output, sort_keys=True, indent=2)
        return results

    @staticmethod
    def output_results(op_filename, _json):
        """
        writes and saves _json to op_filename
        :param op_filename: str
        :param _json: str
        :return: result.out: json obj
        """
        with open(op_filename, 'w') as opened_file:
            opened_file.write(_json)
        opened_file.close()


def process_file(in_put, out_put):
    """
    reads input
    analyzes input
    saves output in json
    process_file("../data/sample-Liz.in", "../data/result.out")
    :param in_put: str
    :param out_put: str
    :return: result.out
    """
    _formatter = Formatter()
    read_input = _formatter.read_file(in_put)
    entries = _formatter.get_entries_by_line(read_input)
    _formatter.validate_entries(entries)
    results = _formatter.format_output()
    _formatter.output_results(out_put, results)


if __name__ == '__main__':
    process_file("../data/sample-Liz.in", "../data/result.out")
