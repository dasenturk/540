# constraint_extractor.py

import ast

class ConstraintExtractor:
    def __init__(self, code_snippet):
        self.code_snippet = code_snippet
        self.functions = []
        self.variables = []

    def extract_constraints(self):
        try:
            # Parse the code snippet into an AST
            parsed_code = ast.parse(self.code_snippet)
        except SyntaxError:
            # If there's a syntax error, return empty constraints
            return {'functions': [], 'variables': []}

        # Create a node visitor and walk the AST
        visitor = self.CodeVisitor(self)
        visitor.visit(parsed_code)

        # Return the extracted constraints
        return {'functions': self.functions, 'variables': self.variables}

    class CodeVisitor(ast.NodeVisitor):
        def __init__(self, extractor):
            self.extractor = extractor

        def visit_FunctionDef(self, node):
            # Extract function name and arguments
            func_name = node.name
            args = [arg.arg for arg in node.args.args]
            self.extractor.functions.append({'name': func_name, 'args': args})

            # Process the body of the function
            self.generic_visit(node)

        def visit_Assign(self, node):
            # Extract variable names
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.extractor.variables.append(target.id)

            self.generic_visit(node)
            
