# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import AccountCheckService, PopbillException

accountCheckService = AccountCheckService(testValue.LinkID, testValue.SecretKey)
accountCheckService.IsTest = testValue.IsTest
accountCheckService.IPRestrictOnOff = testValue.IPRestrictOnOff
accountCheckService.UseStaticIP = testValue.UseStaticIP
accountCheckService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
예금주조회 API 서비스 과금정보를 확인합니다.
- https://developers.popbill.com/reference/accountcheck/python/api/point#GetChargeInfo
"""

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 서비스 유형, 계좌성명조회 - 성명 , 계좌실명조회 - 실명
    serviceType = "성명"

    response = accountCheckService.getChargeInfo(CorpNum, UserID, serviceType)

    tmp = "unitCost (조회단가) : " + response.unitCost + "\n"
    tmp += "chargeMethod (과금유형) : " + response.chargeMethod + "\n"
    tmp += "rateSystem (과금제도) : " + response.rateSystem
    print(tmp)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
