import sys

flag = []
file_path = []
count = None
DEFAULT_COUNT = 10

def count_lines(count, source):
    lines = 0
    for line in source:
        print(line, end='')
        lines += 1
        if lines >= count:
            break

def count_bytes(count, source):
    print("count_bytes not implemented")

# def count_bytes(count, source):
#     byte_count = 0
#     for line in source:
#         byte_count += len(line.encode('utf-8'))
#         if bytes > count:
#             break
#     if bytes < count:
#         print(bytes+'%')
#     print(bytes)

def parse_flags():
    file_path = []
    count = None
    for args in sys.argv[1:]:
        if args.startswith("-"):
            valid_flags = ["-n", "-c"]
            if args not in valid_flags:
                print(f"cchead: illegal option -- {args}")
                print("head [-n lines | -c bytes] [file ...]")
                sys.exit(1)
            flag.append(args)
        elif args.isdigit():
            count = int(args)
        elif args.lstrip('-').isdigit():
            count = int(args)
            if count <= 0:
                print("head: illegal line count --", count)
                sys.exit(1)
        else:
            file_path = args
    return flag, count, file_path

flag, count, file_path = parse_flags()

def head_count(source):
    if flag and "-n" in flag:
        count_lines(count if count else DEFAULT_COUNT, source)
    elif flag and "-c" in flag:
        if count is None:
            print("head: illegal byte count --",source)
            sys.exit(1)
        count_bytes(count, source)
    else:
        count_lines(DEFAULT_COUNT, source)

if not sys.stdin.isatty():
    head_count(sys.stdin)
else:
    if file_path:
        try:
            with open(file_path, 'r') as file:
                head_count(file)
        except FileNotFoundError:
            print(f"cchead: {file_path}: No such file or directory")
            sys.exit(1)
    else:
        print("No file path provided")





