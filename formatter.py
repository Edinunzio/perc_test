class Formatter(object):
    def read_file(self, file):
        f = open(file, 'r')
        txt = f.read()
        f.close()
        return txt


if __name__ == '__main__':
    _fm = Formatter()
    result = _fm.read_file('data/sample-Liz.in')
    print result