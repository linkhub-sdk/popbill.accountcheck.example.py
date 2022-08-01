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
1건의 예금주실명을 조회합니다.
- https://docs.popbill.com/accountcheck/python/api#CheckDepositorInfo
'''

try:
    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 조회할 기관코드
    # - https://docs.popbill.com/accountcheck/?lang=python#BankCodeList
    bankCode = ""

    # 조회할 기관의 계좌번호 (하이픈 '-' 제외 8자리 이상 14자리 이하)
    accountNumber = ""

    # 등록번호 유형 ( P / B 중 택 1 ,  P = 개인, B = 사업자)
    identityNumType = "P"

    # 등록번호
    # - IdentityNumType 값이 "B" 인 경우 (하이픈 '-' 제외  사업자번호(10)자리 입력 )
    # - IdentityNumType 값이 "P" 인 경우 (생년월일(6)자리 입력 (형식 : YYMMDD))
    identityNum =""

    # 팝빌 회원 아이디
    userId = testValue.testUserID

    depositorInfo = accountCheckService.checkDepositorInfo(CorpNum, bankCode, accountNumber, identityNumType, identityNum, userId)

    print("=" * 15 + " 예금주조회 " + "=" * 15)

    print("result (응답코드) : %s " % depositorInfo.resultCode)
    print("resultMessage (응답메시지) : %s " % depositorInfo.resultMessage)
    print("accountName (예금주 성명) : %s " % depositorInfo.accountName)
    print("bankCode (기관코드) : %s " % depositorInfo.bankCode)
    print("accountNumber (계좌번호) : %s " % depositorInfo.accountNumber)
    print("identityNumType (등록번호 유형) : %s " % depositorInfo.identityNumType )
    print("identityNum (등록번호) : %s " % depositorInfo.identityNum )
    print("checkDate (확인일시) : %s " % depositorInfo.checkDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
