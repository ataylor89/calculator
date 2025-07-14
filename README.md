# calculator

## Usage

If you're on MacOS, you can open the Terminal application, and navigate to the root directory of this project using the cd command. Once you are in the root directory, you can type the following command.

    % python app.py

The command "python app.py" executes the Python program. The module "app.py" is the main module of the project. You can also think of it as the entry point. It starts a web server on port 5000.

After you type the command "python app.py", you can open the URL "http://127.0.0.1:5000/" in a web browser, and you should see the HTML content of the index page.

You can write an expression into the text field, and click on the evaluate button to get an answer.

This is all a little long-winded, so let's write it down as a series of steps.

1. Open Terminal and navigate to the root directory of the project
2. Run the command "python app.py" from the root directory of the project
3. Open the URL "http://127.0.0.1:5000/" in a web browser
4. Type any expression into the text field, like (2+3)^3 + 75, and click on the Evaluate button to see the result

This project uses the Flask framework, and we can talk more later on about how to use Flask. I am going to take a short break and when I get back we can talk about Flask.

## Design

A Python program is composed of modules. A module is an individual Python file (that is, a .py file).

Modules can be organized into packages. A package is a directory of modules.

In order to explain the design of this program, we can describe each module in detail.

Module | Description
------ | -----------
app.py | The main module, the entry point. Starts the web server on port 5000.
\__init__.py | Defines a package variable named "app"
views.py | Defines the request handlers
eval.py | This file has an eval function that evaluates a string expression

You might notice that there is a static folder and a templates folder.

The templates folder contains the HTML files; the static folder contains the JavaScript and CSS files.

The JavaScript file, "events.js", in the static/js directory, contains all of the code for event handling.

The jquery-3.7.1.min.js is a compressed JavaScript library which is used by events.js. The jQuery library makes it easy to read and manipulate DOM elements, like the text inside a text field.

To summarize our discussion... we can write a list of main points, a list of key takeaways.

1. The main module of the project is app.py and we execute this module with the command "python app.py"
2. The main module, app.py, starts the web server on port 5000
3. The views.py module defines the request handlers
4. The eval.py module contains the code for evaluating an expression, like "(2+3)^3 + 75"
5. The __init__.py module defines a package variable named "app" as an instance of the Flask class

It is worth mentioning that we can use the package variable "app" anywhere in our project, just by importing it from the calculator module. This helps us avoid circular dependencies, and any other complications that can arise when sharing a variable between different modules.

Well, it's important to keep this section short, so I'll end it on this note. Sometime later, either tonight or later this week, I'll add a third section to this readme on how to use the Flask framework.
