# START
# READ sender_balance
# READ transfer_amount`
# IF transfer_amount <= sender_balance
# THEN subtract transfer_amount from sender_balance add transfer_amount to receiver_balance
# set receipt to "Success"
# ELSE set receipt to "Insufficient funds"
# SHOW receipt END`  
def transfer_money(sender_balance, receiver_balance,transfer_amount):
    if transfer_amount <= sender_balance:
        sender_balance = transfer_amount - sender_balance
        receiver_balance = transfer_amount + receiver_balance
        receipt = "Success"
    else:
        receipt = "Insufficient funds"
    return receipt, sender_balance, receiver_balance