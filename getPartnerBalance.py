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
파트너의 잔여포인트를 확인합니다.
- https://developers.popbill.com/reference/accountcheck/python/api/point#GetPartnerBalance
"""

try:
    print("=" * 15 + " 파트너 잔여포인트 확인 " + "=" * 15)

    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    balance = accountCheckService.getPartnerBalance(CorpNum)

    print("파트너 잔여포인트: %f" % balance)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
