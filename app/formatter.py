"""
Percolate Coding Challenge!
"""
import json


class Formatter():
    """
    formatter
    :returns result.out
    """

    def __init__(self):
        self.entries = []
        self.errors = []
        self.line_count = None
        self.entry_count = None


    def read_file(self, filename):
        """
        reads file
        f = _fm.read_file(filename)
        :param filename: str
        :return: txt: str
        """
        with open(filename, 'r') as f:
            txt = f.read()
        f.close()
        return txt

    def get_entries_by_line(self, file_contents):
        """
        grabs content of each line and appends to list
        stores line_count for test_line_count_equals_entry_count
        container = _fm.get_entries_by_line(file_contents)
        :param file_contents: str
        :return: container: list
        """
        _entries = file_contents.split("\n")
        container = []
        for e in _entries:
            item = e.split(",")
            container.append(item)
        self.line_count = len(container)
        return container

    def analyze_entry(self, container):
        """
        validates each entry
        valid formats:
            1. lastname, firstname, (###)-###-####, color, #####
            2. firstname lastname, color, #####, ### ### ####
            3. firstname, lastname, #####, ### ### ####, color
        invalid entries are appended to self.errors
        output = _fm.analyze_entry(container)
        :param container: list
        :return: results: dict
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
                if None not in _entry.itervalues():
                    self.entries.append(_entry)
            elif len(entry) == 5:
                if "(" in entry[2]:
                    _entry["first_name"] = self.validate_str(entry[1], entry_index)
                    _entry["last_name"] = self.validate_str(entry[0], entry_index)
                    _entry["color"] = self.validate_str(entry[3], entry_index)
                    _entry["zipcode"] = self.validate_zipcode(entry[4], entry_index)
                    _entry["phonenumber"] = self.validate_phonenumber(entry[2], entry_index)
                    if None not in _entry.itervalues():
                        self.entries.append(_entry)
                else:
                    _entry["first_name"] = self.validate_str(entry[0], entry_index)
                    _entry["last_name"] = self.validate_str(entry[1], entry_index)
                    _entry["color"] = self.validate_str(entry[4], entry_index)
                    _entry["zipcode"] = self.validate_zipcode(entry[2], entry_index)
                    _entry["phonenumber"] = self.validate_phonenumber(entry[3], entry_index)
                    if None not in _entry.itervalues():
                        self.entries.append(_entry)
            else:
                self.errors.append(container.index(entry))
        self.errors = list(set(self.errors))  # remove duplicate invalid entries
        self.entry_count = len(self.entries) + len(self.errors)
        sorted_entries = sorted(self.entries, key=lambda k: k["last_name"], reverse=False)
        self.entries = sorted_entries
        output = {"entries": self.entries, "errors": self.errors}
        results = json.dumps(output, sort_keys=True, indent=2)
        return results

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

    def validate_str(self, s, ind):
        """
        normalizes string output
        tests if string could be an integer
        invalid if type is not string
        string = self.validate_str(name[0], container.index(entry))
        :param s: string
        :param ind: int
        :return: s: str or None
        """
        try:
            s = int(s)
            self.errors.append(ind)
            return None
        except ValueError:
            if type(s) == str:
                return s.strip()
            else:
                self.errors.append(ind)
                return None

    def output_results(self, op_filename, _json):
        """
        writes and saves _json to op_filename
        :param op_filename: str
        :param _json: str
        :return: result.out: json obj
        """
        with open(op_filename, 'w') as f:
            f.write(_json)
        f.close()


if __name__ == '__main__':
    frm = Formatter()
    r_f = frm.read_file('../data/sample-Liz.in')
    entries = frm.get_entries_by_line(r_f)
    result = frm.analyze_entry(entries)
    frm.output_results("../data/result.out", result)
