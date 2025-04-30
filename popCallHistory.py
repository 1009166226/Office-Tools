# pyinstaller -F -w popCallHistory.py -n popCallHistory
# pyside6-uic callHistory.ui -o UI_callHistory.py
import sys, os
from datetime import date, timedelta, datetime
import pytz
from PySide6.QtWidgets import  QLabel,QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from UI_callHistory import Ui_MainWindow
import requests
import json

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.auths = self.getAuth()
        # self.phone = sys.argv[1]
        self.phone = 9296394227
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        # 通话历史输出
        self.historyTable = self.ui.HistoryTable
        self.getHistory()

        # policy输出
        self.policyTable = self.ui.PolicyTable
        self.getPolicy()


    def getPolicy(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'Cookie': 'SPIDERAUTH=' + self.auths['AMSauth']
        }
        data = {
            "SearchText": str(self.phone),
            "MaximumRecords": 100,
            "SearchBy": "M",
            "SearchByMoreSelection": "Phone #",
            "x-SearchByMoreSelection": "Phone #",
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

        x = requests.post('https://www.ams360.com/v2414571/NextGen/Customer/GetGridData', headers=header, data=data)
        # print(x.text)
        policy_list = json.loads(x.text)['CustomerList']
        # print(policy_list)
        policies = []
        for policy in policy_list:
            policies.append((policy['CustNo'],policy['Name'],"https://www.ams360.com/v2414571/NextGen/Customer/Detail/" + policy['CustId']))

        self.policyTable.setRowCount(len(policies))
        for i, (a, n, p) in enumerate(policies):
            # policy account number
            item_a = QTableWidgetItem(str(a))
            item_a.setFlags(item_a.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.policyTable.setItem(i, 0, item_a)

            # Policy Name (as normal item)
            item_n = QTableWidgetItem(n)
            item_n.setFlags(item_n.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.policyTable.setItem(i, 1, item_n)

            # Policy URL (as clickable QLabel)
            label = QLabel()
            label.setText(f'<a href="{p}">{p}</a>')  # Use HTML anchor tag
            label.setOpenExternalLinks(True)  # Enable automatic link opening
            self.policyTable.setCellWidget(i, 2, label)  # Set as cell widget

    def getHistory(self):
        displayHistory = []
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'authorization': 'Bearer ' + self.auths['BridgeAuth'][:-1]
        }
        # print(self.auths['BridgeAuth'][:-1])
        search = self.phone
        startDate = date.today() - timedelta(days=7)
        endDate = date.today() + timedelta(days=1)

        requestURL = f'https://blue.api4.bridge.insure/call-history/agency?from-date={startDate}T04%3A00%3A00.000Z&to-date={endDate}T03%3A59%3A59.999Z&per-page=40&page=1&order-by-direction=desc&order-by=stamp&search={search}&missed=&domain-uuid=e25cddc7-bb6a-302a-afb2-67ffa1019add'

        response = requests.get(requestURL,headers=header)
        print(response.text)
        history = json.loads(response.text)['data']
        print(len(history))
        if history:
            for key,value in history.items():
                data = list(value.values())[0]
                f = ''
                t = ''
                if "from_name" in data.keys():
                    f = data["from_name"]
                else:
                    f = data["from"]

                if "to_name" in data.keys():
                    t = data["to_name"]
                else:
                    t = data['to']

                date_time = data["created_at"]
                # Parse the input as UTC datetime
                utc_dt = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)

                # Convert to Eastern Time using pytz
                local_dt = utc_dt.astimezone(pytz.timezone("America/New_York"))

                # Format the datetime
                formatted_date = f"{local_dt.month}/{local_dt.day:02d}/{local_dt.year}"
                hour = 12 if (local_dt.hour % 12) == 0 else (local_dt.hour % 12)
                formatted_time = f"{hour}:{local_dt:%M:%S} {local_dt:%p}".lower()

                formatted = f"{formatted_date} {formatted_time}"
                displayHistory.append((f,t,formatted))

        self.historyTable.setRowCount(len(displayHistory))

        for i, (f, t, day_time) in enumerate(displayHistory):
            item_f = QTableWidgetItem(f)
            item_f.setFlags(item_f.flags() ^ Qt.ItemFlag.ItemIsEditable)
            item_t = QTableWidgetItem(t)
            item_t.setFlags(item_t.flags() ^ Qt.ItemFlag.ItemIsEditable)
            item_time = QTableWidgetItem(day_time)
            item_time.setFlags(item_time.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.historyTable.setItem(i, 0, item_f)
            self.historyTable.setItem(i, 1, item_t)
            self.historyTable.setItem(i, 2, item_time)


    def getAuth(self):
        # print(BASE_DIR)
        auths = {}
        with open(BASE_DIR+"\Auth.txt",'r') as f:
            for a in f:
                auth = a.split('=')
                auths[auth[0]] = auth[1]
        # print(auths)
        return auths


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())