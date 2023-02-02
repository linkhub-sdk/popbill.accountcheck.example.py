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
1건의 예금주성명을 조회합니다.
- https://developers.popbill.com/reference/accountcheck/python/api/check#CheckAccountInfo
'''

try:
    # 팝빌회원 사업자번호 (하이픈 '-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 조회할 기관코드
    # 조회 가능한 금융기관 : [https://docs.popbill.com/accountcheck/?lang=python#BankCodeList]
    bankCode = ""

    # 조회할 기관의 계좌번호 (하이픈 '-' 제외 8자리 이상 14자리 이하)
    accountNumber = ""

    accountInfo = accountCheckService.checkAccountInfo(CorpNum, bankCode, accountNumber)

    print("=" * 15 + " 예금주조회 " + "=" * 15)

    print("result (응답코드) : %s " % accountInfo.resultCode)
    print("resultMessage (응답메시지) : %s " % accountInfo.resultMessage)
    print("accountName (예금주 성명) : %s " % accountInfo.accountName)
    print("bankCode (기관코드) : %s " % accountInfo.bankCode)
    print("accountNumber (계좌번호) : %s " % accountInfo.accountNumber)
    print("checkDate (확인일시) : %s " % accountInfo.checkDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
