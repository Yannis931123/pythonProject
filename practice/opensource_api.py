import requests

url = "http://376-cube-ship-front.product.poc.za-tech.net/deckjob/ship/openapi/v1/publishes/145/tests/scan-opensource/steps/73ce0cc2defd-3/result"

payload = {
    "message": "debug",
    "app_name": "ship-test-service-01",
    "status": "SUCCESS",
    "cve_list": [
        {
            "risk_level": "critical",
            "cve": "cve01",
            "name": "测试漏洞01"
        },
        {
            "risk_level": "critical",
            "cve": "cve02",
            "name": "测试漏洞02"
        },
        {
            "risk_level": "critical",
            "cve": "cve05",
            "name": "测试漏洞05"
        }
    ],
    "detail_url": "debug",
    "critical_risk_bugs": 2,
    "high_risk_bugs": 1,
    "mid_risk_bugs": 2,
    "low_risk_bugs": 0,
    "ignore_risk_bugs": 3,
    "code": 0
}
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
