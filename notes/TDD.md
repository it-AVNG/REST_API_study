# Unit Test
Code which tests case
+ Sets up conditions, inputs
+ Runs a code 
+ check outputs with assertions

Benefits:
+ ensures code runs as expected
+ catches bugs
+ Improves reliability
+ Provides confidence

# What is Test Driven Development (TDD)
It is a development practice by write test first of the functionality and then writing code
+ write a test where the code base failed first.
+ Refractor the code to make it pass

# Django test Framework
base on the unittest library
Test client in Django give us a dummy web browser and has simulate authentication
Tempory database of Django help use create and clear a test database
API test client is part of Rest Framework
We either creat `test.py` in our app or have `test` directory that included all the test. The directory must have `__init__.py` 
+ `SimpleTestCase`: No database integration, useful for test that does not need database
+ `TestCase`: integrated database useful for code that uses database

## Test structureL
+ import test class
+ import object to test
+ define the test class
+ add methods for testing, must dtart with `test_`
+ Setup inputs
+ Execute the code to be tested
+ check output
