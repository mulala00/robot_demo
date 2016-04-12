*** Settings ***
Documentation     Default test fixtures. Implements the default suite/test setup and teardown keywords.
Library           OperatingSystem
Library           RemoteShell


*** Variables ***
${LOG DIR}        ${OUTPUT DIR}/logs
${NAME}         Robot Framework
${VERSION}      2.0
${ROBOT}        ${NAME} ${VERSION}
@{NAMES}        Matti       Teppo
@{NAMES2}       @{NAMES}    Seppo
@{NOTHING}
@{MANY}         one         two      three      four
...             five        six      seven
&{DICT_USER 1}       name=Matti    address=xxx         phone=123
# Their main disadvantages are that values are always strings
# and they cannot be created dynamically.

*** Keywords ***
Initial Logs Collect
    RemoteShell.Write Syslog    Robot setup test case:${TEST NAME}

Collect Target Syslog
    [Arguments]    ${destination directory}
    RemoteShell.Collect Syslog    ${destination directory}/syslog.txt
    Run Keyword And Ignore Error    OperatingSystem.Move File    ${syslog file}    ${destination directory}
    OperatingSystem.Remove File    ${syslog file}

Collect Logs When Tear Down
    [Arguments]     ${extra log files}=${None}
    [Documentation]    This Keyswords can only be used when teardown
    RemoteShell.Write Syslog    Robot teardown test case:${TEST NAME}
    ${destination directory} =    OperatingSystem.Join Path    ${LOG DIR}    ${SUITE NAME}.${TEST NAME}
    Create Directory    ${destination directory}
    RemoteShell.Collect Syslog    ${destination directory}/syslog.txt
    Run Keyword And Ignore Error    Run Keyword If    ${extra log files}    OperatingSystem.Move Files    @{extra log files}    ${destination directory}

