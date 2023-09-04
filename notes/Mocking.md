# What is Mocking
+ Override or change behaviour of dependencies
+ Avoid unintended side effects
+ Isolate code being tested

# Why Mocking
+ Avoid relying external services : cant guarantee the are available
+ Makes tests unpredictable and inconsistent


# Avoid unintended consequences
+ Accidentals sending emails
+ Overloading external services

example:
Register_User() --> create_in_db() --> send_welcome_email()
mocking the send email method
prevent email being send but ensure it is working as intended

# how to mock?
use `unittest.mock`
`magicMock/Mock`: replace the real objects
`patch` allow us to modify the code to check



