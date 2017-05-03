Feature:CPC Login

Scenario Outline: CPC Login with different users
Given open CPC application in firefox
When Enter the username as "<username>"
When Enter the password as "<password>"
Then Press the Login Button
Then Close the Broswer

Examples:
    | username    |password  |
    | globaladmin |roZes@123 |
   
