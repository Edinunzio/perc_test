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
            if len(entry) == 4:
                self.entries.append(entry)
            elif len(entry) == 5:
                self.entries.append(entry)
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