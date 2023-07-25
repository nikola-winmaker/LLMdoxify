def insert_comments(original_file, function_comments, output_file):
    # The `insert_comments` function is designed to insert function comments extracted from an AST
    # back into the original C code file. It takes three parameters:
    #   - `original_file`: The path to the original C code file that needs to be modified.
    #   - `function_comments`: A dictionary containing line numbers as keys and function comments as values.
    #     Each key represents the line number where the comment should be inserted, and the corresponding
    #     value is the Doxygen comment to be inserted.
    #   - `output_file`: The path to the output file where the modified code, with inserted comments,
    #     will be saved.

    # The function reads the content of the `original_file` and stores each line in the `lines` list.
    # It then creates a new list, `modified_lines`, which will hold the modified code with comments.
    # The `line_offset` variable is used to keep track of the changes in the line numbers due to the
    # inserted comments.

    # The function then iterates through each line of the original code using enumerate. If the current
    # line number (`i + 1`) is found in the `function_comments` dictionary, it means a function comment
    # should be inserted before the current line. The corresponding comment is retrieved from the
    # `function_comments` dictionary and added to `modified_lines`, followed by the original line.
    # The `line_offset` is updated based on the number of lines added with the comment.

    # If the line number is not in the `function_comments` dictionary, it means no comment needs to
    # be inserted, so the original line is appended to `modified_lines` without any changes.
    # After processing all the lines, the modified content is written to the `output_file`.

    with open(original_file, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    line_offset = 0

    for i, line in enumerate(lines):
        if i + 1 in function_comments:
            comment = function_comments[i + 1]
            modified_lines.append(comment + '\n')
            modified_lines.append(line)
            line_offset += len(comment.split('\n')) + 1
        else:
            modified_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(modified_lines)

    print(f"Comments inserted successfully into '{output_file}'.")
