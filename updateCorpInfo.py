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

from popbill import CorpInfo, AccountCheckService, PopbillException

accountCheckService = AccountCheckService(testValue.LinkID, testValue.SecretKey)
accountCheckService.IsTest = testValue.IsTest
accountCheckService.IPRestrictOnOff = testValue.IPRestrictOnOff
accountCheckService.UseStaticIP = testValue.UseStaticIP
accountCheckService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원사의 회사정보를 수정 합니다.
- https://docs.popbill.com/accountcheck/python/api#UpdateCorpInfo
"""

try:
    print("=" * 15 + " 회사정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 회사정보
    corpInfo = CorpInfo(

        # 대표자 성명 (최대 100자)
        ceoname="대표자_성명",

        # 상호 (최대 200자)
        corpName="상호",

        # 주소 (최대 300자)
        addr="주소",

        # 업태 (최대 100자)
        bizType="업태",

        # 종목 (최대 100자)
        bizClass="종목"
    )

    result = accountCheckService.updateCorpInfo(CorpNum, corpInfo)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
