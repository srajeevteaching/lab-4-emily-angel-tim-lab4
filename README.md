Lab 4

Problem Write a program to determine how much a customer owes their mobile phone provider based on their subscription package and how much data they used. There are three different subscription packages for its customers:

Green: 2GB of data for $49.99/month. Additional GB are $14.99/GB. Additionally, if the customer has a coupon (only applies to green package), there is a further discount of $20 on bills that are $75 or more. Orange: 4GB of data for $69.99/month. Additional GB are $9.99/GB. Purple: $99.99/month for unlimited data. Round: Use the round function to round your output to two decimal places.

Do not do separate price calculations for each package: Use conditional statements to set up variables that plans have in common. Then do the cost calculation in one place using those variables.

Input Validation: Your program must work regardless of the case the package name is typed in and any blank spaces surrounding it; i.e. " gREEn " should be recognized as valid. If the user inputs an invalid package name, tell them that it was invalid and do not give them a bill amount or do any calculations. Do not accept negative numbers for extra data used.

Instructions Create a new Python file and place intro comments using the template below. Use comments to write the algorithm your program will follow. Draw a flowchart and label the possible control paths. You can use graph-drawing software or you can draw it using pen and paper and then submit a picture. Create an Excel file with at least one test case for each control path. Use one row per test case with one column for the case's label matching the flowchart, one column for each input, and one column for each corresponding output. Write the Python code corresponding to each of your algorithm's steps. You will need to import the math module and use the ceil function to round up. Test your program using your test cases. If the output doesn't match, correct your program.

Commit and push changes and check your repository on github.com to confirm your updates before leaving lab (even if not finished).

Intro comments template

Programmers: [your names]
Course: CS151, Dr. Rajeev
Date: Thu Oct 7
Lab: 4
Program Inputs: [What information do you request from the user?]
Program Outputs: [What information do you display for the user?]# lab4fall
