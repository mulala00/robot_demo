*** Settings ***
Documentation          This demo is about how to extend the built-in libary to make your
...                    Life easy
Default Tags           ExtendLib
Library                RemoteShell
Library                MyStaticLib   Zhou
Resource               ${EXECDIR}/resources/log_resource.robot
Suite Setup            Open Connection Using My ShellLib
Suite Teardown         Close Connection Using My ShellLib
Test Setup             Initial Logs Collect
Test Teardown          Collect Logs When Tear Down

*** Variables ***
${SACLAR  VAR EXAMPLE}       I am a saclar
@{LIST VAR EXAMPLE}          127.0.0.1    8270
&{DICT VAR EXAMPLE}          user=root   password=root

*** Test Cases ***
Check We Are In CLA-0 Using My Shell Lib
    [Documentation]       Check we are in CLA-0, Otherwise, means CLA-0 Down
#    [Tags]   Lewis
    Hostname Should Be    CLA-0

DSP Should Be Enable
    [Documentation]       Check is DSP enable in has state
    Dsp Core Should Be Enable  device=${DEF_DEV}   core=${DEF_CORE}
#    Dsp Core Should Be Disable  device=${DEF_DEV}   core=${DEF_CORE}

This Demo Need Two Connection
    Dsp Core Should Be Enable  device=${DEF_DEV}   core=${DEF_CORE}

*** Keywords ***
Open Connection Using My ShellLib
    ${conn}=    Connect To Target  ${HOST}  ${USERNAME}  ${PASSWORD}

Close Connection Using My ShellLib
    ${conn}=    Disconnect To Target

Open More Conns
    ${conn}=    Connect To Target  ${HOST}  ${USERNAME}  ${PASSWORD}

Collect Logs to Output
    ${conn}=    Connect To Target  ${HOST}  ${USERNAME}  ${PASSWORD}

Collect Logs to Output When Failed
    ${conn}=    Connect To Target  ${HOST}  ${USERNAME}  ${PASSWORD}

