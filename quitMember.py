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
from popbill import AccountCheckService, PaymentForm, PopbillException

accountCheckService = AccountCheckService(testValue.LinkID, testValue.SecretKey)
accountCheckService.IsTest = testValue.IsTest
accountCheckService.IPRestrictOnOff = testValue.IPRestrictOnOff
accountCheckService.UseStaticIP = testValue.UseStaticIP
accountCheckService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
회원 탈퇴 요청을 보냅니다.
- https://developers.popbill.com/reference/accountcheck/python/api/point#QuitMember
"""

try:
    print("=" * 15 + " 회원 탈퇴 신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum
    # 회원 탈퇴 사유
    QuitReason = "회원 탈퇴 예제 입니다."

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    response = AccountCheckService.QuitREquest(CorpNum, QuitReason, UserID)

    print(" refundableBalance (환불 가능 포인트) : %s" % response.refundableBalance)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
