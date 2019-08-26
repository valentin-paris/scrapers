# import fileUtils
#
# payload = {"creditPurposeCode": {"T": "text", "V": "30096"},
#             "loanAmount": {"V": "6000", "T": "decimal"},
#             "maturityMonthQuantity": {"V": "42", "E": "XMADg6Dx/ncBfdlwyFI17+ULAZ/s6bUBdZqZ0kt2bcA=", "T": "decimal"}}
#
#
# amtRange = list(range(2500, 25000, 2500))
#
# firstMonthRange = list(range(12, 36, 6))
# secondMonthRange = list(range(12, 42, 6))
# tirthMonthRange = list(range(12, 48, 6))
# fourthMonthRange = list(range(12, 54, 6))
# fifthMontRange = list(range(12, 66, 6))
# sixthMontRange = list(range(12, 78, 6))
#
# amntToMonthRanges = {
#     tuple(range(2500, 4000, 500)): list(range(12, 36, 6)),
#     tuple(range(4000, 6000, 500)): list(range(12, 42, 6)),
#     tuple(range(6000, 8000, 500)): list(range(12, 48, 6)),
#     tuple(range(8000, 10000, 500)): list(range(12, 54, 6)),
#     tuple(range(10000, 15000, 1000)): list(range(12, 66, 6)),
#     tuple(range(15000, 27000, 2000)): list(range(12, 78, 6))
# }
#
# for ke in amntToMonthRanges:
#     print(ke)
#
# sum = 0
# for key in amntToMonthRanges:
#     sum += len(key) * len(amntToMonthRanges[key])
# print(sum)
#
# # for amt in amtRange:
# #     payload['loanAmount']['V'] = str(amt)
# #     print(payload)
#
#
# requestedDataSampleForAmt = {
#     "personalProperty": {
#         "loanAmount": {"V": "6000", "E": "dHRUaDtw1Q7RU5VjcdzgUv+99ndSMmQSxnklXKtrBVw\u003d", "T": "decimal"},
#         "maturityMonthQuantity": {"V": "42", "E": "dif5WgsWy1k4IVEzGzT9YyoATddIIEaJSDYS7HbtlQ0\u003d", "T": "short"},
#         "termAmount": {"V": "158.28", "E": "eKH4xgpRqeFUJeLpAE1WV/JKKvYBX+pnXm2bFGx1+JM\u003d", "T": "decimal"},
#         "yearCostPercent": {"V": "5.99000", "E": "zEPwV6wAeXQXBRosolByiwix1vSeTkeB2hTVq/DcufA\u003d", "T": "decimal"},
#         "yearInterestPercent": {"V": "5.99000", "E": "luTPHQY3eaR6vjgUpBw6k0uiwkqXMnM/FpWoAcsGP0A\u003d", "T": "decimal"},
#         "totalLoanAmount": {"V": "6647.72", "E": "4tn4dDGLt/45u6qI9r8HByssniusXBIbfJtoUFJVUrQ\u003d", "T": "decimal"}
#     },
#     "header": {"resultCode": {"V": "00", "T": "text"}
#     }
# }
#
#
# sample2 = {
#     "personalProperty": {
#         "loanAmount": {"V": "10000", "E": "KKB1fA6h3nJlwmi8D3ioNOtHousbnn2cQNS0AQFzx4k\u003d", "T": "decimal"},
#         "maturityMonthQuantity": {"V": "42", "E": "TtSE4WcXb1JFEjZTiWKfBAz4SK+h96kPufFLFmFSyJE\u003d", "T": "short"},
#         "termAmount": {"V": "263.80", "E": "hAFAHYjW/lDlgM2S9bpcJq56fcG2eTgrVhHFdAMv1MU\u003d", "T": "decimal"},
#         "yearCostPercent": {"V": "5.99000", "E": "8/JIUP9Bpuq9CbQMJWwv/AJz6qc5mYhyuwERWW2qDrM\u003d", "T": "decimal"},
#         "yearInterestPercent": {"V": "5.99000", "E": "0TgizZwUm0+EImKdHSnvT6Pv5Vc/3QOR0ZwmxKXzOFk\u003d", "T": "decimal"},
#         "totalLoanAmount": {"V": "11079.48", "E": "Iz2qHl4OsoaXzWven7Kr+iBiFkINcaFXSt1HS1EMnFQ\u003d", "T": "decimal"}
#     },
#     "header": {
#         "resultCode": {"V": "00", "T": "text"}
#     }
# }
#
#
# tel = [8, 5, 3, 5, 0, 5, 18, 52, 5, 0, 2, 420, 52, 36]
#
#
#
# price = 7000
#
# payload2 = {"creditPurposeCode": {"T": "text", "V": "30096"},
#             "loanAmount": {"V": str(price), "T": "decimal"},
#             "maturityMonthQuantity": {"V": "42", "E": "XMADg6Dx/ncBfdlwyFI17+ULAZ/s6bUBdZqZ0kt2bcA=", "T": "decimal"}}
#
# print(payload2)
#
# value = {
#     "personalProperty":{
#         "loanAmount":{"V":"7000","E":"C/fvD4kIGPQIrne69FBFwMxis0lBtDGOB18x63dm+uo\u003d","T":"decimal"},
#         "maturityMonthQuantity":{"V":"76","E":"wuohz0wskiIY6SxY52c02cFKfRA8wwp9JmlVh8Rjwls\u003d","T":"short"},
#         "termAmount":{"V":"96.58","E":"e4lZxByk6G9cNNOMKb3FmXnjF/VoLP/i2lXNQLgWrzA\u003d","T":"decimal"},
#         "yearCostPercent":{"V":"1.50000","E":"weMVgv+JclQhOTaSgVyULhBNGLfYgVzmEKlFdxn7gpg\u003d","T":"decimal"},
#         "yearInterestPercent":{"V":"1.50000","E":"dFua8mCQpAWofNMIkDXHSM3/zRBvoW1t0hCQamdko8k\u003d","T":"decimal"},
#         "totalLoanAmount":{"V":"7339.65","E":"0XgjpbpgKb1HTmN8rfzg4azmLKRXX1U4bneX5fEHius\u003d","T":"decimal"}
#     },
#     "header":{"resultCode":{"V":"00","T":"text"}
#               }
# }
#
# def buildStructuredData():
#     pass
#
#
# print(value['personalProperty']['yearInterestPercent']['V'])
#
#
# requestData =[
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 2500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 2500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 2500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 2500, 'duration': 30, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3000, 'duration': 30, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 3500, 'duration': 30, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4000, 'duration': 36, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4500, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 4500, 'duration': 36, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5000, 'duration': 36, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5500, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 5500, 'duration': 36, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6000, 'duration': 42, 'rate': '1.50000'}],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6500, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6500, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 6500, 'duration': 42, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7000, 'duration': 42, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7500, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7500, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 7500, 'duration': 42, 'rate': '1.50000'}],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8000, 'duration': 48, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8500, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8500, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8500, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 8500, 'duration': 48, 'rate': '1.50000'}],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9000, 'duration': 48, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9500, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9500, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9500, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9500, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9500, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9500, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 9500, 'duration': 48, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 10000, 'duration': 60, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 11000, 'duration': 60, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 12000, 'duration': 60, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 13000, 'duration': 60, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 14000, 'duration': 60, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 60, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 66, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 15000, 'duration': 72, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 60, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 66, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 17000, 'duration': 72, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 60, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 66, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 19000, 'duration': 72, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 60, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 66, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 21000, 'duration': 72, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 60, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 66, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 23000, 'duration': 72, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 12, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 18, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 24, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 30, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 36, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 42, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 48, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 54, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 60, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 66, 'rate': '1.50000'},
#                     {'type': 'Prêt Voiture Neuve', 'amount': 25000, 'duration': 72, 'rate': '1.50000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 2500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 2500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 2500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 2500, 'duration': 30, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 3000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 3000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 3000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 3000, 'duration': 30, 'rate': '3.95000'}
#                 ], [{'type': "Prêt Voiture d'occasion", 'amount': 3500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 3500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 3500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 3500, 'duration': 30, 'rate': '3.95000'}
#                     ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4000, 'duration': 36, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4500, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 4500, 'duration': 36, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5000, 'duration': 36, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5500, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 5500, 'duration': 36, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6000, 'duration': 42, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6500, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6500, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 6500, 'duration': 42, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7000, 'duration': 42, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7500, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7500, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 7500, 'duration': 42, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8000, 'duration': 48, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8500, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8500, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8500, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 8500, 'duration': 48, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9000, 'duration': 48, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9500, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9500, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9500, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9500, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9500, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9500, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 9500, 'duration': 48, 'rate': '3.95000'}
#                 ], [{'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 10000, 'duration': 60, 'rate': '3.95000'}
#                     ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 11000, 'duration': 60, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 12000, 'duration': 60, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 13000, 'duration': 60, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 14000, 'duration': 60, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 60, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 66, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 15000, 'duration': 72, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 60, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 66, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 17000, 'duration': 72, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 60, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 66, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 19000, 'duration': 72, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 60, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 66, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 21000, 'duration': 72, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 60, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 66, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 23000, 'duration': 72, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 12, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 18, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 24, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 30, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 36, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 42, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 48, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 54, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 60, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 66, 'rate': '3.95000'},
#                     {'type': "Prêt Voiture d'occasion", 'amount': 25000, 'duration': 72, 'rate': '3.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 2500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 2500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 2500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 2500, 'duration': 30, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 3000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 3000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 3000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 3000, 'duration': 30, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 3500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 3500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 3500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 3500, 'duration': 30, 'rate': '2.95000'}
#                     ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 4000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4000, 'duration': 36, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 4500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4500, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 4500, 'duration': 36, 'rate': '2.95000'}],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 5000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5000, 'duration': 36, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 5500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5500, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 5500, 'duration': 36, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 6000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6000, 'duration': 42, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 6500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6500, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6500, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 6500, 'duration': 42, 'rate': '2.95000'}],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 7000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7000, 'duration': 42, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 7500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7500, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7500, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 7500, 'duration': 42, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 8000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8000, 'duration': 48, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 8500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8500, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8500, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8500, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 8500, 'duration': 48, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 9000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9000, 'duration': 48, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 9500, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9500, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9500, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9500, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9500, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9500, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 9500, 'duration': 48, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 10000, 'duration': 60, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 11000, 'duration': 60, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 12000, 'duration': 60, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 13000, 'duration': 60, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 14000, 'duration': 60, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 60, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 66, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 15000, 'duration': 72, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 60, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 66, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 17000, 'duration': 72, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 60, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 66, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 19000, 'duration': 72, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 60, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 66, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 21000, 'duration': 72, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 60, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 66, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 23000, 'duration': 72, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 12, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 18, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 24, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 30, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 36, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 42, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 48, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 54, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 60, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 66, 'rate': '2.95000'},
#                     {'type': 'Prêt Rénovation', 'amount': 25000, 'duration': 72, 'rate': '2.95000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 2500, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 2500, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 2500, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 2500, 'duration': 30, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 3000, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 3000, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 3000, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 3000, 'duration': 30, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 3500, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 3500, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 3500, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 3500, 'duration': 30, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 4000, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4000, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4000, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4000, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4000, 'duration': 36, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 4500, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4500, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4500, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4500, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 4500, 'duration': 36, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 5000, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5000, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5000, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5000, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5000, 'duration': 36, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 5500, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5500, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5500, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5500, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 5500, 'duration': 36, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 6000, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6000, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6000, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6000, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6000, 'duration': 36, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6000, 'duration': 42, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 6500, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6500, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6500, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6500, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6500, 'duration': 36, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 6500, 'duration': 42, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 7000, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7000, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7000, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7000, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7000, 'duration': 36, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7000, 'duration': 42, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 7500, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7500, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7500, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7500, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7500, 'duration': 36, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 7500, 'duration': 42, 'rate': '5.99000'}
#                 ],
#                 [
#                     {'type': 'Prêt Personnel', 'amount': 8000, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8000, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8000, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8000, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8000, 'duration': 36, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8000, 'duration': 42, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8000, 'duration': 48, 'rate': '5.99000'}
#                 ], [{'type': 'Prêt Personnel', 'amount': 8500, 'duration': 12, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8500, 'duration': 18, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8500, 'duration': 24, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8500, 'duration': 30, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8500, 'duration': 36, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8500, 'duration': 42, 'rate': '5.99000'},
#                     {'type': 'Prêt Personnel', 'amount': 8500, 'duration': 48, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 9000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9000, 'duration': 48, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 9500, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9500, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9500, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9500, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9500, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9500, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 9500, 'duration': 48, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 10000, 'duration': 60, 'rate': '6'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 11000, 'duration': 60, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 12000, 'duration': 60, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 13000, 'duration': 60, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 14000, 'duration': 60, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 60, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 66, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 15000, 'duration': 72, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 60, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 66, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 17000, 'duration': 72, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 60, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 66, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 19000, 'duration': 72, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 60, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 66, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 21000, 'duration': 72, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 60, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 66, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 23000, 'duration': 72, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 12, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 18, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 24, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 30, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 36, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 42, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 48, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 54, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 60, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 66, 'rate': '5.99000'},
#                         {'type': 'Prêt Personnel', 'amount': 25000, 'duration': 72, 'rate': '5.99000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 2500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 2500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 2500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 2500, 'duration': 30, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 3000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 3000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 3000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 3000, 'duration': 30, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 3500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 3500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 3500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 3500, 'duration': 30, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 4000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4000, 'duration': 36, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 4500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4500, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 4500, 'duration': 36, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 5000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5000, 'duration': 36, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 5500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5500, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 5500, 'duration': 36, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 6000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6000, 'duration': 42, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 6500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6500, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6500, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 6500, 'duration': 42, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 7000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7000, 'duration': 42, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 7500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7500, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7500, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 7500, 'duration': 42, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 8000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8000, 'duration': 48, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 8500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8500, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8500, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8500, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 8500, 'duration': 48, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 9000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9000, 'duration': 48, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 9500, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9500, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9500, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9500, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9500, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9500, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 9500, 'duration': 48, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 10000, 'duration': 60, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 11000, 'duration': 60, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 12000, 'duration': 60, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 13000, 'duration': 60, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 14000, 'duration': 60, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 60, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 66, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 15000, 'duration': 72, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 60, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 66, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 17000, 'duration': 72, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 60, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 66, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 19000, 'duration': 72, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 60, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 66, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 21000, 'duration': 72, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 60, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 66, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 23000, 'duration': 72, 'rate': '1.80000'}
#                     ],
#                     [
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 12, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 18, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 24, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 30, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 36, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 42, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 48, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 54, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 60, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 66, 'rate': '1.80000'},
#                         {'type': 'Prêt Energie', 'amount': 25000, 'duration': 72, 'rate': '1.80000'}
#                     ]
# ]
#
#
# def createGroups(structuredData):
#     loanGroups = {}
#     for loanList in structuredData:
#         for loanElement in loanList:
#             if (loanElement['type'], loanElement['duration'], loanElement['rate']) not in loanGroups.keys():
#                 loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'])] = [loanElement['amount']]
#             else:
#                 loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'])].append(loanElement['amount'])
#     return loanGroups
#
#
#
# def formatDataFrom(groups, provider):
#     frameToExport = []
#     for eachGroup in groups:
#         frameToExport.append([provider, eachGroup[0], min(map(float, groups[eachGroup])), max(map(float, groups[eachGroup])), int(eachGroup[1]), float(eachGroup[2])])
#     return frameToExport
#
#
#
# tab_column = ['PROVIDER ', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
#
#
# fileUtils.displayRates(tab_Column, formatDataFrom(createGroups(requestData), 'CBC BANK'))
# print(formatDataFrom(createGroups(requestData), 'CBC BANK'))
#
#


import requests

# url = "https://promo.ing.be/RenovationLoan/webservices/wsSimulation.asmx/GetSimulations"
#
# payload = "{\"type\":1,\"amount\":19500}"
# headers = {
#     'Connection': "keep-alive",
#     'Content-Length': "25",
#     'Accept': "application/json, text/javascript, */*; q=0.01",
#     'X-Requested-With': "XMLHttpRequest",
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
#     'Sec-Fetch-Mode': "cors",
#     'Content-Type': "application/json; charset=UTF-8",
#     'Origin': "https://promo.ing.be",
#     'Sec-Fetch-Site': "same-origin",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "353f8b0b-b95c-46e4-93bc-4ed75555e343,46ea9a56-e6db-48e6-81dd-6377195930cd",
#     'Host': "promo.ing.be",
#     'Accept-Encoding': "gzip, deflate",
#     'cache-control': "no-cache"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
#
#
#
#
# payload2 = "{\"type\":2,\"amount\":19500}"
#
# response2 = requests.request("POST", url, data=payload2, headers=headers)
#
# print(response2.text)




url = "https://loan.carrefourfinance.be/fimsim/"

querystring = {"retailer":"2487635","amount":"10000","duration":"42","materialCode":"502","language":"fr","v-1566812049495":"","":""}

import json
import random
import DataUtils

params = (
    ('retailer', '2487635'),
    ('amount', '10000'),
    ('duration', '42'),
    ('materialCode', '502'),
    ('language', 'fr'),
    ('v-1559684081349', ''),
    ('v-1559684192192', ''),
)

data = {
  'v-browserDetails': '1',
  'theme': 'fimsim',
  'v-appId': 'fimsim-1274463091',
  'v-sh': '1080',
  'v-sw': '1920',
  'v-cw': '846',
  'v-ch': '911',
  'v-curdate': '1559684192192',
  'v-tzo': '-120',
  'v-dstd': '60',
  'v-rtzo': '-60',
  'v-dston': 'true',
  'v-vw': '846',
  'v-vh': '0',
  'v-loc': 'https://loan.carrefourfinance.be/fimsim/?retailer=2487635&amount=10000&duration=42&materialCode=502&&language=fr&fbclid=IwAR1gizN8cLzmboWhXLZG4e4JMxGbeBUMp_dLS5Ax6EjUpflUty4Xgg_959s&v-1559684081349',
  'v-wn': 'fimsim-1274463091-0.3835151505760399'
}
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-type': "application/x-www-form-urlencoded",
    'Referer': "https://loan.carrefourfinance.be/fimsim/?retailer=2487635&amount=10000&duration=42&materialCode=502&&language=fr",
    'Sec-Fetch-Mode': "cors",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36Content-type:",
    'accept': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "7b658075-7cac-4492-aa5e-35dc9de15b5c,920db245-41ae-4a3b-ba7a-42b8fb99f938",
    'Host': "loan.carrefourfinance.be",
    'Cookie': "JSESSIONID=Wfs786CxqGWt3DH3D-SE_v_fJiierqZNFgQzu-sd.buywl0004:phenix-buywl0004; TS0181821e=016b073a458b3ead7e5da992cfc5508af95a98314a56e90d6105fe03edeb9d2e637b5f3b6042a24570afad135a2a3e812492425cc52a4db37ad282acfb3dbc6ed6901967e1; BIGipServer~ap-buyway_int_app_front_dmz-337~p-buyway-phenix-front-prod-80=rd337o00000000000000000000ffff0ad7b545o80; TS016b11db=016b073a4540c4048e58318c0c404fdec50140c83c6ba6b570223c5d8261167db5492ef2445c8e7e1bff8683afc2af8e018b63f459f3d1c47aa7891593d4f72e621c8f69e9",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "528",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.post('https://loan.carrefourfinance.be/fimsim/',  params=params,  data=data)
print(response.text)
print(response.content)



def requestForData():
    params = (
        ('retailer', '2487635'),
        ('amount', '10000'),
        ('duration', '42'),
        ('materialCode', '502'),
        ('language', 'fr'),
        ('v-1559684081349', ''),
        ('v-1559684192192', ''),
    )

    data = {
        'v-browserDetails': '1',
        'theme': 'fimsim',
        'v-appId': 'fimsim-1274463091',
        'v-sh': '1080',
        'v-sw': '1920',
        'v-cw': '846',
        'v-ch': '911',
        'v-curdate': '1559684192192',
        'v-tzo': '-120',
        'v-dstd': '60',
        'v-rtzo': '-60',
        'v-dston': 'true',
        'v-vw': '846',
        'v-vh': '0',
        'v-loc': 'https://loan.carrefourfinance.be/fimsim/?retailer=2487635&amount=10000&duration=42&materialCode=502&&language=fr&fbclid=IwAR1gizN8cLzmboWhXLZG4e4JMxGbeBUMp_dLS5Ax6EjUpflUty4Xgg_959s&v-1559684081349',
        'v-wn': 'fimsim-1274463091-0.3835151505760399'
    }
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Content-type': "application/x-www-form-urlencoded",
        'Referer': "https://loan.carrefourfinance.be/fimsim/?retailer=2487635&amount=10000&duration=42&materialCode=502&&language=fr",
        'Sec-Fetch-Mode': "cors",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36Content-type:",
        'accept': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "7b658075-7cac-4492-aa5e-35dc9de15b5c,920db245-41ae-4a3b-ba7a-42b8fb99f938",
        'Host': "loan.carrefourfinance.be",
        'Cookie': "JSESSIONID=Wfs786CxqGWt3DH3D-SE_v_fJiierqZNFgQzu-sd.buywl0004:phenix-buywl0004; TS0181821e=016b073a458b3ead7e5da992cfc5508af95a98314a56e90d6105fe03edeb9d2e637b5f3b6042a24570afad135a2a3e812492425cc52a4db37ad282acfb3dbc6ed6901967e1; BIGipServer~ap-buyway_int_app_front_dmz-337~p-buyway-phenix-front-prod-80=rd337o00000000000000000000ffff0ad7b545o80; TS016b11db=016b073a4540c4048e58318c0c404fdec50140c83c6ba6b570223c5d8261167db5492ef2445c8e7e1bff8683afc2af8e018b63f459f3d1c47aa7891593d4f72e621c8f69e9",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "528",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.post('https://loan.carrefourfinance.be/fimsim/', params=params, data=data)
    return json.loads(json.loads(response.text)['uidl'])


def bankData():
    dataList = requestForData()['state']['1']['materialCodesMapping'][1]
    bankData = dataList[random.randint(0, len(dataList)-1)]['rateRanges']
    for loan in bankData:
        loan['duration'] = loan['minDuration']
        loan['amount'] = loan['minCreditAmount']
        loan['rate'] = loan['taeg']
        loan['type'] = 'All Loans'
        loan['productID'] = 'CAFI0001'
    return bankData

print(bankData())

print(DataUtils.createGroups(bankData()))

def carrefourLoanScrape():
    tab_Column = ['PROVIDER ', 'PRODUCT_ID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    dataMatrix = DataUtils.formatDataFrom(DataUtils.createGroups(bankData()), 'BANK CARREFOUR')
    return DataUtils.processData(dataMatrix, tab_Column, 'CARREFOUR SCRAPE', 'carrefour_rates')



carrefourLoanScrape()

test_data = json.loads(response.text)

print(test_data)


essai= json.loads(test_data['uidl'])

for elt in test_data:
    print(elt)
    print(test_data[elt])


print("ESSAIE ELEMENT ###########################################################")
for elt in essai:
    print('this is the element')
    print(elt)
    print(essai[elt])
    print()
    print()

    #print(test_data['uidl'][elt])
print('#################################################################################################\n###################################################'
      '#############################################################\n#############################################################################')
for elt in essai['state']:
    print(elt)
    print(type(elt))
    print(essai['state'][elt])
    print()


print('#################################################################################################\n###################################################'
      '#############################################################\n#############################################################################')


for elt in essai['state']['1']:
    print('this is the element')
    print(elt)
    print(essai['state']['1'][elt])
    print()

print('THE CODE MAPPING ')

theMap = essai['state']['1']['materialCodesMapping']

for i in theMap[0]:
    print(i)

print()

for i in theMap[1]:
    print(i)



taste = {
   'rateRanges':[
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.74',
         'maxDuration':48
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700',
         'maxCreditAmount':'3700',
         'tada':'8.55',
         'maxDuration':30
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700.01',
         'maxCreditAmount':'5600',
         'tada':'8.55',
         'maxDuration':36
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'5600.01',
         'maxCreditAmount':'5999.99',
         'tada':'8.55',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.27',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'6.69',
         'maxDuration':84
      }
   ],
   'numberOfMonthsPostponed':0,
   'minDuration':6,
   'paymentDay':7,
   'price':634,
   'minCreditAmount':'3700',
   'id':53164,
   'materialCodes':[
      {
         'materialCodeName':None,
         'id':'919',
         'label':'Travaux / Déco'
      },
      {
         'materialCodeName':None,
         'id':'650',
         'label':'Scolarité'
      },
      {
         'materialCodeName':None,
         'id':'502',
         'label':"Véhicule d'occasion"
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Refinancement de crédits'
      },
      {
         'materialCodeName':None,
         'id':'863',
         'label':'Soins santé'
      },
      {
         'materialCodeName':None,
         'id':'320',
         'label':'Mariage'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Trésorerie'
      },
      {
         'materialCodeName':None,
         'id':'501',
         'label':'Véhicule neuf'
      },
      {
         'materialCodeName':None,
         'id':'972',
         'label':'Déménagement'
      }
   ],
   'maxCreditAmount':'40000',
   'maxDuration':84,
   'alphaProductCode':None
}


test2 = {
   'rateRanges':[
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700',
         'maxCreditAmount':'3700',
         'tada':'8.55',
         'maxDuration':30
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'5600.01',
         'maxCreditAmount':'5999.99',
         'tada':'8.55',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.27',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700.01',
         'maxCreditAmount':'5600',
         'tada':'8.55',
         'maxDuration':36
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.74',
         'maxDuration':48
      }
   ],
   'numberOfMonthsPostponed':0,
   'minDuration':6,
   'paymentDay':7,
   'price':634,
   'minCreditAmount':'3700',
   'id':53164,
   'materialCodes':[
      {
         'materialCodeName':None,
         'id':'502',
         'label':"Véhicule d'occasion"
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Trésorerie'
      },
      {
         'materialCodeName':None,
         'id':'650',
         'label':'Scolarité'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Refinancement de crédits'
      },
      {
         'materialCodeName':None,
         'id':'320',
         'label':'Mariage'
      },
      {
         'materialCodeName':None,
         'id':'919',
         'label':'Travaux / Déco'
      },
      {
         'materialCodeName':None,
         'id':'972',
         'label':'Déménagement'
      },
      {
         'materialCodeName':None,
         'id':'863',
         'label':'Soins santé'
      },
      {
         'materialCodeName':None,
         'id':'501',
         'label':'Véhicule neuf'
      }
   ],
   'maxCreditAmount':'40000',
   'maxDuration':84,
   'alphaProductCode':None
}



test3 = {
   'rateRanges':[
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700.01',
         'maxCreditAmount':'5600',
         'tada':'8.55',
         'maxDuration':36
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700',
         'maxCreditAmount':'3700',
         'tada':'8.55',
         'maxDuration':30
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'5600.01',
         'maxCreditAmount':'5999.99',
         'tada':'8.55',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.74',
         'maxDuration':48
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.27',
         'maxDuration':42
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'6.69',
         'maxDuration':84
      }
   ],
   'numberOfMonthsPostponed':0,
   'minDuration':6,
   'paymentDay':7,
   'price':634,
   'minCreditAmount':'3700',
   'id':53164,
   'materialCodes':[
      {
         'materialCodeName':None,
         'id':'972',
         'label':'Déménagement'
      },
      {
         'materialCodeName':None,
         'id':'502',
         'label':"Véhicule d'occasion"
      },
      {
         'materialCodeName':None,
         'id':'501',
         'label':'Véhicule neuf'
      },
      {
         'materialCodeName':None,
         'id':'919',
         'label':'Travaux / Déco'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Refinancement de crédits'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Trésorerie'
      },
      {
         'materialCodeName':None,
         'id':'650',
         'label':'Scolarité'
      },
      {
         'materialCodeName':None,
         'id':'863',
         'label':'Soins santé'
      },
      {
         'materialCodeName':None,
         'id':'320',
         'label':'Mariage'
      }
   ],
   'maxCreditAmount':'40000',
   'maxDuration':84,
   'alphaProductCode':None
}


testX = {
   'rateRanges':[
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.27',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'5600.01',
         'maxCreditAmount':'5999.99',
         'tada':'8.55',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.74',
         'maxDuration':48
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700',
         'maxCreditAmount':'3700',
         'tada':'8.55',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700.01',
         'maxCreditAmount':'5600',
         'tada':'8.55',
         'maxDuration':36
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'6.69',
         'maxDuration':84
      }
   ],
   'numberOfMonthsPostponed':0,
   'minDuration':6,
   'paymentDay':7,
   'price':634,
   'minCreditAmount':'3700',
   'id':53164,
   'materialCodes':[
      {
         'materialCodeName':None,
         'id':'919',
         'label':'Travaux / Déco'
      },
      {
         'materialCodeName':None,
         'id':'863',
         'label':'Soins santé'
      },
      {
         'materialCodeName':None,
         'id':'501',
         'label':'Véhicule neuf'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Trésorerie'
      },
      {
         'materialCodeName':None,
         'id':'320',
         'label':'Mariage'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Refinancement de crédits'
      },
      {
         'materialCodeName':None,
         'id':'502',
         'label':"Véhicule d'occasion"
      },
      {
         'materialCodeName':None,
         'id':'650',
         'label':'Scolarité'
      },
      {
         'materialCodeName':None,
         'id':'972',
         'label':'Déménagement'
      }
   ],
   'maxCreditAmount':'40000',
   'maxDuration':84,
   'alphaProductCode':None
}

testZ = {
   'rateRanges':[
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700',
         'maxCreditAmount':'3700',
         'tada':'8.55',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.27',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700.01',
         'maxCreditAmount':'5600',
         'tada':'8.55',
         'maxDuration':36
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'5600.01',
         'maxCreditAmount':'5999.99',
         'tada':'8.55',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.74',
         'maxDuration':48
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'4.4',
         'maxDuration':42
      }
   ],
   'numberOfMonthsPostponed':0,
   'minDuration':6,
   'paymentDay':7,
   'price':634,
   'minCreditAmount':'3700',
   'id':53164,
   'materialCodes':[
      {
         'materialCodeName':None,
         'id':'919',
         'label':'Travaux / Déco'
      },
      {
         'materialCodeName':None,
         'id':'320',
         'label':'Mariage'
      },
      {
         'materialCodeName':None,
         'id':'502',
         'label':"Véhicule d'occasion"
      },
      {
         'materialCodeName':None,
         'id':'863',
         'label':'Soins santé'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Refinancement de crédits'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Trésorerie'
      },
      {
         'materialCodeName':None,
         'id':'650',
         'label':'Scolarité'
      },
      {
         'materialCodeName':None,
         'id':'501',
         'label':'Véhicule neuf'
      },
      {
         'materialCodeName':None,
         'id':'972',
         'label':'Déménagement'
      }
   ],
   'maxCreditAmount':'40000',
   'maxDuration':84,
   'alphaProductCode':None
}

testAlpha= {
   'rateRanges':[
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.27',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.74',
         'maxDuration':48
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700',
         'maxCreditAmount':'3700',
         'tada':'8.55',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'5600.01',
         'maxCreditAmount':'5999.99',
         'tada':'8.55',
         'maxDuration':42
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700.01',
         'maxCreditAmount':'5600',
         'tada':'8.55',
         'maxDuration':36
      }
   ],
   'numberOfMonthsPostponed':0,
   'minDuration':6,
   'paymentDay':7,
   'price':634,
   'minCreditAmount':'3700',
   'id':53164,
   'materialCodes':[
      {
         'materialCodeName':None,
         'id':'320',
         'label':'Mariage'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Trésorerie'
      },
      {
         'materialCodeName':None,
         'id':'502',
         'label':"Véhicule d'occasion"
      },
      {
         'materialCodeName':None,
         'id':'650',
         'label':'Scolarité'
      },
      {
         'materialCodeName':None,
         'id':'501',
         'label':'Véhicule neuf'
      },
      {
         'materialCodeName':None,
         'id':'972',
         'label':'Déménagement'
      },
      {
         'materialCodeName':None,
         'id':'919',
         'label':'Travaux / Déco'
      },
      {
         'materialCodeName':None,
         'id':'863',
         'label':'Soins santé'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Refinancement de crédits'
      }
   ],
   'maxCreditAmount':'40000',
   'maxDuration':84,
   'alphaProductCode':None
}

testLast = {
   'rateRanges':[
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'5600.01',
         'maxCreditAmount':'5999.99',
         'tada':'8.55',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700.01',
         'maxCreditAmount':'5600',
         'tada':'8.55',
         'maxDuration':36
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':61,
         'teg':'6.69',
         'taeg':'6.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'6.69',
         'maxDuration':84
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.27',
         'maxDuration':42
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.74',
         'maxDuration':48
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'3700',
         'maxCreditAmount':'3700',
         'tada':'8.55',
         'maxDuration':30
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'7500.01',
         'maxCreditAmount':'10000',
         'tada':'5.27',
         'maxDuration':30
      },
      {
         'minDuration':43,
         'teg':'5.74',
         'taeg':'5.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'5.74',
         'maxDuration':60
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'20000.01',
         'maxCreditAmount':'40000',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'15000.01',
         'maxCreditAmount':'20000',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':6,
         'teg':'8.55',
         'taeg':'8.9',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'8.55',
         'maxDuration':6
      },
      {
         'minDuration':31,
         'teg':'4.4',
         'taeg':'4.49',
         'minCreditAmount':'6000',
         'maxCreditAmount':'7500',
         'tada':'4.4',
         'maxDuration':42
      },
      {
         'minDuration':7,
         'teg':'5.27',
         'taeg':'5.4',
         'minCreditAmount':'10000.01',
         'maxCreditAmount':'15000',
         'tada':'5.27',
         'maxDuration':30
      }
   ],
   'numberOfMonthsPostponed':0,
   'minDuration':6,
   'paymentDay':7,
   'price':634,
   'minCreditAmount':'3700',
   'id':53164,
   'materialCodes':[
      {
         'materialCodeName':None,
         'id':'650',
         'label':'Scolarité'
      },
      {
         'materialCodeName':None,
         'id':'502',
         'label':"Véhicule d'occasion"
      },
      {
         'materialCodeName':None,
         'id':'501',
         'label':'Véhicule neuf'
      },
      {
         'materialCodeName':None,
         'id':'919',
         'label':'Travaux / Déco'
      },
      {
         'materialCodeName':None,
         'id':'320',
         'label':'Mariage'
      },
      {
         'materialCodeName':None,
         'id':'863',
         'label':'Soins santé'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Trésorerie'
      },
      {
         'materialCodeName':None,
         'id':'810',
         'label':'Refinancement de crédits'
      },
      {
         'materialCodeName':None,
         'id':'972',
         'label':'Déménagement'
      }
   ],
   'maxCreditAmount':'40000',
   'maxDuration':84,
   'alphaProductCode':None
}

print(len(test3['rateRanges']))
for i in range(len(test3['rateRanges'])):
    value = test3['rateRanges'][i]
    print(value)
    print('the index of the value is', i)
    if value in taste['rateRanges'] or value in testZ['rateRanges']:
        print('value is in testZ') if value in testZ['rateRanges'] else print('value is in first test')


print('#################################################################################')
print()

for i in range(len(test3['rateRanges'])):
    val = test3['rateRanges'][i]
    if val['taeg'] == '6.9':
        print(i)
        print(val)
        print()

print('######################################################################\n#################################')

for v in testLast['rateRanges']:
    if v in testAlpha['rateRanges']:
        print(v)



print('######################################################################\n#################################')

print('test alph alpha')
for t in testLast['rateRanges']:
    if t in testAlpha['rateRanges']:
        print(t)

print()
print(testAlpha)


print(requestForData())


print('######################################################################\n#################################')
print('THE BANK DATA ARE...')
print(bankData())

for val in bankData():
    print(val)

print()
print()


for val in bankData():
    if val in testAlpha['rateRanges']:
        print(val)





