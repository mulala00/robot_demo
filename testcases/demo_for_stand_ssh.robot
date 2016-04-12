*** Settings ***
Documentation          This example demonstrates using SSHLibrary to executing commands on a remote machine,
...                    getting their output and the return code.
...
...                    Notice how connections are handled as part of the suite setup and
...                    teardown. This saves some time when executing several test cases.
Default Tags           StardardLib
Library                SSHLibrary
Suite Setup            Open Connection And Log In
Suite Teardown         Close All Connections


*** Variables ***
${HOST}                10.69.10.88
${USERNAME}            root
${PASSWORD}            root

*** Test Cases ***
Execute Command And Verify Output
    [Documentation]    Execute Command can be used to ran commands on the remote machine.
    ...                The keyword returns the standard output by default.
    ${output}=    Execute Command    echo Hello SSHLibrary!
    Should Be Equal    ${output}    Hello SSHLibrary!

    Switch Connection   1
    ${output}=    Execute Command    echo Hello SSHLibrary!
    Should Be Equal    ${output}    Hello SSHLibrary!

Execute Command And Verify Return Code
    [Documentation]    Often getting the return code of the command is enough.
    ...                This behaviour can be adjusted as Execute Command arguments.
    ${rc}=    Execute Command    echo Success guaranteed.    return_stdout=False    return_rc=True
    Should Be Equal    ${rc}    ${0}

Executing Commands In An Interactive Session
    [Documentation]    Execute Command always executes the command in a new shell.
    ...                This means that changes to the environment are not persisted
    ...                between subsequent Execute Command keyword calls.
    ...                Write and Read Until variants can be used to operate in the same shell.
    Write    cd ..
    Write    echo Hello from the parent directory!
    ${output}=    Read Until    directory!
    Should End With     ${output}    Hello from the parent directory!

Check We Are In CLA-0
    [Documentation]    Check we are in CLA-0, Otherwise, means CLA-0 Down
    ${output}=    Execute Command    hostname
    Should Be Equal    ${output}    CLA-0


*** Keywords ***
Open Connection And Log In
   ${Conn}=   Open Connection    ${HOST}
   Login    ${USERNAME}    ${PASSWORD}

