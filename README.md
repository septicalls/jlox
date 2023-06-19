# jlox
My implementation of jlox as described by Robert Nystrom in [crafting interpreters](https://craftinginterpreters.com/contents.html).

## Requirements
1. Java 18 or higher.
2. Gradle 8.0.1 or higher.

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/septicalls/jlox.git
    cd jlox/
    ```

2. *nix users:
    ```
    chmod +x jlox.sh
    ./jlox.sh [script.lox]
    ```

    Windows users: Right-click on `jlox.bat` and select "Run" to execute it.

## Features
- Supports reading user input with native functions `scanNum()` that returns a double, and `scanText()` that returns a String.
- Rewrote GenerateAST.java in Python.

## Challenges
- [x] Support C-style multiline comments.
- [x] Support C-style ternary operator.
- [x] Support C-style comma expressions.
- [ ] Report errors when binary operator appears without left operand.
- [x] `+` concatenates if either operand is a string.
- [x] Division by zero throws runtime error.
- [x] REPL implicitly prints expressions.
- [x] Support C-style `break` syntax.
- [ ] Support lambda functions.
- [ ] Resolver reports if a variable is never used.
- [ ] Extend the resolver to associate a unique index for each local variable declared in a scope.
- [ ] Support static methods.
- [ ] Support getter methods.
- [ ] Replace `super` method lookup with BETA semantics.