from scripts.c_preproc import preprocess_c_code, ast_to_code, extract_doxygen_comment
from scripts.llm_querry import LlmDoxify
from scripts.insert_doxygen import insert_comments

C_FILE = './c_files/example.c'
C_OUT  = '.c_files/output.c'

# Example usage
code_without_comments, functions = preprocess_c_code(C_FILE)
#print("Code without comments:")
#print(code_without_comments)

comments = {}
for function in functions:
    print(f"Function at line {function.coord.line}")
    # extract function code
    function_code = ast_to_code(function)
    # get doxygen comment
    response = LlmDoxify(function_code)
    doxygen_comment = extract_doxygen_comment(response)
    print('--------------------------------------------------')
    print(doxygen_comment)
    print('--------------------------------------------------')

    # create dictionary pair
    comments[function.coord.line] = doxygen_comment

# check if all functions got comments
if len(functions) != len(comments):
    raise "Error on LLM querry!"

insert_comments(C_FILE, comments, C_OUT)

