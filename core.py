import datetime
import copy


class OutOfStockError(Exception):

    def __init__(
            self,
            product_id: str,
            available: int,
            requested: int
    ) -> None:
        self.product_id = product_id
        self.available = available
        self.requested = requested

        super().__init__(
            f"Stock insufficient for the product with product_id {product_id}. Available {available} units but i have requested {requested} units.")

    def __str__(selfself) -> str:
        return (
            f"Product {self.product_id}:"
            f"available {self.available}, requested: {self.requested}"
        )

    def __repr__(self) -> str:
        return (
            f"OutOfStockError('{self}"
        )


class Product:  # definir mi clase
    def __init__(  # qué me caracteriza: tú me das unos atributos y yo los guardo en mi estado interno
            self,
            product_id: str,
            name: str,
            category: str
    ) -> None:
        # este es mi estado interno
        self.product_id = product_id
        self.name = name
        self.category = category

    def __str__(self):
        return f"Product ID {self.product_id} - Name: {self.name}"


class Batch:

    def __init__(
            self,
            batch_id: str,
            product_id: str,
            quantity: int,
            unit_cost: float,
            expiration_date: datetime.date
    ) -> None:

        self.batch_id = batch_id
        self.product_id = product_id
        self._quantity = quantity
        self.unit_cost = unit_cost
        self.expiration_date = expiration_date

    def __str__(self) -> str:
        return (
            f"Batch ID {self.batch_id} - Product ID: {self.product_id} - Quantity {self._quantity} - Expiration Date: {self.expiration_date}"
        )

    def get_quantity(self) -> int:
        """Getter of quantity"""
        return self._quantity

    def consume(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        if quantity > self._quantity:
            raise ValueError('Quantity cannot be greater than product quantity')
        self._quantity -= quantity


class Stock:

    def __init__(self) -> None:
        self._inventory: dict[str, list[Batch]] = {}

    def get_batches(self, product_id: str) -> tuple[Batch, ...]:

        # batches = self._inventory[product_id]
        batches = self._inventory.get(product_id,
                                      [])  # esto es equivalente a la línea anterior pero más seguro y ya cumple especificaciones

        return tuple(copy.deepcopy(batch) for batch in batches)

    def add_shipment(self, batch: Batch) -> None:

        """
        b_product_id = batch.product_id

        if b_product_id not in self._inventory:
            self._inventory[b_product_id] = []

        self._inventory[b_product_id].append(batch)
        """

        self._inventory.setdefault(batch.product_id, []).append(batch)

    def total_stock(self, product_id: str) -> int:

        """
        total_sum = 0
        if product_id not in self._inventory:
            return total_sum

        batches_product_id = self._inventory.get(product_id, [])
        for batch in batches_product_id:
            total_sum += batch.get_quantity()

        #return total_sum
        """

        return sum([batch.get_quantity() for batch in self._inventory.get(product_id, [])])

    def _fefo_consume(self,
                      product_id: str, quantity: int)
        -> list[tuple[str, int]]:]

        def sell_e21(self, product_id: str, quantity: int)
            -> None:

        batches = self._inventory.get(product_id, [])
        batches[0].consume(quantity)

    def sell_e22(self, product_id: str, quantity: int)
        -> None:

    batches = self._inventory.get(product_id, [])
    # Obtain the lots ordered by date of expiration (least to greatest)
    batches.sort(key=lambda b: b.expiration_date)
    remaining = quantity

    for batch in batches:
        if remaining < 0:
            break
        available = batch.get_quantity()
        consumed = min(available, remaining)
        remaining -= consumed
        breakdown.append(
            (batch.batch_id, consumed)
        )
    return breakdown


def _remove_empty_batchess(self, product_id: str) ->
    None:


batches = self._inventory.get(product_id, [])
self._inventory = [
    batch for batch in batches if batch.get_quantity() > 0
]


def sell_e23(self, product_id: str, quantity: int)
    -> None:


batches = self._inventory.get(product_id, [])
# Obtain the lots ordered by date of expiration (least to greatest)
batches.sort(key=lambda b: b.expiration_date)
remaining = quantity
for batch in batches:
    if remaining < 0:
        break
    available = batch.get_quantity()
    consumed = min(available, remaining)
    # 2. CONSUME UNITS
    remaining -= consumed
    # Eliminate sold out lots
    self._inventory = [
        b for b in batches if b.get_quantity() > 0
    ]


def sell(self, product_id: str, quantity: int)
    -> None:


total_available = self.total_stock(product_id)
if total_available < quantity:
    raise OutOfStockError(product_id, total_available, quantity)

if __name__ == "__main__":
    product = Product("A-001", "yogur natural", "alimentación")
    print(product)

    batch0 = Batch("B-001", "A-001", 5, 10.0, datetime.date(2026, 2, 17))
    print(batch0)

    my_stock = Stock()
    my_stock.add_shipment(batch0)
