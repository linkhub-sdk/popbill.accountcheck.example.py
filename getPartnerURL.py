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
파트너 포인트충전 팝업 URL을 반환합니다.
- 보안정책에 따라 반환된 URL은 30초의 유효시간을 갖습니다.
- https://docs.popbill.com/accountcheck/python/api#GetPartnerURL
'''

try:
    print("=" * 15 + " 파트너 포인트충전 URL 확인 " + "=" * 15)

    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # CHRG-포인트 충전 URL
    TOGO = "CHRG"

    url = accountCheckService.getPartnerURL(CorpNum, TOGO)

    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
