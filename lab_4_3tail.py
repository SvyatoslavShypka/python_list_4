import sys


def tail(file, lines=None, bytes=None):
    if bytes is None and lines is None:
        lines = 10

    if file:
        try:
            with open(file, 'rb') as f:
                if bytes is not None:
                    f.seek(-int(bytes), 2)
                byteListLine = f.readlines()
                if lines is not None and lines < len(byteListLine):
                    byteListLine = byteListLine[-int(lines):]
                decoded = []
                for line in byteListLine:
                    # decode from bytes into chars
                    decoded.append(line.decode("utf-8"))
                lines_to_print = decoded
        except FileNotFoundError:
            print("File not found:", file)
            sys.exit(1)
    else:
        lines_to_print = sys.stdin.readlines()
        if bytes is not None:
            lines_all = "\r".join(lines_to_print)
            lines_to_print = lines_all[-bytes:]
    if lines is not None and lines < len(lines_to_print):
        # zero lines - zero printed
        if lines == 0:
            lines_to_print.clear()
        else:
            # print only last few lines
            lines_to_print = lines_to_print[-int(lines):]

    for line in lines_to_print:
        sys.stdout.buffer.write(line.encode())


class SimpleArgumentParser:
    def __init__(self):
        self.args = {}

    def add_argument(self, argv):
        for i in range(1, len(argv)):
            if argv[i] != "<" and argv[i] != "type":
                if argv[i].startswith("--lines"):
                    self.args["lines"] = int(argv[i][8:])
                elif argv[i].startswith("--bytes"):
                    self.args["bytes"] = int(argv[i][8:])
                else:
                    self.args["file"] = argv[i]


if __name__ == "__main__":
    parser = SimpleArgumentParser()
    parser.add_argument(sys.argv)
    tail(parser.args.get("file"), parser.args.get("lines"), parser.args.get("bytes"))
    # test
    # type test.txt | python lab_4_3tail.py --bytes=20
    # python lab_4_3tail.py test.txt --bytes=20
    # python lab_4_3tail.py test.txt --lines=15
    # python lab_4_3tail.py test.txt --lines=2
    # python lab_4_3tail.py test.txt --lines=0
    # type test.txt | python lab_4_3tail.py --lines=2
