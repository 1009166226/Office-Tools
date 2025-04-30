import requests, json, os, sys

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

def getAuth():
    # print(BASE_DIR)
    auths = {}
    with open(BASE_DIR + "\Auth.txt", 'r') as f:
        for a in f:
            auth = a.split('=')
            auths[auth[0]] = auth[1]
    # print(auths)
    return auths

def getPolicyID(companyName):
    auths = getAuth()
    # print(auths)
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Cookie':'SPIDERAUTH='+auths['AMSauth']
    }
    data ={
        "SearchText": companyName,
        "MaximumRecords": 100,
        "SearchBy": "N",
        "SearchByMoreSelection": "",
        "x-SearchByMoreSelection": "",
        "IncludeAgencyCustomers": True,
        "IncludeBrokerCustomers": True,
        "CustomerStatus": "ALL",
        "IncludeCustomers": True,
        "IncludeProspects": True,
        "IncludeSuspects": True,
        "ScopeCustomer": True,
        "ScopeDBAName": True,
        "ScopeNamedInsureds": True,
        "ScopeDependents": True,
        "ScopeContacts": True,
        "ScopeClaimant": True,
        "ScopeXRef": True,
        "ScopeDriverName": True,
        "ScopeCertHolderName": True,
        "ScopeCustomerStandard": True,
        "ScopeCustomerMaster": True,
        "ScopeCustomerSub": True,
        "ScopeCustomerAccessLimit": False,
        "MatchOn": "K",
        "AutoOpenOnSingleSearchResult": True,
        "ColorInactiveForeground": "#E62838"
    }

    x = requests.post('https://www.ams360.com/v2414571/NextGen/Customer/GetGridData',headers=header,data=data)
    # print(x.text)
    policy_list = json.loads(x.text)['CustomerList']
    # print(policy_list)
    for policy in policy_list:
        if policy["Name"] == companyName:
            return policy['CustId']

def getInfo(companyName):
    auths = getAuth()
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Cookie': 'SPIDERAUTH=' + auths['AMSauth']
    }
    data = {
        "id":getPolicyID(companyName)
    }
    x = requests.post('https://www.ams360.com/v2414571/NextGen/Customer/CustomerOverview', headers=header, data=data)
    info = x.text[x.text.index("overviewList:")+len("overviewList:"):x.text.index("PageHelp")-19]
    info = json.loads(info)
    # print(info["customerOverviewInfo"])
    # print(info["customerContactInfoModelList"][0])
    # print(info["customerProfiles"][0])
    return info["customerOverviewInfo"],info["customerContactInfoModelList"][0],info["customerProfiles"]

if __name__ == '__main__':
    getInfo("JKL Trucking Inc")