
import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)
# Created Date Range 
dates = pd.date_range(
    start="2026-01-01",
    end="2026-12-31",
    freq="D"
)

# Initialyzed data list
analytics_data = []

# generated daily metrices {lopped through each date}
for date in dates:
    visitors = np.random.randint(12000, 18000)
    sessions = visitors + np.random.randint(1000, 5000)
    conversion_rate = round(
        np.random.uniform(3.0, 4.5),
        2
    )
    bounce_rate = round(
        np.random.uniform(35, 50),
        2
    )
    checkout_failures = np.random.randint(10, 40)

    
    # injected march anamoly this is the first investogation scenario 
    if date.month == 3:
        checkout_failures = np.random.randint(180, 300)
        conversion_rate = round(
            np.random.uniform(1.0, 2.0),
            2  
        )
        bounce_rate = round(
            np.random.uniform(55, 70),
            2
        )

    # Injected June App issue
    if date.month == 6:
        bounce_rate = round(
            np.random.uniform(60, 75),
            2
        )
        conversion_rate = round(
            np.random.uniform(2.0, 3.0),
            2
        )

    # Append Record
    analytics_data.append({
    "date": date,
    "visitors": visitors,
    "sessions": sessions,
    "conversion_rate": conversion_rate,
    "bounce_rate": bounce_rate,
    "checkout_failures": checkout_failures
    })

# create dataframe
df = pd.DataFrame(analytics_data)

# save csv
output_dir = Path("data/generated")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "web_analytics.csv"
df.to_csv(output_file, index=False)

# To validate the output 
print(f"Generated: {output_file}")
print("\nMarch Sample:")
print(
    df[df["date"].astype(str).str.startswith("2026-03")]
    .head()
)
