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
- [no arguments — wait for user to input]
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

- parse_flags(): loops through sys.argv, separates flags from the count and filename, validates flags against supported options (-n, -c), count against isdigit() and returns the output.
- count_lines(count, source): takes any line source (file or stdin) and computes number of lines as per the count. Reads one line at a time to keep memory usage low. 
- count_bytes(count, source): takes any line source (file or stdin) and computes number of bytes as per the count. Reads one line at a time to keep memory usage low. 
- Main flow: 
1. Parse and validate arguments (exit early if invalid flag)
2. Determine input source (file or stdin)
3. Call count_lines or count_bytes with the source (catch FileNotFoundError | catch ValueError)
4. Display results

design decisions
- Chose manual sys.argv parsing over argparse because the tool only has two flags. Manual parsing is simpler to implement and easier to read for a small number of arguments. For a tool with many flags or complex argument relationships, argparse would be the better choice. 
- Create two methods count_lines and count_bytes depending on the flags passed, the file here will only be read once and 
will be passed to the correcponding functions. 

Testing
compare against head tool:
[1] empty file
[2] file with no new line
[3] file with count greater than the number of lines present in the file
[4] file with bytes greater than the number of bytes present in the file
[5] Invalid number
[6] nonexistent file
[7] test stdin input (piping) 
[8] head -n 5 -c 10 motivation.txt
