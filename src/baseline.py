# rule_based_baseline.py

class RuleBasedBaseline:
    def __init__(self):
        # Define common keywords and their typical structures
        self.keyword_structures = {
            'def': 'def function_name():',
            'for': 'for item in collection:',
            'if': 'if condition:',
            'class': 'class ClassName:',
            '"""': '"""Docstring Description"""',
            '#': '# TODO: ',
            'try': 'try:\n    # code\nexcept ExceptionName:\n    # handle exception'
        }
        # Common control structures
        self.control_structures = {
            'if': 'elif condition: # or else:',
            'elif': 'else:'
        }
        # Common variable names and methods
        self.variable_suggestions = {
            'int': ['count', 'index'],
            'str': ['name', 'title'],
            'list': ['append', 'remove', 'sort'],
            'dict': ['keys', 'values', 'items']
        }
        # Common import statements
        self.import_statements = {
            'numpy': 'import numpy as np',
            'pandas': 'import pandas as pd'
            # Add other common libraries as needed
        }

    def generate_suggestion(self, context):
        # Keyword Completion and Control Structures
        for keyword, structure in self.keyword_structures.items():
            if context.startswith(keyword):
                return structure

        # Indentation Management
        if context.endswith(':'):
            return '    '  # Indentation with 4 spaces

        # Function Snippets and Variable Suggestions
        for key, suggestions in self.variable_suggestions.items():
            if key in context:
                return suggestions[0]  # Return the first suggestion for simplicity

        # Import Statements
        for key, statement in self.import_statements.items():
            if key in context:
                return statement

        # Default to an empty string if no rule applies
        return ''
