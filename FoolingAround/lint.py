import ast


class GlobalsVisitor(ast.NodeVisitor):
    def __init__(self):
        self.globals = set()

    def add_globals_from_subtree(self, node):
        for n in ast.walk(node):
            if type(n) is ast.Name:
                self.globals.add(n.id)

    def visit_Assign(self, node):
        for t in node.targets:
            self.add_globals_from_subtree(t)

    def visit_AugAssign(self, node):
        self.add_globals_from_subtree(node.target)

    def visit_AnnAssign(self, node):
        self.add_globals_from_subtree(node.target)

    def visit_FunctionDef(self, node):
        pass

    def visit_Lambda(self, node):
        pass

    def visit_AsyncFunctionDef(self, node):
        pass

    def visit_ClassDef(self, node):
        pass

    def visit_comprehension(self, node):
        pass


tree = ast.parse("""
i = j = k = 0
f = lambda in_lambda: in_lambda + 1
while i < 5:
    i += 1
    in_while = True
def test():
    in_func = 2
print("done")
""")

visitor = GlobalsVisitor()
visitor.visit(tree)
print(visitor.globals)

# tree = ast.parse("""
# i = 0
# while i < 5:
#   i += 1
#   print("done")
# """)
# # print(ast.dump(tree, indent=4))
# visitor = globalsVisitor()
# visitor.visit(tree)
