*** Settings ***
Documentation          This demo is about How to Using Variable In Robot and Python Libraries
Default Tags           Variables  Done
Variables              common_vars.py
Variables              vars_with_args.py  hzling09
Library                FunctionLibDemo


*** Variables ***
${SACLAR VAR EXAMPLE}        I am a saclar
@{LIST VAR EXAMPLE}          127.0.0.1    8270
&{DICT VAR EXAMPLE}          user=root    password=root

${I am string 80}   80
${I am integer 80}  ${80}


*** Test Cases ***
Learn About The Variable Types In Robot
    [Documentation]  Here We Try to figure out how variable works in Robot
    Log  ${SACLAR VAR EXAMPLE}
    Log Many  @{LIST VAR EXAMPLE}
    Log Many  &{DICT VAR EXAMPLE}
    Log In Python   ${SACLAR VAR EXAMPLE}   @{LIST VAR EXAMPLE}   &{DICT VAR EXAMPLE}

Learn About The How To Define An Integer In Robot
    [Documentation]  Learn About The How To Define An Integer In Robot
    Log  ${I am string 80}
    Log  ${I am integer 80}
    Log In Python    ${I am string 80}   ${I am integer 80}

Learn About Variables From A Common Variable Files
    [Documentation]  We can using variables from python file by import them like:
    ...              Variables  common_vars.py
    ...              All The attribute that not start with '_' will be import and
    ...              They are exaclty what they defined both in python and robot
    Log  ${USER NAME}
    Log Many  @{REMOTE HOST}
    Log Many  &{DICT DEMO}
    Log In Python  ${USER}  ${PASSWORD}  @{REMOTE_HOST}  &{DICT_DEMO}
    Run Keyword And Expect Error  *   Log  ${_I_AM_NOT_EXIST}

Learn About Variables From Variable Files With Arguments
    [Documentation]  We can using variables from python file with Arguments:
    ...              Variables  vars_with_args.py  hzling09
    Log  ${HOST}
    Log  ${USER}
    Log  ${PASSWORD}
    Log In Python  ${HOST}  ${USER}  ${PASSWORD}  @{REMOTE_HOST}