class Formatter(object):
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

    '''def analyze_entry(self, entries):
        """analyzes each entry"""
        container = []
        for e in entries:
            x = e.split(",")
            container.append(x)
        return container'''

if __name__ == '__main__':
    _fm = Formatter()
    #result = _fm.read_file('data/empty.txt')
    r_f = _fm.read_file('data/sample-Liz.in')
    entries = _fm.get_entries_by_line(r_f)
    result = entries
    #result = _fm.analyze_entry(entries)
    #result = _fm.get_entries_by_line(r_f)
    print result