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

'''
예금주정보 1건을 조회합니다.
'''

try:
    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회할 계좌 기관코드
    bankCode = "0004"

    # 조회할 계좌번호
    accountNumber = "9432451175851"

    accountInfo = accountCheckService.checkAccountInfo(CorpNum, bankCode, accountNumber)

    print("=" * 15 + " 예금주조회 " + "=" * 15)

    print("bankCode (기관코드) : %s " % accountInfo.bankCode)
    print("accountNumber (계좌번호) : %s " % accountInfo.accountNumber)
    print("accountName (예금주 성명) : %s " % accountInfo.accountName)
    print("checkDate (확인일시) : %s " % accountInfo.checkDate)
    print("resultCode (응답코드) : %s " % accountInfo.resultCode)
    print("resultMessage (응답메시지) : %s " % accountInfo.resultMessage)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
