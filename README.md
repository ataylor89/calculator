# readme

## Usage

I might add more sections later, and give a detailed explanation of the code. But for now, let's write a short section on usage.

The program can be run with the command `python calculator.py <arithmetic_expression>`. Here are some examples.

    # Test simple addition
    % python calculator.py "1 + 1"
    2

    # Test order of operations (it should be 7 instead of 9)
    % python calculator.py "1 + 2 * 3"
    7

    # Test left associativity of addition and subtraction (it should be 2 instead of -4)
    % python calculator.py "1 - 2 + 3"

    # Test right associativity of powers (it should be 2417851639229258349412352 instead of 4096)
    % python calculator.py "2^3^4"
    2417851639229258349412352

    # Test a single numeric input
    % python calculator.py "1"
    1

    # Test a long expression with many operations
    % python calculator.py "1 + (2 * 3) - (4 * 5) + (6 * 7) + 8^9 + -10"
    134217747

    # Test division
    % python calculator.py "1/3 + 2/3 + 1/2"
    1.5

    # Check that division by zero raises an error
    % python calculator.py "1/0"
    Division by zero is not allowed

    # Test error handling (round 1)
    % python calculator.py "1+"
    The + operation is missing one or more operands

    # Test error handling (round 2)
    % python calculator.py "abcdefghijklmnop99+11+2^2"
    The expression contains one or more invalid characters

    # Test error handling (round 3)
    % python calculator.py ""
    The expression is empty

We were able to test many cases by passing arguments to the calculator program. But we can also test the program by running unit tests.

(I added unit tests to the tests folder, and I added test data to the tests/test_data folder.)

The unit tests can be run in the following ways.

    # First, let's navigate to the root directory of the project. This is the root directory for me, but it might be different for you.
    % cd ~/Github/calculator
    % ls
    calculator.py	strategies	tests

    # The command python -m <module_name> runs a module. It can be a module you wrote, or a module from the standard library.
    # For example, you can try running the command `python -m calculator.py "1+2^3"` to see that it works for the calculator module.
    # We are now going to run the unittest module, a module from the Python standard library.
    # We are going to use the "discover" argument, and we are going to pass the start directory with the -s option.
    # We will use the -v option for verbose output.
    % python -m unittest discover -s tests -v
    test_strategy1 (test_invalid_inputs.TestInvalidInputs.test_strategy1) ... ok
    test_strategy2 (test_invalid_inputs.TestInvalidInputs.test_strategy2) ... ok
    test_strategy3 (test_invalid_inputs.TestInvalidInputs.test_strategy3) ... ok
    test_strategy1 (test_valid_inputs.TestValidInputs.test_strategy1) ... ok
    test_strategy2 (test_valid_inputs.TestValidInputs.test_strategy2) ... ok
    test_strategy3 (test_valid_inputs.TestValidInputs.test_strategy3) ... ok

    ----------------------------------------------------------------------
    Ran 6 tests in 0.001s

    OK

    # Voila! It worked. But what if we want to run each test file individually?
    # We can do that with the syntax `python -m unittest <path_to_test_file>`
    # Here are some examples
    % python -m unittest tests/test_valid_inputs.py
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK

    % python -m unittest tests/test_invalid_inputs.py
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK

    # We were able to run the test files individually. We were also able to run all test files in one go, using the "discover" argument.
    # I think this concludes our discussion on Python's unittest module.

    # Testing is often an important part of software development. You can see that it's very relevant for this project.
    # The nice thing about the unittest module, is that it is built in to the Python standard library.
    # We don't have to download it from an external source. It's already built in. We just have to import it.
    # I try to use the standard library as much as possible. But sometimes I download an external library (e.g. Flask).
    # I use the pip package manager to download external libraries (like Flask). pip takes care of the work and does the heavy lifting.
    # But I digress. We have veered off the main subject of conversation. We are talking about calculator and unit tests.
        
    # I often ask myself, "What is unit testing?" My understanding is that a unit is a method, function, or class.
    # A unit test tests a method, function, or class.
    # (The words "method" and "function" are often interchangeable, but sometimes "method" refers to an object's method.)

    # The unit tests contained within tests/test_valid_inputs.py and tests/test_invalid_inputs.py test the Strategy classes.
    # In particular, they test the Strategy.eval methods, for each strategy.
    # We can think of the Strategy.eval methods as units. There are three Strategy classes, so it's natural to write three unit tests.
    # I wrote three unit tests for valid inputs, and three unit tests for invalid inputs.
    # The reason we use the word "unit", is that a method is considered to be the smallest component of code that you want to test.
    # I said earlier that a unit can be a class, but it is most often considered to be a method or a function.

    # I wanted to talk a little bit about unit testing. But now it's time to wrap things up.
    # I might add more sections to this readme later.
    # For the meantime, it explains how to run the program and run the unit tests.

Alright, I'm out of the code block, and back to the main scope.

This section explains how to use the program and run the unit tests.

I might add more sections later, but it suffices for now.

I am planning to explain, in the future, how strategy1.py and strategy2.py use stacks and iteration, and how strategy3.py uses recursion.

It's hard to find a good use case for stacks. Evaluating an arithmetic expression is a really good use case for stacks.

Furthermore, it's hard to find a good use case for postfix notation. Evaluating an arithmetic expression is a really good use case for postfix notation.

In my opinion, strategy1.py (which uses postfix) is the simplest algorithm, and the easiest to follow. That is why I made it the default.

We can talk about these things, in more detail, in the next sections.
