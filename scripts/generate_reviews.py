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

# normal reviews
positive_reviews = [
    "Great product and fast delivery",
    "Excellent shopping experience",
    "Easy checkout process",
    "Received order on time",
    "Good quality product",
    "Very satisfied with my purchase",
    "Customer service was helpful",
    "Will buy again from this store"
]

# march reviews 
payment_reviews = [
    "Payment keeps failing during checkout",
    "Could not complete my purchase",
    "Checkout page froze multiple times",
    "Card was charged but order failed",
    "Transaction failed repeatedly",
    "Unable to place order after payment"
]

# June rewiews 
app_reviews = [
    "App crashes after the latest update",
    "Cannot login anymore",
    "Application keeps closing",
    "Mobile app performance is terrible",
    "App became unusable after update",
    "Experiencing constant crashes"
]

# september reviews
shipping_reviews = [
    "Delivery took much longer than expected",
    "Package arrived very late",
    "Tracking information never updated",
    "Order was delayed significantly",
    "Shipping experience was disappointing",
    "Still waiting for my package"
]

# initialize records
review_records = []
review_counter = 1

for date in dates:
    daily_reviews = np.random.randint(15,25)
    ## increase reviews during incident
    # march
    if date.month == 3:
        daily_reviews = np.random.randint(35,55)
    # june
    elif date.month == 6:
        daily_reviews = np.random.randint(30,50)
    # september 
    elif date.month == 9:
        daily_reviews = np.random.randint(30,50)
    
    for _ in range(daily_reviews):
        if date.month == 3:
            review_text = np.random.choice(payment_reviews)
            rating = np.random.choice([1,2],p=[0.7,0.3])
            source_event = "Payment Gateway Upgrade"
        
        elif date.month == 6:
            review_text = np.random.choice(app_reviews)
            rating = np.random.choice([1,2],p=[0.7,0.3])
            source_event = "Mobile App Release"

        elif date.month == 9:
            review_text = np.random.choice(shipping_reviews)
            rating = np.random.choice([1,2,3],p=[0.5,0.3,0.2])
            source_event = "Shipping Migration"
        else:
            review_text = np.random.choice(positive_reviews)
            rating = np.random.choice([4,5],p=[0.4,0.6])
            source_event = "Normal Operations"
        review_records.append({
            "review_id": f"R{review_counter}",
            "customer_id": f"C{np.random.randint(1,100001)}",
            "date": date,
            "rating": rating,
            "review_text": review_text,
            "source_event": source_event
        })
        review_counter += 1

reviews_df = pd.DataFrame(review_records)

output_file = (Path("data/generated")/ "customer_reviews.csv")
reviews_df.to_csv(output_file, index=False)

# validation
print(f"Generated: {output_file}")
print(f"Total Reviews: {len(reviews_df):,}")

#  monthly review count
reviews_df["month"] = pd.to_datetime(reviews_df["date"]).dt.to_period("M")
monthly = (reviews_df.groupby("month").size().reset_index(name="review_count"))
print(monthly)

print(
    reviews_df[
        reviews_df["date"].astype(str)
        .str.startswith("2026-03")
    ][[
        "rating",
        "review_text",
        "source_event"
    ]].head(10)
)
    
