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

    # Test a single number
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
    # For example, you can try running the command `python -m calculator "1+2^3"` to see that it works for the calculator module.
    # We are now going to run the unittest module, a module from the Python standard library.
    # We are going to use the "discover" argument, and we are going to pass the start directory with the -s option.
    # We will use the -v option for verbose output.
    % python -m unittest discover -s tests -v
    test_eval_with_invalid_inputs (test_strategy1.TestStrategy1.test_eval_with_invalid_inputs) ... ok
    test_eval_with_valid_inputs (test_strategy1.TestStrategy1.test_eval_with_valid_inputs) ... ok
    test_eval_with_invalid_inputs (test_strategy2.TestStrategy2.test_eval_with_invalid_inputs) ... ok
    test_eval_with_valid_inputs (test_strategy2.TestStrategy2.test_eval_with_valid_inputs) ... ok
    test_eval_with_invalid_inputs (test_strategy3.TestStrategy3.test_eval_with_invalid_inputs) ... ok
    test_eval_with_valid_inputs (test_strategy3.TestStrategy3.test_eval_with_valid_inputs) ... ok

    ----------------------------------------------------------------------
    Ran 6 tests in 0.001s

    OK

    # Voila! It worked. But what if we want to run each test file individually?
    # We can do that with the syntax `python -m unittest <path_to_test_file>`
    # Here are some examples
    % python -m unittest tests/test_strategy1.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

    % python -m unittest tests/test_strategy2.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

    % python -m unittest tests/test_strategy3.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

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

    # The unit tests contained within the tests folder test the Strategy classes.
    # In particular, they test the Strategy.eval methods, for each strategy.
    # We can think of the Strategy.eval methods as units.
    # I wrote three unit tests for valid inputs, and three unit tests for invalid inputs.
    # The reason we use the word "unit", is that a method is often considered to be the smallest component of code that you want to test.
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

## A brief note on unit testing

The idea behind unit testing is to test a program unit by unit. A unit can be a method, function, or class.

The Strategy.eval methods are important units in my program. There are three Strategy.eval methods in total (one for each strategy).

I test these units in unit tests to make sure that they work properly.

Are there any other units that I should be testing? Honestly, I think the answer is yes.

The AbstractStrategy.parse method is another important unit that I should test. I want to make sure that the expression parsing is correct.

In the future, I might write a test_parser.py file and place it in the tests folder.

The purpose of this file will be to test the AbstractStrategy.parse method.

I can give it different inputs (just like I did with eval) and make sure it produces the correct output.

To return to the initial point, the idea behind unit testing is to test a program unit by unit.

We can say, "This unit works properly. This unit works properly. Are there any units that don't work properly?"

We can test software unit by unit, using unit tests, to make sure that the software works properly.

## Vocabulary (part one)

Before we talk about the design of this project, and the algorithms used, I thought it would help to talk about vocabulary.

Here is a vocabulary sheet, meant to guide the reader through subjects like arithmetic, algebra, and linear algebra.

| Word/Phrase | Definition |
| ----------- | ---------- |
| Operand | An input to an operator; an element from the underlying set of an algebraic structure |
| Operator | A function that operates on one or more operands (e.g. unary operators, binary operators, field operators, etc) |
| Relation | Formally, a set of ordered pairs (we can think of the equality and inequality relations as a set of ordered pairs) |
| Expression | A sequence of mathematical symbols, consisting of operators and operands |
| Equation | A statement which asserts that two expressions are equal |
| Structure | A set with operations and relations (e.g. real number field, group, vector space) |
| Natural numbers | The numbers defined by the Peano axioms (formal); any element from the set {0, 1, 2, 3, ...} (informal) |
| Integers | An integer is an expression of the form a-b, where a and b are natural numbers (formal) |
| Rationals | A rational number is an expression of the form p/q, where p is an integer and q is a non-zero integer (formal) |
| Reals | A real number is a Cauchy sequence (formal); a real number is a point on the number line (informal) |
| Set | A collection of mathematical objects (e.g. the naturals, the integers, the rationals, the reals, the complex numbers, the set of all possible m by n matrices) |
| Vector | A list of numbers |
| Matrix | A rectangular array of numbers |
| Field axioms | I like to remember them with the acronym MAD. The five addition axioms, A1 through A5 (closure, associativity, commutativity, additive identity, additive inverses). The five multiplication axioms, M1 through M5 (closure, associativity, commutativity, multiplicative identity, multiplicative inverses). The distributivity axiom, D for distributivity. Real numbers, together with addition and multiplication, satisfy the eleven field axioms, and so they qualify to be a field. |

## Vocabulary (part two)

Let's look at some examples. I think it often helps to point out some examples.

The string "1 + 2 * 3" is a mathematical expression. It is a sequence of symbols consisting of operands and operators.

In the above string, the operands are 1, 2, and 3. The operators are + and * (addition and multiplication).

Is the string "1" a mathematical expression? My opinion is yes. Some people might argue that it's not. But I have an argument showing that it is. The equation 1 = 1 asserts that two expressions are equal. The expressions are "1" and "1". In the context of equations, I think it's fair to say that "1" is an expression. In other words, a single number is an expression. We might call it a basic expression.

Another argument would be this. We can say that "-1" is an expression on this basis: it consists of the negation operator (-) and a single operand (1). It combines one operator with one operand. Now, if "-1" is an expression, then shouldn't "1" also be an expression?

I think this digression teaches us a lot about rhetoric and argument. We came up with two persuasive arguments claiming that a single number, like 1 or 117, can be considered a basic expression. We said, "if 1 = 1 asserts that two expressions are equal, then isn't the number 1 a basic expression?" We said, "if -1 is an expression, assuming - is the negation operator, then shouldn't 1 also be an expression?"

Now, what about the string "1 + 2 * 3 = 7". Is it also an expression?

The answer is no. The string "1 + 2 * 3 = 7" is not an expression. It's something else. It is actually called an equation.

An equation asserts that two expressions are equal. The equation above asserts that "1 + 2 * 3" is equal to "7".

When we write an expression, we are drawing from a set (the real numbers) and a list of operators (addition, subtraction, multiplication, division, powers, roots, parentheses, etc).

When we write an equation, we are drawing from a set (the real numbers), a list of operators (PEMDAS), and the equality relation.

A structure has everything that we need to write an equation. When we write an equation, we are working in a structure.

In the context of this project, we are working with the real number field. The equations that you see in tests/test_data/valid_inputs.txt are based in the real number field. When we write equations involving real numbers, we are working in the real number field.

The real number field is a useful algebraic structure. There are other useful algebraic structures, like groups and vector spaces.

When we write a linear transformation y = Ax, where x and y are vectors and A is a matrix, we are working in a vector space.

We can use the equation y = Ax to solve a system of linear equations, and also to transform (rotate/reflect/scale/shrink) a vector.

In fact, we can express every possible linear transformation as an equation of the form y = Ax, where x and y are vectors and A is a transformation matrix.

So we have talked about two algebraic structures thus far: the real number field and vector spaces.

The underlying set of the real number field is the real numbers, as the name suggests.

The underlying set of a vector space can be any set of vectors that satisfies the requirements of a vector space.

For example, the underlying set of a vector space could be the set of m by n matrices, for all positive integers m and n.

When we write an equation involving matrices, or when we write a linear transformation, it is common to use this underlying set, the set of all m by n matrices.

I don't want to take too long talking about this subject. But before I move on, I think it helps to review.

## Review

Let's review what we learned with a list of key points.

1. When we write equations, we work with numbers (operands), operators, and the equality relation
2. When we write equations, we are working in a mathematical structure
3. When we write equations like "1 + 2 * 3 = 7", we are working in the real number field
4. A mathematical expression is a sequence of symbols consisting of operators and operands
5. A mathematical equation is a statement which asserts that two expressions are equal
6. We need operands and operators to write expressions
7. We need operands, operators, and the equality relation to write equations
8. The real number field is a common algebraic structure
9. We are accustomed to real numbers and we are accustomed to the field operators (PEMDAS)
10. When we evaluate a mathematical expression, written in infix notation, we have to follow the order of operations (OOO)
11. When we evaluate a mathematical expression, written in postfix notation, we don't need the PEMDAS rules
12. When we write a mathematical expression using infix notation, we often need parentheses
13. When we write a mathematical expression using postfix notation, we don't need parentheses
14. It is easier for a program to evaluate postfix notation than it is to evaluate infix notation
15. For this reason, we often convert infix to postfix, when we want to write a program that evaluates an expression
16. Infix notation looks like "1 + 2 * 3" (the operators are placed in between the operands)
17. Postfix notation looks like "1 2 3 * +" (the operators are placed after the operands)
18. When we evaluate a postfix expression, we can be greedy, and perform an operation wherever possible
19. When we evaluate an infix expression, we have to identify the highest ranking operation, and perform the highest ranking operation
20. For example, when we evaluate "1 + 2 * 3", the highest ranking operation is "2 * 3", so we perform that operation first.

I think this succeeds in reviewing what we talked about before... but it also introduces some interesting new points.

I think it's fitting to talk about mathematical expressions, mathematical equations, and mathematical structures in a project like this.

I find the subject really fascinating, and I wanted to share what I have learned.

## A brief note on the real number field

The real numbers are a set, the set of all Cauchy sequences, the set of all points on the real number line.

The real number field is a structure. It combines the set of real numbers with all of the field operations and field relations.

The field operations are commonly referred to as PEMDAS. (We can think of parentheses as precedence operators.)

The field relations, to my knowledge, are equality and inequality.

(But it's also possible to include other relations, like the subset relation and the memberOf relation.)

So the real numbers are the set of all numbers that can be represented as points on the number line (1, sqrt(2), π, e, et cetera).

The real number field is a structure consisting of (1) the real numbers (2) the field operations (3) the field relations.

The real numbers qualify to be a field, when combined with PEMDAS and the equality relation.

The integers, on the other hand, do not quality to be a field, because they do not satisfy the requirements of a field (in particular, the integers do not have multiplicative inverses, which are needed to be a field).

I wanted to explain the difference between the "real numbers" and the "real number field".

The real numbers are a set; the real number field is a structure.
