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
### Kivy File
```.py
ScreenManager:
    id: screen_manager

    LoginScreen:
        name: "LoginScreen"

    HomeScreen:
        name: "HomeScreen"

    RegisterScreen:
        name: "RegisterScreen"

    ListScreen:
        name: "ListScreen"

    SummativeScreen:
        name: "SummativeScreen"


<LoginScreen>
    MDBoxLayout:
        size_hint: 1.0, 1.0
        orientation: "vertical"
        spacing: 20

        MDLabel:
            text: "Summative Tracker"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.3}

        MDLabel:
            id: login_label
            text: "Login"
            halign: "center"
            pos_hint: {"center_y": 0.9}

        MDTextField:
            id: email
            hint_text: "email"
            halign: "center"
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: password
            hint_text: "password"
            halign: "center"
            pos_hint: {"center_x": 0.5}
            password: True

        MDRaisedButton:
            text: "Log in"
            hint_text: "email"
            halign: "center"
            pos_hint: {"center_x": 0.5}
            on_release:
                root.login_user()

        MDRaisedButton:
            text: "Register"
            hint_text: "Register"
            halign: "center"
            pos_hint: {"center_x": 0.5}
            on_release:
                root.register()

        MDLabel:


<RegisterScreen>
    MDBoxLayout:
        size_hint: 0.3,0.3
        orientation: "vertical"
        pos_hint: {"center_y":0.5}
        spacing: 20

        MDLabel:
            id: register_label
            text: "Register"
        MDTextField
            id: new_user
            hint_text: "Username"
        MDTextField
            id: new_email
            hint_text: "Email"
        MDTextField
            id: new_password
            hint_text: "Password"
            password: True
        MDRaisedButton
            text: "Register"
            on_release:
                root.try_register()


<HomeScreen>
    MDBoxLayout:

    MDLabel:
        text: "Welcome to Summative Tracker!"
    MDRaisedButton:
        text: "Add Summative"
        on_release:
            root.summative()
    MDRaisedButton:
        text: "List of Summative"
        on_release:
            root.list()



<ListScreen>
    ScrollView:
        MDCard:
            size_hint: 1, 0.1
            elevation: 0
            padding: 30
            pos_hint: {"center_x": 0.5, "top": 0.8}
            orientation: "horizontal"

            MDCard:

                MDIconButton:
                    icon: "account-details"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.1, "top": 0.6}
                    on_press:
                        root.print_data()

            GridLayout:
                id: container
                cols: 2
                padding: 50
                spacing: 30
                row_default_height: 60
                row_force_default: True
                pos_hint_y: 0
                MDLabel:
                    id: col1
                    text: "Subject"
                    halign: "center"
                MDLabel:
                    id: col2
                    text: "Deadline"
                    halign: "center"


<SummativeScreen>:
    BoxLayout:
        orientation: 'vertical'
        size: root.height, root.width

    MDCard:
        size_hint: 0.5, 0.70
        elevation: 10
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        orientation: "vertical"

        MDBoxLayout:
            id: content
            orientation: "vertical"
            padding: dp(30)
            spacing: dp(20)

            MDIconButton:
                icon: "keyboard-backspace"
                on_press:
                    root.parent.current = "ListScreen"

            MDLabel:
                text: "New Assignment"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                halign: "center"

            MDTextField:
                id: subject_name
                hint_text: "Subject Name"

            MDBoxLayout:
                orientation: "horizontal"
                spacing: dp(20)

                MDRectangleFlatIconButton:
                    icon: 'calendar'
                    text: "Select the due date"
                    pos_hint: {'center_x': .15, 'center_y': .5}
                    on_release: root.date_picker()

                MDLabel:
                    id: chosen_date
                    pos_hint: {'center_x': .25, 'center_y': .5}

            MDRaisedButton:
                text: "CREATE"
                padding: dp(50)
                on_release:
                    root.add_summative()

            MDLabel:
```

### Python File
```.py
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
# import from the SQLAlchemy the function to connect to db
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, desc
# also the function to create a session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)


class Summative(Base):
    __tablename__ = "summative"
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    deadline = Column(Date)
    users_id = Column(Integer, ForeignKey("users.id"))


db_engine = create_engine("sqlite:///database.db", echo=False)
Base.metadata.create_all(db_engine)
Base.metadata.bind = db_engine
db_session = sessionmaker(bind=db_engine)
session = db_session()
Window.size = (700, 500)


class HomeScreen(MDScreen):
    def summative(self):
        self.parent.current = "SummativeScreen"

    def list(self):
        print("Hello")
        self.parent.current = "ListScreen"


class LoginScreen(MDScreen):
    def login_user(self):
        email = self.ids.email.text
        password = self.ids.password.text
        check = session.query(User).filter_by(email=email).one_or_none()
        if check:
            self.parent.current = "HomeScreen"
            LoginScreen.current_user_id = check.id

    def register(self):
        print(self.parent)
        self.parent.current = "RegisterScreen"


class RegisterScreen(MDScreen):
    def try_register(self):
        input_user = self.ids.new_user.text
        input_email = self.ids.new_email.text
        input_password = self.ids.new_password.text
        u = User(username=input_user, email=input_email, password=input_password)
        session.add(u)
        session.commit()
        self.parent.current = "LoginScreen"


class SummativeScreen(MDScreen):
    current = None
    subject_name = None

    def on_save(self, instance, value,  date_range):
        title = "Selected: "
        out_date = title + str(value)
        self.ids.chosen_date.text = out_date
        SummativeScreen.current = value

    def on_cancel(self, instance, value):
        print("Canceled")

    def date_picker(self):
        date = MDDatePicker()
        date.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date.open()

    # ---
    def add_summative(self):
        session.close()
        subject_name = self.ids.subject_name.text
        current = SummativeScreen.current

        SummativeScreen.current = current
        SummativeScreen.subject_name = subject_name

        summative = Summative(
            subject=subject_name,
            deadline=current,
            users_id=LoginScreen.current_user_id)

        session.add(summative)
        session.commit()
        self.parent.current = "HomeScreen"


class ListScreen(MDScreen):

    def print_data(self):
        self.ids.container.clear_widgets()
        summative = session.query(Summative). \
            filter_by(users_id=LoginScreen.current_user_id).all()

        subject = MDLabel(text="Subject")
        self.ids.container.add_widget(subject)
        deadline = MDLabel(text="Deadline")
        self.ids.container.add_widget(deadline)

        for data in summative:
            subject_name = MDLabel(text=str(data.subject))
            self.ids.container.add_widget(subject_name)
            duedate = MDLabel(text=str(data.deadline))
            self.ids.container.add_widget(duedate)


class login(MDApp):
    def build(self):
        return


m = login()
m.run()
```

## Criteria D: Functionality 
https://drive.google.com/drive/search?q=videoleap

## Criteria E: Evaluation
Parts that went well: the product worked, and the client was satisfied with it. The success criteria's were met and overall the performance of the product was decent. In addition, association of Python, KivyMD and SQLAlchemy worked effectively and also efficiently. However, the parts that did not go well: everything was very last minute, and the lack of time management was very obvious leading to impatient coding and loss of quality in terms functionality and visuals. Although time was provided, I myself pretty much spoiled the time scheduling and made a mess. From this, one of the criteria "Password Encrypt" was not met. This directly leads to the level of security and we can say that it is a major problem. Concludingly, the biggest issue in this project was time management, and which should is a problem that needs an immediate fix to it.


