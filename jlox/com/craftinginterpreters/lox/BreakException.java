package com.craftinginterpreters.lox;

class BreakException extends RuntimeException {
    final Token token;

    BreakException(Token token) {
        this.token = token;
    }
}