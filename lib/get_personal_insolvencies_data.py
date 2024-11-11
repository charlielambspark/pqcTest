from typing import List

import requests

from lib.constants import DEV_PQC_URL, OPPORTUNITY_NUMBER, USER_ID


def get_personal_insolvencies_data(company_numbers: List[str]):
    flagged_company_company_numbers = []
    for i, company_number in enumerate(company_numbers):
        if i % 10 == 0:
            print("Processing company number", i + 1, "of", len(company_numbers))
        response = requests.get(f"{DEV_PQC_URL}Pqc/0{company_number}/{OPPORTUNITY_NUMBER}/{USER_ID}")
        try:
            json = response.json()
            if get_pqc_personal_insolvency_company_numbers(json):
                flagged_company_company_numbers.append([company_number])
        except ValueError:
            print("Error processing company number", company_number)
    return flagged_company_company_numbers


def get_pqc_personal_insolvency_company_numbers(json):
    return any(insolvency['case_type'] == 2 for insolvency in json['pqc_data']['kpc_data']['personal_insolvencies'])
