# Tests
## Before running
```fessUpDatabase.db``` must be deleted before starting the server.
This is to ensure that the tests are completely reproducible.

The server must then be started before any tests are run.

The test for account creation and sign in must be run first, as it creates an account that will then be used for all further tests.

```runAllTests.py``` will do both of these steps for you before starting all tests.

Make sure that all tests are run from the base directory, __NOT__ from /tests/.

## Running a test
### Command syntax:
```python <test filename> <address>```
### For example:
```python accountCreationAndSignin.py 127.0.0.1:3000```


This will run a test for creating an account and signing in. It will report back if the test was successful.
