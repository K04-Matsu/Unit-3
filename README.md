# Unit-3: New Project 
![](game.gif)

# Criteria A: Planning

## Context and Solution
Reiji Nishikawa, student at UWC ISAK Japan who takes the IB program is needing a programmer who can code a program that tracks his summative assignments. The summative tracker must include the 6 success criterias listed below. Regarding this, I will be creating a product that meets all the requirements.
The solution product will be made with PyCharm, and will be coded with the Python3.7 associated with KivyMD and SQLAlchemy. This KivyMD differs from normal Kivy. KivyMD, which is shortened for Kivy Material Design is a package Kivy design widgets. SQL is a library configuration language, and this time we will be using specifically SQLAlchemy. Pros and justification of used languages will be explained below. The program will start off from an title screen with email text box, password text box, login button and register button. The login button will simply login the user if correct email and password is entered, leading to the home screen. The register button will move the screen to register screen where the user can input their username, email and password. In the home screen, the list of entered summative will be shown. Below list, there will be a button which leads to the summative adding page. User will be required to put subject name and teacher name along with the due date information. The due date can be selected through the calendar interface which will pop when "Add Date" button is pressed. When the summative is added, it will be added to both list screen and database. This is the overall look of this project solution. The name of this product is the "Summative Tracker."

## Success Criteria
### 1. Register and Login system.
### 2. Minimalist design.
### 3. Calendar style interface to add the assignments.
### 4. Screen with the list of all recorded assignments.
### 5. Assignments should have subject, teacher and date label.
### 6. The password should be encrypted.

### Justification

#### Python
The Python 3.7 is a widely-known language for its easy usage and simple syntax. And since the language is vastly recognised, there are countless materials and community websites to support the programmer. In addition to this, Python has flexibility and big database which gives versatility, efficiency, reliability, and speed to the language. Another factor is the compatibility with KivyMD and SQLAlchemy, which are both essential languages to create an application. Lastly, Python is the only main language I have learned so far in this IB academic course, and I am most comfortable with it. This experience will directly connect to the overall performance of the product, and considering this, I will be using Python.

#### KivyMD
The KivyMD is an extension package of Kivy framework. MD stands for Material Design, and it has various widgets that helps the coder to create a beautiful interface application. Lack of ready to use components for creating a nice GUI was known con of Kivy, and since KivyMD covers this con, we will be using KivyMD rather than Kivy. As mentioned previously, the KivyMD has a strong compatibility with Python. This is another justification for using the KivyMD language for the GUI creation.

#### SQLAlchemy
SQL language is a specific language used for controlling database. It stands for Structured Query Language. And SQLAlchemy is SQL toolkit and ORM(object-relational mapper) for the Python programming language. SQLAlchemy is great since it has good connection and compatibility with Pythonic languages which we will be using in this project. Additionally, the SQLAlchemy has connection to various Databases, and helps the coder for easier usage. The reasons mentioned justifies the usage of SQLAlchemy for this project in terms of database.

# Criteria B: Design

## System Diagram
![](System_Diagram.png)

## Flow Diagrams
### FD1


![](Diagram1.png)

### FD2
![](Diagram2.png)

### FD3
![](Diagram3.png)

## Record of Tasks
| Task No | Planned Action                          | Planned Outcome                                                                                                                          | Time estimate | Target completion date | Criterion |   |   |
|---------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|---|---|
| 01      | Time and Score for the game             | A system to measure the time and score the user took.                                                                                    | 10min         | 2021.Sep.23            | C         |   |   |
| 02      | Recording database for Game             | Database for the user's name, time to finish the game, and the score.                                                                    | 10min         | 2021.Sep.25            | C         |   |   |
| 03      | Unit Test: Caesar Cypher Encoding       | To check the function works as expected. Test with the input of "Hello" with code of 3, the outcome becomes "Khoor".                     | 10min         | 2021.Sep.26            | C         |   |   |
| 04      | Construction of big picture of the game | Timeline and outline of the whole game for more efficient progress.                                                                      | 2hours        | 2021.Sep.28            | A         |   |   |
| 05      | Side character death function           | Function that kills the side character in story.                                                                                         | 20min         | 2021.Sep.28            | C         |   |   |
| 06      | Underplot for the TRUE END              | Path to secret true ending: Upon specific input from the user at the first decision.                                                     | 1hour         | 2021.Sep.29            | C         |   |   |
| 07      | While statement true loop               | While the main character is in certain room, the while loop will happen and show choices accordingly                                     | 1week         | 2021.Oct.29            | C         |   |   |
| 08      | Inventory system                        | Inventory system to save items, which will be needed later on the game.                                                                  | 1day          | 2021.Oct.6             | C         |   |   |
| 09      | Text file                               | Save all the long paragraphs that appears during the game. Putting in different file and making it a function for easier access and use. | 10min         | 2021.Oct.6             | C         |   |   |
| 10      | Play sound                              | Sound playing system using afplay. Used for sound effect in the game.                                                                    | 2hours        | 2021.Oct.7             | C         |   |   |
| 11      | MVP                                     | Create a minimum viable product for seniors to play and receive feedback from them for further improvements.                             | 2weeks        | 2021.Oct.8             | C         |   |   |
| 12      | Checkpoint                              | Create a checkpoint lists for saving players process every chapter. (On every ending of chapter, "Chapter N" Will be added)              | 2hours        | 2021.Oct.14            | C         |   |   |
| 13      | Saving system                           | A saving system that saves username, item and progress(checkpoint list) into gamesave.txt.                                               | 30min         | 2021.Oct.18            | C         |   |   |
| 14      | Loading system                          | A loading system that loads the saved variables from gamesave.txt.                                                                       | 30min         | 2021.Oct.18            | C         |   |   |
| 15      | Confirmation for success criteria       | Check if the whole game meets the success criteria.                                                                                      | 2hours        | 2021.Oct.22            | C         |   |   |
| 16      | Flow diagrams                           | Draw flow diagrams for While statement true loop, Saving system and Loading system.                                                      | 1hour         | 2021.Oct.23            | B         |   |   |


## Test plans

| Description                                                   | Type             | Input                                                                                    | Expected Output                                                                                                |
|---------------------------------------------------------------|------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Caesar Cypher Encoding Program for Usernames                  | Module Test      | "Hello"                                                                                  | "Khoor"                                                                                                        |
| Database for [Username], [Time taken to finish game], [Score] | Module Test      | Player named "Matsu" finished the game with 200seconds.                                  | Appends {["Matsu"], [200.21], [3400]} into database file                                                       |
| Function [RYU_D] (Side character death function)              | Module Test      | Player makes specific decisions after entering the door without [Fallen] Statement False | Print("Ryu DIED"), make ryu_dead statement and fallen statement True                                           |
| Function [ROUTE3] (True ending function)                      | Module Test      | Player makes specific decision before opening the door                                   | Print("Ryu found a teddy bear"), append [Bear] into inventory, make fallen statement True                      |
| Sound playing module                                          | Module Test      | After event                                                                              | Play sound from selected mp3 file.                                                                             |
| Inventory lists                                               | Module Test      | Player finds append-able item                                                            | Append selected items into [Inventory] lists                                                                   |
| Room statement true                                           | Module Test      | When player enters room                                                                  | Make entered Room statement True, and previous room sstatement False                                           |
| While statement True loop'                                    | Module Test      | When room statement True                                                                 | Print(Room details) + input(player decisions).                                                                 |
| Run Chapter1                                                  | Integration Test | Run through chapter1 with various inputs on all decisions                                | No bugs, function effectively used, compatibility in global statements.                                        |
| Run Chapter2                                                  | Integration Test | Run through chapter2 with various inputs on all decisions                                | No bugs, function effectively used, compatibility in global statements, quizes working.                        |
| Run Chapter3                                                  | Integration Test | Run through chapter3 with various inputs on all decisions                                | No bugs, function effectively used, compatibility in global statements, quizes working.                        |
| Run Ember                                                     | System Test      | Run through the whole game for all endings.                                              | No bugs, function effectively used, compatibility in global statements, quizes working, all endings reachable. |
| Satisfaction checker                                          | Module Test      | Player inputs satisfactory level from the scale of 1 to 5.                               | If validable input, append to Satisfactory.txt, if invalid input, repeat question.                             |

## Criteria C: Code

## Criteria D: 

## Criteria E:

