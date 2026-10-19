''' 
Three main entity 
|  ENTITAS  |                FIELD MINIMAL             | Aturan                                                  |
|Transaction| id, date, type, category_id, amount, note| Amount berupa integer rupiah positif; note boleh kosong |
|  Category	| id, name, type	                       | Type adalah income atau expense                         |
|   Budget  |       id, category_id, period, amount	   | Anggaran bulanan positif untuk kategori pengeluaran     |
'''

from dataclasses import dataclass
from typing import Literal

TransactionType = Literal["income", "expense"]

#data class decorator is decorator that specially optimized for storing-only class, automatically generate __init__, __repr__, and __eq__
#frozen = True disallow attribute change thus prevent any accidental change
@dataclass(frozen=True)
class Transaction():
    id : int
    date : str
    type : TransactionType
    category_id : int
    amount : int
    note : str | None = None

@dataclass(frozen=True)
class Category:
    id : int
    name : str
    type : TransactionType

@dataclass(frozen=True)
class Budget:
    id : int
    category_id : int
    budget_amount : int
    period : str #date of budget being set

@dataclass(frozen=True)
class FinancialSummary:
    total_income : int
    total_expenses : int
    net_cash_flow : int
    

