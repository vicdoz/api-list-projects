Feature: User register

Scenario: Successful register
    Given a user with username "test@vicdoz.com" and password "PASS_SECURE_TEST"
    When we try to register the user valid
    Then the user is saved

Scenario: Incorrect register by email domain
    Given a user with username "test@INVALIDDOMAIN.com" and password "PASS_SECURE_TEST"
    When  we try to register the user invalid
    Then the error "Not allowed domain for this user" is shown

Scenario: Incorrect register by email empty
    Given a user with username empty and password "PASS_SECURE_TEST"
    When  we try to register the user invalid
    Then the error "Empty email" is shown

Scenario: Incorrect register by password empty
    Given a user with username "test@vicdoz.com" and password empty
    When  we try to register the user invalid
    Then the error "Empty password" is shown

Scenario: Incorrect register both user and password empty
    Given a user with username empty and password empty
    When  we try to register the user invalid
    Then the error "Empty email" is shown