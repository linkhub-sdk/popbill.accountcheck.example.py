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
1건의 예금주실명을 조회합니다.
- https://developers.popbill.com/reference/accountcheck/python/api/check#CheckDepositorInfo
"""

try:
    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 조회할 기관코드
    bankCode = ""

    # 조회할 기관의 계좌번호
    accountNumber = ""

    # 실명번호 유형 ( P / B 중 택 1 ,  P = 개인, B = 사업자)
    identityNumType = "P"

    # 실명번호 (하이픈 '-' 제외하고 입력)
    # └ 실명번호 유형 값이 "B"인 경우 사업자번호(10 자리) 입력
    # └ 실명번호 유형 값이 "P"인 경우 생년월일(6 자리) 입력 (형식 : YYMMDD)
    identityNum = ""

    depositorInfo = accountCheckService.checkDepositorInfo( CorpNum, bankCode,
        accountNumber, identityNumType, identityNum )

    print("=" * 15 + " 예금주조회 " + "=" * 15)

    print("result (상태코드) : %s " % depositorInfo.resultCode)
    print("resultMessage (상태메시지) : %s " % depositorInfo.resultMessage)
    print("accountName (예금주 성명) : %s " % depositorInfo.accountName)
    print("bankCode (기관코드) : %s " % depositorInfo.bankCode)
    print("accountNumber (계좌번호) : %s " % depositorInfo.accountNumber)
    print("identityNumType (실명번호 유형) : %s " % depositorInfo.identityNumType)
    print("identityNum (실명번호) : %s " % depositorInfo.identityNum)
    print("checkDT (확인일시) : %s " % depositorInfo.checkDT)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
