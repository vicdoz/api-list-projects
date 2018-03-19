The objective of this repository is to play with TDD in python.

[![Build Status](https://travis-ci.org/vicdoz/api-list-projects.svg?branch=master)](https://travis-ci.org/vicdoz/api-list-projects)

<b>Requirements</b><br>

Requirement 1:<br>
An API is needed to register users from an email and a password

Requirement 2:<br>
Only users of the domain "vicdoz.com" can be registered

<b>Components</b><br>

Component 1:API -> Receive external requests and invoke the use case<br>
Component 2:Domain -> Use cases,services and domain entities<br>
Component 3:Infraestructure -> Repositories and database models<br>


<b>Testing</b><br>
API: BDD with Behave<br>
Domain: BDD with Behave and Mamba (I am playing with this two)

CI:Travis<br>