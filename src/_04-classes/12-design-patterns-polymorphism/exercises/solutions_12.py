class VipDiscount:
    def apply(self, price: float) -> float:
        return price * 0.7


def build_discount(kind: str):
    if kind == "vip":
        return VipDiscount()
    raise ValueError("Nieznany typ zniżki")
