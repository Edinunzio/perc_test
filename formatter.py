import json

class Formatter(object):
    def __init__(self):
        self.entries = []
        self.errors = []

    def read_file(self, file):
        f = open(file, 'r')
        txt = f.read()
        f.close()
        return txt

    def get_entries_by_line(self, file_contents):
        """grabs content of each line and appended to array"""
        entries = file_contents.split("\n")
        container = []
        for e in entries:
            x = e.split(",")
            container.append(x)
        self.line_count = len(container)
        return container

    def analyze_entry(self, container):
        """analyzes each entry"""
        for entry in container:
            _entry = {}
            if len(entry) == 4:
                name = entry[0].split(" ")
                _entry["first_name"] = self.validate_str(name[0], container.index(entry))
                _entry["last_name"] = self.validate_str(name[1], container.index(entry))
                _entry["color"] = self.validate_str(entry[1], container.index(entry))
                _entry["zipcode"] = self.validate_zipcode(entry[2], container.index(entry))
                _entry["phonenumber"] = self.validate_phonenumber(entry[3], container.index(entry))
                if None not in _entry.itervalues():
                    self.entries.append(_entry)
            elif len(entry) == 5:
                if "(" in entry[2]:
                    _entry["first_name"] = self.validate_str(entry[1], container.index(entry))
                    _entry["last_name"] = self.validate_str(entry[0], container.index(entry))
                    _entry["color"] = self.validate_str(entry[3], container.index(entry))
                    _entry["zipcode"] = self.validate_zipcode(entry[4], container.index(entry))
                    _entry["phonenumber"] = self.validate_phonenumber(entry[2], container.index(entry))
                    if None not in _entry.itervalues():
                        self.entries.append(_entry)
                else:
                    _entry["first_name"] = self.validate_str(entry[0], container.index(entry))
                    _entry["last_name"] = self.validate_str(entry[1], container.index(entry))
                    _entry["color"] = self.validate_str(entry[4], container.index(entry))
                    _entry["zipcode"] = self.validate_zipcode(entry[2], container.index(entry))
                    _entry["phonenumber"] = self.validate_phonenumber(entry[3], container.index(entry))
                    if None not in _entry.itervalues():
                        self.entries.append(_entry)
            else:
                self.errors.append(container.index(entry))
        self.errors = list(set(self.errors)) # remove duplicate invalid entries
        self.entry_count = len(self.entries) + len(self.errors)
        output = {"entries": self.entries, "errors": self.errors}
        return output

    def validate_phonenumber(self, phone, ind):
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

    def validate_str(self, string, ind):
        try:
            string = int(string)
            self.errors.append(ind)
            return None
        except ValueError:
            if type(string) == str:
                return string.strip()
            else:
                self.errors.append(ind)
                return None




if __name__ == '__main__':
    _fm = Formatter()
    r_f = _fm.read_file('data/sample-Liz.in')
    entries = _fm.get_entries_by_line(r_f)
    result = _fm.analyze_entry(entries)
    #print result
    result = json.dumps(result, sort_keys=True, indent=2)
    x = open('liz_test.json', 'w')
    x.write(result)
    x.close()
