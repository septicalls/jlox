from sys import exit, argv
from os.path import join


def main():
    if len(argv) != 2:
        exit("Usage: generate_ast.py <output directory>")

    output_dir = argv[1]

    expr_types = [
        "Assign   : Token name, Expr value",
        "Binary   : Expr left, Token operator, Expr right",
        "Call     : Expr callee, Token paren, List<Expr> arguements",
        "Get      : Expr object, Token name",
        "Grouping : Expr expression",
        "Literal  : Object value",
        "Logical  : Expr left, Token operator, Expr right",
        "Set      : Expr object, Token name, Expr value",
        "This     : Token keyword",
        "Unary    : Token operator, Expr right",
        "Variable : Token name",
    ]

    stmt_types = [
        "Block      : List<Stmt> statements",
        "Break      : Token token",
        "Class      : Token name, List<Stmt.Function> methods",
        "Expression : Expr expression",
        "Function   : Token name, List<Token> params, List<Stmt> body",
        "If         : Expr condition, Stmt thenBranch, Stmt elseBranch",
        "Print      : Expr expression",
        "Return     : Token keyword, Expr value",
        "Var        : Token name, Expr initializer",
        "While      : Expr condition, Stmt body",
    ]

    define_ast(output_dir, "Expr", expr_types)
    define_ast(output_dir, "Stmt", stmt_types)


def define_ast(output_dir: str, base_name: str, types: list):
    with open(join(output_dir, base_name + ".java"), "w") as code_file:
        code_file.write("package com.craftinginterpreters.lox;\n\n")
        code_file.write("import java.util.List;\n\n")
        code_file.write(f"abstract class {base_name} {{\n\n")

        write_visitor_interface(code_file, base_name, types)
        write_types(code_file, base_name, types)
        write_base_accept_method(code_file)

        code_file.write("}")


def write_visitor_interface(code_file, base_name, types):
    code_file.write(f"    interface Visitor<R> {{\n")

    for typ in types:
        type_name = typ.split(":")[0].strip()
        code_file.write(f"        R visit{type_name}{base_name}({type_name} {base_name.lower()});\n")

    code_file.write("    }\n\n")


def write_types(code_file, base_name, types):
    for typ in types:
        class_name = typ.split(":")[0].strip()
        field_list = typ.split(":")[1].strip()

        code_file.write(f"    static class {class_name} extends {base_name} " + "{\n")
        code_file.write(f"        {class_name} ({field_list}) " + "{\n")

        fields = field_list.split(", ")
        for field in fields:
            name = field.split(" ")[1]
            code_file.write(f"            this.{name} = {name};\n")

        code_file.write("        }\n\n")
        code_file.write("        @Override\n")
        code_file.write("        <R> R accept(Visitor<R> visitor) {\n")
        code_file.write(f"            return visitor.visit{class_name}{base_name}(this);\n")
        code_file.write("        }\n\n")

        for field in fields:
            code_file.write(f"        final {field};\n")

        code_file.write("    }\n\n")


def write_base_accept_method(code_file):
    code_file.write("    abstract<R> R accept(Visitor<R> visitor);\n")


if __name__ == "__main__":
    main()
