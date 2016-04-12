*** Settings ***
Documentation     This is an axample how to crreate keywords


*** Keywords ***
Keywords For ${name} as Example
    [Documentation] This is an axample for embedding args in keyword
        Log ${name}

Exmaple To Using Keywords With Embedding Args
    Keywords For Leiws as Example
    Keywords For Mulala as Example
    Given Exmaple To Using Keywords With Embedding Args