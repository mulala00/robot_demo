*** Settings ***
Documentation          This demo is about how to Extend Lib Using
...                    Life easy
# This is same as : Library                MyStaticLib.MyStaticLib   Mulala
Library                MyStaticLib   Mulala
Library                MyStaticLib.IHaveToUsingExplict   Leiws
Library                MyFunctionsLib

*** Variables ***



*** Test Cases ***
Using Keywords From Static Lib APIs
    MyStaticLib.Static_Api
    log  ${TEST NAME}

Using Keywords From Static Lib APIs Again
    MyStaticLib.Static_Api
    log  ${TEST NAME}

Using Keywords From That Have Another Name Lib APIs
    MyStaticLib.IHaveToUsingExplict.Static_Api
    log  ${TEST NAME}

Using Function Keywords From Lib APIs
    Function Keyword   Hello world
    log  ${TEST NAME}