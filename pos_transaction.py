# ### **A real-world example: POS terminal**
# Think about a POS machine at a shop. A customer wants to pay for goods with a card.
# Before any code is written, a programmer must think through the logic:
# Staff enters the amount.
# Customer inserts a card.
# Customer enters a PIN.
# System checks whether the card is valid.
# If the card is invalid, decline the transaction.
# System checks whether the PIN is correct.
# If the PIN is incorrect three times, block the card.
# System checks whether the customer has sufficient funds.
# If funds are insufficient, decline the transaction.
# If everything is fine, approve the transaction and print a receipt.

def pos_transaction(amount, card_valid, pin_correct, sufficient_funds):
    if not card_valid:
        return "Transaction declined: Invalid card."
    if not pin_correct:
        return "Transaction declined: Incorrect PIN."
    if not sufficient_funds:
        return "Transaction declined: Insufficient funds."
    return "Transaction approved. Printing receipt."