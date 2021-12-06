# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import AccountCheckService, PopbillException

accountCheckService = AccountCheckService(testValue.LinkID, testValue.SecretKey)
accountCheckService.IsTest = testValue.IsTest
accountCheckService.IPRestrictOnOff = testValue.IPRestrictOnOff
accountCheckService.UseStaticIP = testValue.UseStaticIP
accountCheckService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
예금주조회 단가를 확인합니다.
'''

try:
    print("=" * 15 + " 예금주조회 단가 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 서비스 유형, 계좌성명조회 - 성명 , 계좌실명조회 - 실명 	
    serviceType = "실명"

    unitCost = accountCheckService.getUnitCost(CorpNum, UserID, serviceType)

    print("조회 단가 : %f" % unitCost)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
