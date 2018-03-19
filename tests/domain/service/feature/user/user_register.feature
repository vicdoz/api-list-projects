Feature: User register

Scenario: Successful register
    Given I try to register a user with username "test@vicdoz.com" and password "PASS_SECURE_TEST"
    When we register the user
    Then the user is saved

Scenario: Incorrect register by email domain
    Given I try to register a user with username "test@INVALIDDOMAIN.com" and password "PASS_SECURE_TEST"
    When we register the user
    Then the error "Not allowed domain for this user" is shown

Scenario: Incorrect register by email empty
    Given I try to register a user with username empty and password "PASS_SECURE_TEST"
    When we register the user
    Then the error "Empty email" is shown

Scenario: Incorrect register by password empty
    Given I try to register a user with username "test@vicdoz.com" and password empty
    When we register the user
    Then the error "Empty password" is shown