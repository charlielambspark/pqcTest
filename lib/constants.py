DEV_PQC_URL = 'https://dev-pre-qualification-check-api.clover-technology.co.uk:6443/'
STAGING_PQC_URL = 'https://dev-staging-pre-qualification-check-api.clover-technology.co.uk:6443/'
OPPORTUNITY_NUMBER = '223'
USER_ID = '1000877'

TYPES_AND_SUBTYPES = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4],
                      [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]
TYPE_DESCRIPTIONS = {1: 'Associated Business', 2: 'Business', 3: 'Director', 4: 'Psc', 5: 'Financials'}
SUBTYPE_DESCRIPTIONS = {
    1: {
        1: 'Associated Business Insolvency',
        2: 'HM Court Data',
        3: 'Charges on other businesses',
    },
    2: {
        1: 'CCJ (Business)',
        2: 'Director resignations',
        3: 'Accounts Overdue',
        4: 'Incorporation Date',
        5: 'Adverse SIC Code',
    },
    3: {
        1: 'Director bankruptcy',
        2: 'Director disqualifications',
        3: 'Director country of residence',
        4: 'Director nationality',
        5: 'Director average age',
        6: 'Director Personal Insolvency',
    },
    4: {
        1: 'UBO nationality',
        2: 'UBO is overseas company?',
        3: 'Recent ownership changes',
    },
    5: {
        1: 'Negative Audit report',
        2: 'Negative Balance Sheet',
        3: 'Estimated Losses',
        4: 'Substantial Debts',
    }
}
