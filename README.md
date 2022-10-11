# oop_with_python
Master OOP by Building Games and GUIs.  This repository is about a software development technique called 
object-oriented programming (OOP) and how it can be used with Python.

Chapter 1. PROCEDURAL PYTHON EXAMPLES
========================================================================================================================

Higher or Lower Card Game
My first example is a simple card game called Higher or Lower. In this
game, eight cards are randomly chosen from a deck. The first card is shown
face up. The game asks the player to predict whether the next card in the
selection will have a higher or lower value than the currently showing card.
For example, say the card that’s shown is a 3. The player chooses “higher,”
and the next card is shown. If that card has a higher value, the player is
correct. In this example, if the player had chosen “lower,” they would have
been incorrect.
If the player guesses correctly, they get 20 points. If they choose
incorrectly, they lose 15 points. If the next card to be turned over has the
same value as theHigherOrLowerProcedural.py previous card, the player is incorrect.
Code: HigherOrLowerProcedural.py

Bank Account Simulations
In this second example of procedural coding, I’ll present a number of
variations of a program that simulates running a bank. In each new version
of the program, I’ll add more functionality. Note that these programs are not
production-ready; invalid user entries or misuse will lead to errors. The
intent is to have you focus on how the code interacts with the data
associated with one or more bank accounts.
To start, consider what operations a client would want to do with a bank
account and what data would be needed to represent an account.
    Code: Bank1_OneAccount.py
Implementation 2—Single Account with Functions
In the version of the program, the code is broken up into
separate functions, one for each action. Again, this simulation is for a single
account.
    Code: Bank2_OneAccountWithFunctions
The version of the bank simulation program  uses the same approach but adds the ability to have two accounts.
    Code: Bank3_TwoAccounts.py
Implementation 4—Multiple Accounts Using Lists
To more easily accommodate multiple accounts, I’ll represent
the data using lists. I’ll use three parallel lists in this version of the program:
accountNamesList , accountPasswordsList , and accountBalancesList .
Implementation 4—Multiple Accounts Using Lists
To more easily accommodate multiple accounts, in Listing 1-5 I’ll represent
the data using lists. I’ll use three parallel lists in this version of the program
     Code: Bank4_N_Accounts.py
Implementation 5—List of Account Dictionaries
To implement this last approach, I’ll use a slightly more complicated data
structure. In this version, I’ll create a list of accounts, where each account
(each element of this list) is a dictionary
     Code: Bank5_Dictionary.py

Object-Oriented Solution—First Look at a Class
Listing 1-7 is an object-oriented approach that combines all the code and
associated data of a single account. There are many new concepts here, and
I will get into all the details starting in the next chapter. While I am not
expecting you to fully understand this example yet, notice that there is a
combination of code and data in a single script (called a class). Here is your
first look at object-oriented code.
    Code: Account.py

CHAPTER 2: MODELING PHYSICAL OBJECTS WITH OBJECT-ORIENTED PROGRAMMING
========================================================================================================================

State and Behavior: Light Switch Example
Software model of a standard two-position light switch
written in procedural Python. This is a trivial example, but it will
demonstrate state and behavior.
     Code: LightSwitch_Procedural.py
Calling Methods of an Object
Listing contains the LightSwitch class, code to instantiate an object
from the class, and code to turn that LightSwitch object on and off by
calling its turnOn() and turnOff() methods.
    File: OO_LightSwitch_with_Test_Code.py
Creating Multiple Instances from the Same Class
Listing creates two light switch objects and calls
methods on the different objects.
    File: OO_LightSwitch_Two_Instances.py
Building a Slightly More Complicated Class
The DimmerSwitch class uses the standard template shown earlier
: it starts with a class statement and a first method named
__init__() , then defines a number of additional methods, one for each of
the behaviors listed.
    File: DimmerSwitch.py
    File: OO_DimmerSwitch_with_Test_Code.py
Representing a More Complicated Physical
Object as a Class
Let’s consider a more complicated physical object: a television. With this
more complicated example, we’ll take a closer look at how arguments work
in classes.
    File: TV.py
    File: OO_TV_with_Test_Code.py
