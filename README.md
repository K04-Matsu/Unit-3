# Unit-3: New Project 
![](game.gif)

# Criteria A: Planning

## Context and Solution
Reiji Nishikawa, student at UWC ISAK Japan who takes the IB program is needing a programmer who can code a program that tracks his summative assignments. The summative tracker must include the 6 success criterias listed below. Regarding this, I will be creating a product that meets all the requirements.
The solution product will be made with PyCharm, and will be coded with the Python3.7 associated with KivyMD and SQLAlchemy. This KivyMD differs from normal Kivy. KivyMD, which is shortened for Kivy Material Design is a package Kivy design widgets. SQL is a library configuration language, and this time we will be using specifically SQLAlchemy. Pros and justification of used languages will be explained below. The program will start off from an title screen with email text box, password text box, login button and register button. The login button will simply login the user if correct email and password is entered, leading to the home screen. The register button will move the screen to register screen where the user can input their username, email and password. In the home screen, the list of entered summative will be shown. Below list, there will be a button which leads to the summative adding page. User will be required to put subject name along with the due date information. The due date can be selected through the calendar interface which will pop when "Add Date" button is pressed. When the summative is added, it will be added to both list screen and database. This is the overall look of this project solution. The name of this product is the "Summative Tracker."

## Success Criteria
### 1. Register and Login system.
### 2. Minimalist design.
### 3. Calendar style interface to add the assignments.
### 4. Screen with the list of all recorded assignments.
### 5. Assignments should have subject and date label.
### 6. The password should be encrypted.

### Justification

#### Python
The Python 3.7 is a widely-known language for its easy usage and simple syntax. And since the language is vastly recognised, there are countless materials and community websites to support the programmer. In addition to this, Python has flexibility and big database which gives versatility, efficiency, reliability, and speed to the language. Another factor is the compatibility with KivyMD and SQLAlchemy, which are both essential languages to create an application. Lastly, Python is the only main language I have learned so far in this IB academic course, and I am most comfortable with it. This experience will directly connect to the overall performance of the product, and considering this, I will be using Python.

#### KivyMD
The KivyMD is an extension package of Kivy framework. MD stands for Material Design, and it has various widgets that helps the coder to create a beautiful interface application. Lack of ready to use components for creating a nice GUI was known con of Kivy, and since KivyMD covers this con, we will be using KivyMD rather than Kivy. As mentioned previously, the KivyMD has a strong compatibility with Python. This is another justification for using the KivyMD language for the GUI creation.

#### SQLAlchemy
SQL language is a specific language used for controlling database. It stands for Structured Query Language. And SQLAlchemy is SQL toolkit and ORM(object-relational mapper) for the Python programming language. SQLAlchemy is great since it has good connection and compatibility with Pythonic languages which we will be using in this project. Additionally, the SQLAlchemy has connection to various Databases, and helps the coder for easier usage. The reasons mentioned justifies the usage of SQLAlchemy for this project in terms of database.

## Record of Tasks
| Task No. | Planned Action                             | Time Estimate | Target Complete Date | Criterion  |
|----------|--------------------------------------------|---------------|----------------------|------------|
| 1        | Define Problem through client meeting      | 30min         | Mar20                | A          |
| 2        | Discuss with the client about the solution | 30min         | Mar24                | A          |
| 3        | Application details                        | 30min         | Mar28                | A          |
| 4        | LoginScreen GUI                            | 30min         | Apr12                | C          |
| 5        | LoginScreen Function                       | 1hour         | Apr13                | C          |
| 6        | RegisterScreen GUI                         | 30min         | Apr15                | C          |
| 7        | RegisterScreen Function                    | 2hours        | Apr15                | C          |
| 8        | HomeScreen GUI                             | 10min         | Apr15                | C          |
| 9        | HomeScreen Function                        | 10min         | Apr15                | C          |
| 10       | ListScreen GUI                             | 1.5hours      | Apr21                | C          |
| 11       | ListScreen Function                        | 2hours        | Apr21                | C          |
| 12       | SummativeScreen GUI                        | 2hours        | Apr22                | C          |
| 13       | SummativeScreen Function                   | 3hours        | Apr22                | C          |
| 14       | Diagrams                                   | 2hours        | Apr22                | B          |
| 15       | Functionality Video                        | 10min         | Apr22                | D          |
| 16       | Evaluation                                 | 20min         | Apr22                | E          |
# Criteria B: Design

## System Diagram
![](System_Diagram.png)

## Flow Diagrams
### Flow Diagram 1.
### Flow diagram for Register Screen 
<img src="https://github.com/K04-Matsu/Unit-3/blob/main/Image/FD1.png">

### Flow Digram 2.
### Flow diagram for Login Screen 
<img src="https://github.com/K04-Matsu/Unit-3/blob/main/Image/FD2.png">

### Flow Diagram 3.
### FLow diagram for the summative adding function
<img src="https://github.com/K04-Matsu/Unit-3/blob/main/Image/FD3.png">

### ER Diagram
<img src="https://github.com/K04-Matsu/Unit-3/blob/main/Image/ER.png">

### System Diagram
<img src="https://github.com/K04-Matsu/Unit-3/blob/main/Image/SD.png">

### Wire Frame Diagram
<img src="https://github.com/K04-Matsu/Unit-3/blob/main/Image/WF.png">


## Test plans

| Test Name:                | Test matter:                                                                              | Test type:  | Output:                                                                        |
|---------------------------|-------------------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------|
| Login System              | Checking if the login system is functioning correctly or not.                             | Module Test | The login system works without any bugs or crashes and is ready to be used.    |
| Register System           | Checking if the register system is functioning correctly or not.                          | Module Test | The register system works without any bugs or crashes and is ready to be used. |
| List Screen               | Seeing if the list screen has all the summative with the name of subject and deadline.    | Module Test | The list screen has all the components needed and is fully functional.         |
| Summative adding function | Can the summative added through summative page.                                           | Module Test | The summative can be added from summative page.                                |
| Calendar Interface        | When adding the summative, is the calendar interface functioning in terms of adding date. | Module Test | The calendar style interface is working for adding the date for summative.     |
| Run-through               | Run-through the whole code to see if the product can function without major crashes       | System Test | The product can run-through without any major crashes and is ready to be used. |

## Criteria C: Code

## Criteria D: Functionality 

## Criteria E: Evaluation
Parts that went well: the product worked, and the client was satisfied with it. The success criteria's were met and overall the performance of the product was decent. In addition, association of Python, KivyMD and SQLAlchemy worked effectively and also efficiently. However, the parts that did not go well: everything was very last minute, and the lack of time management was very obvious leading to impatient coding and loss of quality in terms functionality and visuals. Although time was provided, I myself pretty much spoiled the time scheduling and made a mess. From this, one of the criteria "Password Encrypt" was not met. This directly leads to the level of security and we can say that it is a major problem. Concludingly, the biggest issue in this project was time management, and which should is a problem that needs an immediate fix to it.


