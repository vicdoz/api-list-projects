Feature: User login

Scenario: Successful login
    Given a user to login with username "test@vicdoz.com" and password "PASS_SECURE_TEST"
    When we try to login the user valid
    Then the user is logged

Scenario: Incorrect login by email domain
    Given a user to login with username "test@INVALID.com" and password "PASS_SECURE_TEST"
    When  we try to register the user invalid
    Then the error when login "Not allowed domain for this user" is shown

Scenario: Incorrect login by email empty
    Given a user to login with username empty and password "PASS_SECURE_TEST"
    When  we try to register the user invalid
    Then the error when login "Empty email" is shown

Scenario: Incorrect login by password empty
    Given a user to login with username "test@vicdoz.com" and password empty
    When  we try to register the user invalid
    Then the error when login "Empty password" is shown

Scenario: Incorrect login both user and password empty
    Given a user to login with username empty and password empty
    When  we try to register the user invalid
    Then the error when login "Empty email" is shown