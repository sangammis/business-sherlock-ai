import pandas as pd
from pathlib import Path

# Event Data 

events = [
    {
        "event_id": "EV001",
        "date": "2026-03-01",
        "event_type": "Payment Gateway Upgrade",
        "description": "Payment gateway upgraded to version 2.0"
    },
    {
        "event_id": "EV002",
        "date": "2026-06-01",
        "event_type": "Mobile App Release",
        "description": "Mobile application version 3.2 released"
    },
    {
        "event_id": "EV003",
        "date": "2026-09-01",
        "event_type": "Shipping Provider Migration",
        "description": "Migrated logistics operations to a new shipping partner"
    }
]
# Convert to dataframe
df = pd.DataFrame(events)

# output directory
output_dir = Path("data/generated")
output_dir.mkdir(parents=True, exist_ok=True)

# save csv
output_file = output_dir / "product_events.csv"
df.to_csv(output_file, index = False)

# added success message
print(f"Generate : {output_file}")
print(df)

