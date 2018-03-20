The objective of this repository is to play with TDD in python.
<br>


[![Language](https://img.shields.io/badge/language-python-brightgreen.svg)](https://img.shields.io/badge/language-python-brightgreen.svg)
[![Build Status](https://travis-ci.org/vicdoz/api-list-projects.svg?branch=master)](https://travis-ci.org/vicdoz/api-list-projects)
[![codecov](https://codecov.io/gh/vicdoz/api-list-projects/branch/master/graph/badge.svg)](https://codecov.io/gh/vicdoz/api-list-projects)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f2530e3f0db34ec3ae166b7dadb03a73)](https://www.codacy.com/app/vicdoz/api-list-projects?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vicdoz/api-list-projects&amp;utm_campaign=Badge_Grade)

<b>Requirements</b><br>

Requirement 1: :white_check_mark: <br>
An API is needed to register users from an email and a password

Requirement 2: :white_check_mark: <br>
Only users of the domain "vicdoz.com" can be registered

Requirement 3: :red_circle: <br>
The system can save projects. A project contains:
 - code
 - description
 - url
 - owner
 
<b>Components</b><br>

Component 1:API -> Receive external requests and invoke the use case<br>
Component 2:Domain -> Use cases,services and domain entities<br>
Component 3:Infraestructure -> Repositories and database models<br>


<b>Testing</b><br>
API: BDD with Behave<br>
Domain: BDD with Behave and Mamba (I am playing with this two)

CI:Travis<br>