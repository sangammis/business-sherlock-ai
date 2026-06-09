import pandas as pd
import numpy as np
from pathlib import Path
from faker import Faker

fake = Faker()
np.random.seed(42)

# load analytics data
analytics = pd.read_csv("data/generated/web_analytics.csv")
analytics["date"] = pd.to_datetime(analytics["date"])

# define categories
categories = [
    "Electronics",
    "Fashion",
    "Home",
    "Books",
    "Store"
]

# define region
regions = [
    "North",
    "South",
    "East",
    "West"
]

# initialze sales list
sales_records= []

# loop through daily analytics 
order_counter = 1
for _, row in analytics.iterrows():

    daily_orders = int(
        row["visitors"] *
        (row["conversion_rate"] / 100) * 0.25
    )

    # create orders
    for _ in range(daily_orders):

        revenue = round(
            np.random.uniform(20, 500),
            2
        )

        if row["date"].month == 3:
            payment_status = np.random.choice(
                ["Success", "Failed"],
                p=[0.82, 0.18]
            )
        else:
            payment_status = np.random.choice(
                ["Success", "Failed"],
                p=[0.98, 0.02]
            )

        shipping_status = np.random.choice(
            ["Delivered", "In Transit"],
            p=[0.9, 0.1]
        )

        sales_records.append({
            "order_id": f"O{order_counter}",
            "customer_id": f"C{np.random.randint(1,100001)}",
            "order_date": row["date"],
            "region": np.random.choice(regions),
            "category": np.random.choice(categories),
            "revenue": revenue,
            "payment_status": payment_status,
            "shipping_status": shipping_status
        })

        order_counter += 1

sales_df = pd.DataFrame(sales_records)

# revenue adjustment : falied payments should not count
sales_df.loc[
    sales_df["payment_status"] == "Failed",
    "revenue"
] = 0

# save the file
output_file = (
    Path("data/generated")
    / "sales_data.csv"
)
sales_df.to_csv(
    output_file,
    index=False
)

# validation 
print(f"Generated: {output_file}")

print(
    f"Total Orders: {len(sales_df):,}"
)

# monthly revenue check 
sales_df["month"] = pd.to_datetime(
    sales_df["order_date"]
).dt.to_period("M")

monthly = (
    sales_df.groupby("month")["revenue"]
    .sum()
    .reset_index()
)

print(monthly)