from bankAcount import MinimumBalanceAcount

accountMinimum = MinimumBalanceAcount(1500, 1000)

result = accountMinimum.try_withdraw(400)
print(result.message)