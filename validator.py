KEYWORDS = [
    "sales",
    "sale",
    "inventory",
    "stock",
    "promotion",
    "promotions",
    "discount",
    "price",
    "pricing",
    "region",
    "regions",
    "category",
    "categories",
    "product",
    "products",
    "store",
    "stores",
    "forecast",
    "demand",
    "units",
    "weather",
    "season",
    "seasonality",
    "holiday",
    "competitor",
    "order",
    "orders"
]

def is_valid_question(question):
    question = question.lower()
    return any(keyword in question for keyword in KEYWORDS)