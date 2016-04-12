"""
Dynamic libraries are classes that implement a method to get the names of the keywords they implement,
and another method to execute a named keyword with given arguments.
The names of the keywords to implement, as well as how they are executed, can be determined dynamically at runtime,
but reporting the status, logging and returning values is done similarly as in the static API.
"""

def function_keyword(arg):
    print "I am a simple keyword:", arg