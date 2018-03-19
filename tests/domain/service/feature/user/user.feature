Feature: User register

Scenario: Register a VALID user
    Given a new VALID user
    When we register the user
    Then the user is saved

Scenario: Register a INVALID user
    Given a new INVALID user
    When we register the user
    Then the domain is not allowed and the user is not created