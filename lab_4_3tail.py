import sys
import argparse


def tail(file, lines=None, bytes=None):
    if bytes is None and lines is None:
        lines = 10

    if file:
        print("file: " + file)
        try:
            with open(file, 'rb') as f:
                if bytes is not None:
                    f.seek(-int(bytes), 2)
                lines_to_print = f.readlines()
                print(lines_to_print)
                decoded = []
                for line in lines_to_print:
                    decoded.append(line.decode("utf-8"))
                print(decoded)
                lines_all = "".join(decoded)
                lines_to_print = lines_all
        except FileNotFoundError:
            print("File not found:", file)
            sys.exit(1)
    else:
        print("else")
        lines_to_print = sys.stdin.readlines()
        print(lines_to_print)
        if bytes is not None:
            lines_all = "\r".join(lines_to_print)
            print(type(lines_all))
            lines_to_print = lines_all[-bytes:]
            print(lines_to_print)

    if lines is not None:
        lines_to_print = lines_to_print[-int(lines):].encode()
    # else:
    #     lines_to_print = lines_to_print[-int(lines):]

    # sys.stdout.buffer.write(lines_to_print.encode())
    # for line in lines_to_print:
    if bytes is None:
        print(bytes)
        sys.stdout.buffer.write(lines_to_print)
    else:
        sys.stdout.buffer.write(lines_to_print.encode())



class SimpleArgumentParser:
    def __init__(self):
        self.args = {}

    def add_argument(self, argv):
        for i in range(1, len(argv)):
            print("arg: " + argv[i])
            if argv[i] != "<" and argv[i] != "type":
                if argv[i].startswith("--lines"):
                    self.args["lines"] = int(argv[i][8:])
                elif argv[i].startswith("--bytes"):
                    self.args["bytes"] = int(argv[i][8:])
                else:
                    self.args["file"] = argv[i]

    # def parse_args(self):
    #     parsed_args = {}
    #     i = 1
    #     while i < len(argv):
    #         if argv[i][:7] in self.args:
    #             nargs = self.args[argv[i][:7]]
    #             if nargs == 1:
    #                 parsed_args[argv[i]] = argv[i + 1]
    #                 i += 2
    #             else:
    #                 parsed_args[argv[i]] = argv[i + 1:i + 1 + nargs]
    #                 i += 1 + nargs
    #         else:
    #             parsed_args["file"] = argv[i]
    #             i += 1
    #     return parsed_args


if __name__ == "__main__":
    parser = SimpleArgumentParser()
    parser.add_argument(sys.argv)
    # nargs=1 oznacza jeden argument do "--lines" nargs = '?' oznacza 0 lub 1 argument
    # parser.add_argument("--lines", nargs=1)
    # parser.add_argument("--bytes", nargs=1)
    # parser.add_argument("file", nargs="?")

    # print(parser)
    # arg_num = len(sys.argv)
    # print("arg_num= ", arg_num)
    # for i in range(arg_num):
    #     print(sys.argv[i])
    # args = parser.parse_args()
    #
    # print(args)

    # parser = argparse.ArgumentParser(description="Print the last lines of a file or stdin.")
    # parser.add_argument("file", nargs="?", help="File to read from.")
    # parser.add_argument("--lines", "-n", type=int, help="Number of lines to print.")
    # parser.add_argument("--bytes", "-c", type=int, help="Number of bytes to print.")
    # args = parser.parse_args()
    #
    # python lab_4_3tail.py --lines=5 test.txt
    # python lab_4_3tail.py --bytes=50 test.txt
    # cat test.txt | python lab_4_3tail.py
    # type test.txt | python lab_4_3tail.py
    # python lab_4_3tail.py test.txt
    # cat inny_plik.txt | python lab_4_3tail.py test.txt
    #
    # tail(args.get("file"), args.lines, args.bytes)
    tail(parser.args.get("file"), parser.args.get("lines"), parser.args.get("bytes"))
    #
    # logs = read_log()
    # # testowy wydruk     python lab_4_3tail.py < test.txt
    # for log in logs:
    #     print(log)
