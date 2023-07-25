from pycparser import parse_file, c_ast, c_parser, c_generator
import re

class FunctionVisitor(c_ast.NodeVisitor):
    # This function provides functionality to preprocess C code and extract Doxygen comments from it.
    # The AST is obtained using the `parse_file` function from the
    # 'pycoarser' library.

    # The `preprocess_c_code` function takes a file path as input, reads the C code from the file,
    # and then processes it. It first removes any existing comments from the code and then uses the
    # `FunctionVisitor` to extract all the function definitions present in the code. Finally, the
    # modified AST is converted back to C code using the `ast_to_code` function.

    def __init__(self):
        self.functions = []

    def visit_FuncDef(self, node):
        self.functions.append(node)
        self.generic_visit(node)


def preprocess_c_code(file_path):
    # Parse the C code into an AST
    ast = parse_file(file_path, use_cpp=True)

    # Extract functions
    function_visitor = FunctionVisitor()
    function_visitor.visit(ast)

    # Convert the modified AST back to C code
    modified_code = ast_to_code(ast)

    return modified_code, function_visitor.functions

# Convert an AST back to C code
def ast_to_code(ast):
    generator = c_generator.CGenerator()
    return generator.visit(ast)

def extract_doxygen_comment(code):
    pattern = r'(\/\*\*.*?\*\/)'
    matches = re.findall(pattern, code, re.DOTALL)
    return matches[0].strip() if matches else None