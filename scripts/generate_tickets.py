import pandas as pd
import numpy as np
from pathlib import Path
from faker import Faker

fake = Faker()

np.random.seed(42)

# create date range
dates = pd.date_range(
    start="2026-01-01",
    end="2026-12-31",
    freq="D"
)

# normal issues
normal_issues = [
    "Refund Request",
    "Order Tracking",
    "Product Inquiry",
    "Return Request",
    "Account Question"
]

# march issue
payment_issues = [
    "Payment Failure",
    "Checkout Error",
    "Transaction Failed"
]

# june issue
app_issues = [
    "App Crash",
    "Login Problem",
    "Performance Issue"
]

# september issue
shipping_issues = [
    "Late Delivery",
    "Package Missing",
    "Tracking Issue"
]

# description templates
descriptions = {
    "Payment Failure": [
        "Payment failed during checkout",
        "Card charged but order not placed",
        "Unable to complete transaction"
    ],

    "Checkout Error": [
        "Checkout page froze",
        "Checkout process failed",
        "Order could not be completed"
    ],

    "Transaction Failed": [
        "Transaction declined unexpectedly",
        "Payment processing error",
        "Purchase failed"
    ],

    "App Crash": [
        "Application crashes after update",
        "App closes unexpectedly",
        "Unable to use mobile app"
    ],

    "Login Problem": [
        "Cannot login after update",
        "Authentication issue",
        "Login keeps failing"
    ],

    "Performance Issue": [
        "App is very slow",
        "Screen takes too long to load",
        "Performance degraded"
    ],

    "Late Delivery": [
        "Order delayed",
        "Package arrived very late",
        "Delivery took too long"
    ],

    "Package Missing": [
        "Package never arrived",
        "Shipment lost",
        "Order missing"
    ],

    "Tracking Issue": [
        "Tracking information unavailable",
        "Tracking not updating",
        "Cannot locate shipment"
    ],
    "Refund Request": [
    "Customer requested refund",
    "Refund not processed",
    "Requesting refund for recent purchase"
    ],

    "Order Tracking": [
    "Need tracking information",
    "Unable to track order",
    "Order status not updated"
    ],

    "Product Inquiry": [
    "Question about product specifications",
    "Need more product information",
    "Inquiry regarding product availability"
    ],

    "Return Request": [
    "Customer wants to return product",
    "Return process inquiry",
    "Need assistance with return"
    ],

    "Account Question": [
    "Question regarding account settings",
    "Unable to update account information",
    "Account related inquiry"
    ]
}

# initialize records
ticket_records = []
ticket_counter = 1

# generate daily tickets 
for date in dates:
    daily_tickets = np.random.randint(8,15)
    # march spike
    if date.month == 3:
        daily_tickets = np.random.randint(25,40)
    # june spike
    if date.month == 6:
        daily_tickets = np.random.randint(20,35)
    # september spike
    if date.month == 9:
        daily_tickets = np.random.randint(20,35)

    source_event = "Normal Operations"
    if date.month == 3:
        source_event = "Payment Gateway Upgrade"

    elif date.month == 6:
        source_event = "Mobile App Release"

    elif date.month == 9:
        source_event = "Shipping Migration"
    
    for _ in range(daily_tickets):
        if date.month == 3:
            issue_type = np.random.choice(
                payment_issues
        )  
        elif date.month == 6:
            issue_type = np.random.choice(
                app_issues
        )
        elif date.month == 9:
            issue_type = np.random.choice(
                shipping_issues
        )     
        else:
            issue_type = np.random.choice(
                normal_issues
        )
        
        description = np.random.choice(
        descriptions.get(
        issue_type,
        ["General customer inquiry"]
        )
        )
        ticket_records.append({
            "ticket_id": f"T{ticket_counter}",
            "customer_id": f"C{np.random.randint(1,100001)}",
            "date": date,
            "issue_type": issue_type,
            "priority": np.random.choice(
                ["Low","Medium","High"],
                p=[0.4,0.4,0.2]
            ),
            "description": description,
            "source_event" : source_event
        })
        ticket_counter += 1

tickets_df = pd.DataFrame(
    ticket_records
)
# save csv
output_file = (
    Path("data/generated")
    / "support_tickets.csv"
)

tickets_df.to_csv(
    output_file,
    index=False
)
    
# validation
print(
    f"Generated: {output_file}"
)
print(
    f"Total Tickets: {len(tickets_df):,}"
)

# monthly counts
tickets_df["month"] = pd.to_datetime(
    tickets_df["date"]
).dt.to_period("M")
monthly = (
    tickets_df.groupby("month")
    .size()
    .reset_index(name="ticket_count")
)
print(monthly)

# print(tickets_df.head())
print(
    tickets_df[
        tickets_df["date"].astype(str).str.startswith("2026-03")
    ][["issue_type","description","source_event"]]
    .head(10)
)