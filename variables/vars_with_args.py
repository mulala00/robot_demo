"""Variables example from a .py """

BLADE_VARS = {
    'buck':     {'TEST_HW':              'adsp1',
                 'PRODUCT':              'ui50',
                 'TEST_SLOT_ID':         4,
                 'CLA_IP_ADDRESS':       '10.69.10.88'},
    'westlake': {'TEST_HW':              'adsp1',
                 'PRODUCT':              'ui50',
                 'TEST_SLOT_ID':         4,
                 'CLA_IP_ADDRESS':       '10.69.10.212'},
    'koff':     {'TEST_HW':              'adsp1',
                 'PRODUCT':              'ui50',
                 'TEST_SLOT_ID':         4,
                 'CLA_IP_ADDRESS':       '10.69.55.5'},
    'hulk':     {'TEST_HW':              'adsp2',
                 'PRODUCT':              'ui60',
                 'TEST_SLOT_ID':         4,
                 'CLA_IP_ADDRESS':       '10.69.115.108'}
}


def get_variables(test_hw):
    return BLADE_VARS[test_hw]
