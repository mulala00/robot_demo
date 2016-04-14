*** Settings ***
Documentation     Main level test suite for This Demo
Suite Setup       Initialize Test Environment
Suite Teardown    Clean-up Test Environment
Library           OperatingSystem
Library           Process


*** Variables ***
${remote server process name}     LocalServer



*** Keywords ***
Initialize Test Environment
    [Documentation]    Initializes ADSP blade for the tests.
    Clean-up Local Results
    Start Robot Remote Server

Clean-up Test Environment
    Stop Robot Remote Server

Start Robot Remote Server
    [Tags]  Remote
    Start Process   python  ${EXECDIR}/libraries/remote_server_demo.py    alias=${remote server process name}

Stop Robot Remote Server
    [Tags]  Remote
    Terminate Process   ${remote server process name}
    ${result}=     Get Process Result  ${remote server process name}
    Log  ${result.rc}
    Log  ${result.stdout}
    Log  ${result.stderr}


Clean-up Local Results
    [Documentation]    Removes temporary files and folders on local host from the previous run.
    OperatingSystem.Run    find ${EXECDIR} -name "*.pyc" -exec rm -rf {} \\;
#    OperatingSystem.Remove Directory   ${OUTPUTDIR}   recursive=${TRUE}
