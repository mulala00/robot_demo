*** Settings ***
Library       MyRemote    http://${ADDRESS}:${PORT}
Library       Process
Default Tags           Remote  Done
#Suite Setup            Start Robot Remote Server
#Suite Teardown         Stop Robot Remote Server

*** Variables ***
${ADDRESS}=    127.0.0.1
${PORT}        8270

*** Test Cases ***
An Example Case Require Remote Operation
    [Documentation]   Here I just Start It In Local Host, In the real case, You can need to depoly it to remote server.
    ${result}=   Start Application On Remote
    Log   ${result}
    Log   We Do Something Else Here Like Configure And Setup Service In BTS
    Run Keyword And Ignore Error    Stop Application On Remote

An Example Using Run Keyword Method
    &{result}=   Run Keyword   Start Application On Remote
    Log Many    &{result}
    Log   We Do Something Else Here Like Configure And Setup Service In BTS
    Run Keyword And Ignore Error    Stop Application On Remote


*** Keywords ***
Start Robot Remote Server
   [Documentation]   Here I just Start It In Local Host, In the real case, You can need to depoly it to remote server.
    ...              And start it through like SSH
   Start Process   python  D:\git_project\robot_demo\libraries\remote_server_demo

Stop Robot Remote Server
   Terminate All Processes

Start Application On Remote
   Start Applicaiton Here    TM500

Stop Application On Remote
   stop_application_here    TM500