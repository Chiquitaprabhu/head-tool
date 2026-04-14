problem statement
Here we are building our own version of the Unix command line tool head. The head tool displays the first N lines or bytes of a file or stdin input.
functional requirements
- Supports flag -n [count] to output the first N lines
- Supports flag -c [count] to output the first N bytes
- When no flag is given, outputs the first 10 lines (default)
- Accepts input from a file path argument
- Accepts input from stdin when data is piped in
- Supports count that is more than the lines for the file, in that case we ouput the max lines in the file.
error handling
Error Handling:
- [invalid number — will throw an error saying -  illegal line count.]
- [missing file — will throw an error saying - No such file or directory.]
- [no arguments — ]
non-functional requirements 
Memory : We will only read as many lines or characters as given in the input into the memory.
Error Handling : The tool displays clean, user-friendly error messages for invalid flags and missing files. No Python tracebacks are shown to the user.

Data Flow Diagram:

sys.argv → [parse_flags()] → flags, [count] ,file_path
                                    ↓
                    file or stdin → [count_lines(count,source)]  | [count_bytes(count,source)]
                                    ↓
                                  print output

structure

- parse_flags(): loops through sys.argv, separates flags from the count and filename, validates flags against supported options (-n, -c), and returns the output.
- count_lines(count, source): takes any line source (file or stdin) and computes number of lines as per the count. Reads one line at a time to keep memory usage low. 
- count_bytes(count, source): takes any line source (file or stdin) and computes number of bytes as per the count. Reads one line at a time to keep memory usage low. 
- Main flow: 
1. Parse and validate arguments (exit early if invalid flag)
2. Determine input source (file or stdin)
3. Call count_lines or count_bytes with the source (catch FileNotFoundError | catch ValueError)
4. Display results

design decisions
- Chose manual sys.argv parsing over argparse so that we learn file I/O 
- Create two methods count_lines and count_bytes depending on the flags passed, the file here will only be read once and 
will be passed to the correcponding functions.