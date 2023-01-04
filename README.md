# Web Application Test Suite
## Description
This test suite is designed to test the functionality of a web application(yandex mail). It includes tests for logging in, creating and sending emails, checking and deleting emails, and logging out.

The tests are organized using the Page Object Model (POM) design pattern, which separates the tests from the implementation details of the web application. This makes the tests more maintainable and easier to understand.

## Test actions
The test suite includes the following test functions:

- **test_log_in** logs in to the web application.
- **test_mail_create** creates and sends an email.
- **test_mail_check** checks the sent and incoming emails, and deletes them.
- **test_log_out** logs out of the web application.

Each test function performs a series of actions on the web application and checks the resulting behavior to ensure that the application is functioning correctly.

## Prerequisites
In order to run these tests, you will need the following software:

- Python 3
- pytest
- Selenium

## Test coverage
The **pytest-cov** plugin can be used to measure the test coverage of the codebase. This will help identify any areas of the code that are not being tested by the test suite.

## Parallel execution
The **pytest-xdist** plugin can be used to run the tests in parallel, which can significantly reduce the total execution time of the test suite.

## Test results
The **pytest-html** plugin can be used to generate a HTML report of the test results, which makes it easier to understand the overall status of the tests and identify any failures.
