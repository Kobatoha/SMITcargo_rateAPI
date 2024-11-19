import json
from datetime import datetime
from sqlalchemy.orm import Session
from models import InsuranceRate


def load_rates_from_json(file_path: str, db: Session):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for data_str, rates in data.items():
        date_obj = datetime.strptime(data_str, "%Y-%m-%d").date()
        for rate in rates:
            db_rate = InsuranceRate(
                date=date_obj,
                cargo_type=rate["cargo_type"],
                rate=float(rate['rate'])
            )
            db.add(db_rate)
    db.commit()
