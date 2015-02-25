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
        return container

    def analyze_entry(self, container):
        """analyzes each entry"""
        for entry in container:
            _entry = {}
            if len(entry) == 4:
                name = entry[0].split(" ")
                _entry["first_name"] = name[0]
                _entry["last_name"] = name[1]
                _entry["color"] = entry[1]
                _entry["zipcode"] = entry[2]
                _entry["phonenumber"] = entry[3]
                self.entries.append(_entry)
            elif len(entry) == 5:
                if "(" in entry[2]:
                    _entry["first_name"] = entry[1]
                    _entry["last_name"] = entry[0]
                    _entry["color"] = entry[3]
                    _entry["zipcode"] = entry[4]
                    _entry["phonenumber"] = entry[2]
                    self.entries.append(_entry)
                else:
                    _entry["first_name"] = entry[0]
                    _entry["last_name"] = entry[1]
                    _entry["color"] = entry[4]
                    _entry["zipcode"] = entry[2]
                    _entry["phonenumber"] = entry[3]
                    self.entries.append(_entry)
            else:
                self.errors.append(container.index(entry))
        return self.errors, self.entries


if __name__ == '__main__':
    _fm = Formatter()
    #result = _fm.read_file('data/empty.txt')
    r_f = _fm.read_file('data/sample-Liz.in')
    entries = _fm.get_entries_by_line(r_f)
    #result = entries
    result = _fm.analyze_entry(entries)
    #result = _fm.get_entries_by_line(r_f)
    print result