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
예금주성명 1건을 조회합니다.
'''

try:
    # 팝빌회원 사업자번호 ('-' 제외 10자리)
    CorpNum = testValue.testCorpNum

    # 조회할 계좌 기관코드
    # - https://docs.popbill.com/accountcheck/?lang=python#BankCodeList
    bankCode = "0004"

    # 조회할 계좌번호 (하이픈 '-' 제외 8자리 이상 14자리 이하)
    accountNumber = "9432451175851"

    # 팝빌 회원 아이디
    userId = testValue.testUserID

    accountInfo = accountCheckService.checkAccountInfo(CorpNum, bankCode, accountNumber, userId)

    print("=" * 15 + " 예금주조회 " + "=" * 15)

    print("bankCode (기관코드) : %s " % accountInfo.bankCode)
    print("accountNumber (계좌번호) : %s " % accountInfo.accountNumber)
    print("accountName (예금주 성명) : %s " % accountInfo.accountName)
    print("checkDate (확인일시) : %s " % accountInfo.checkDate)
    print("resultCode (응답코드) : %s " % accountInfo.resultCode)
    print("resultMessage (응답메시지) : %s " % accountInfo.resultMessage)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
