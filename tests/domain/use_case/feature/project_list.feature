Feature: Receive list of projects

Scenario: Receive list empty of projects without filters
    Given no projects
    When we request a list
    Then no project is returned
#
#Scenario: Receive list with projects without filters
#    Given one project at database
#    When we request a list
#    Then the project is returned