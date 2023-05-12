from sys import exit, argv
from os.path import join


def main():
    if len(argv) != 2:
        exit("Usage: generate_ast.py <output directory>")

    ExprTypes = [
        "Assign   : Token name, Expr value",
        "Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : Object value",
        "Unary    : Token operator, Expr right",
        "Variable : Token name",
    ]

    StmtTypes = [
        "Expression : Expr expression",
        "Print      : Expr expression",
        "Var        : Token name, Expr initializer",
    ]

    outputDir = argv[1]
    defineAst(outputDir, "Expr", ExprTypes)
    defineAst(outputDir, "Stmt", StmtTypes)


def defineAst(outputDir: str, baseName: str, types: list) -> str:
    with open(join(outputDir, baseName + ".java"), "w") as codeFile:

        # Headers
        codeFile.write("package com.craftinginterpreters.lox;\n")
        codeFile.write("\n")
        codeFile.write("import java.util.List;\n")
        codeFile.write("\n")
        codeFile.write("abstract class " + baseName + " {\n\n")

        # Visitor Interface
        codeFile.write("    interface Visitor<R> {\n")

        # Visitor types
        for typ in types:
            typeName = typ.split(":")[0].strip()
            codeFile.write(f"       R visit{typeName}{baseName}({typeName} {baseName.lower()});\n")

        codeFile.write("    }\n\n")

        # Types
        for typ in types:
            className = typ.split(":")[0].strip()
            fieldList = typ.split(":")[1].strip()

            # Subclass
            codeFile.write(f"    static class {className} extends {baseName} " + "{\n")
            codeFile.write(f"        {className} ({fieldList}) " + "{\n")

            # Constructor
            fields = fieldList.split(", ")
            for field in fields:
                name = field.split(" ")[1]
                codeFile.write(f"            this.{name} = {name};\n")

            codeFile.write("        }\n\n")

            # Accept for visitor
            codeFile.write("        @Override\n")
            codeFile.write("        <R> R accept(Visitor<R> visitor) {\n")
            codeFile.write(f"            return visitor.visit{className}{baseName}(this);\n")
            codeFile.write("        }\n\n")

            # Fields
            for field in fields:
                codeFile.write(f"        final {field};\n")

            codeFile.write("    }\n\n")

        # Base accept method
        codeFile.write("    abstract<R> R accept(Visitor<R> visitor);\n")
        codeFile.write("}")


if __name__ == "__main__":
    main()
