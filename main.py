import statistics
import json
import csv
import re

from urllib.request import urlopen


def parse_html(page):
    url = f"https://24h.pchome.com.tw/store/DSAA31?p={page}"
    with urlopen(url) as response:
        html = response.read().decode("utf-8")

    return html


def parse_products(html):
    key = 'initProdList\\":'
    start = html.find(key)
    if start == -1:
        return []

    array_start = html.find("[", start)
    if array_start == -1:
        return []

    depth = 0
    in_string = False
    escaped = False

    for i in range(array_start, len(html)):
        char = html[i]

        if escaped:
            escaped = False
            continue

        if char == "\\":
            escaped = True
            continue

        if char == '"':
            in_string = not in_string
            continue

        if in_string:
            continue

        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                product_list_block = html[array_start : i + 1]
                product_list_json = product_list_block.replace('\\"', '"')
                products = json.loads(product_list_json)
                return [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "describe": product.get("describe", ""),
                        "reviewCount": product["reviewCount"],
                        "ratingValue": product["ratingValue"],
                        "price": product["price"],
                    }
                    for product in products
                ]

    return []


def calculate_z_score(price, average_price, standard_deviation):
    return (price - average_price) / standard_deviation


page = 1
all_products = []
best_products = []
while True:
    products = parse_products(parse_html(page))
    if not products:
        break

    for product in products:
        all_products.append(product)
        if (
            product["ratingValue"] is not None
            and product["reviewCount"] is not None
        ):
            if (
                float(product["ratingValue"]) > 4.9
                and int(product["reviewCount"]) >= 1
            ):
                best_products.append(product["id"])
    page += 1

# Task 1
with open("products.txt", "w", encoding="utf-8") as f:
    for product in all_products:
        f.write(product["id"] + "\n")

# Task 2
with open("best-products.txt", "w", encoding="utf-8") as f:
    for product in best_products:
        f.write(product + "\n")

# Task 3
intel_i5_products = [
    product
    for product in all_products
    if re.search(r"(?<!\w)i5(?!\w)", product["name"], re.IGNORECASE)
    or re.search(r"(?<!\w)i5(?!\w)", product["describe"], re.IGNORECASE)
]
average_price = statistics.mean(
    product["price"] for product in intel_i5_products
)
print(average_price)

# Task 4
standard_deviation = statistics.pstdev(
    product["price"] for product in all_products
)
with open("standardization.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for product in all_products:
        writer.writerow(
            [
                product["id"],
                product["price"],
                calculate_z_score(
                    product["price"], average_price, standard_deviation
                ),
            ]
        )
