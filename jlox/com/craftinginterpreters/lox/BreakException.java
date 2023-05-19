package com.craftinginterpreters.lox;

class BreakException extends RuntimeException {
    final Token token;

    BreakException(Token token) {
        super(null, null, false, false);
        this.token = token;
    }
}