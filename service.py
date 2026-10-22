'''
output contract for service function
|           FUNCTION                 |          OUTPUT          |
| create_transaction(...)            |	int — ID transaksi baru  |
| get_transaction(transaction_id)    |	Transaction \| None      |
| list_transactions(...)	         |      list[Transaction]      |
| update_transaction(...)	         |  bool — apakah transaksi berhasil ditemukan dan diperbarui |
| delete_transaction(transaction_id) |	bool — apakah transaksi berhasil ditemukan dan dihapus |
'''

