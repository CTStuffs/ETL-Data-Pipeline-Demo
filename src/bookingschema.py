import pandera.pandas as pa
import pandas as pd

from pandera.typing import Series


class BookingSchema(pa.DataFrameModel):
    booking_id: Series[str]

    guest_name: Series[str]

    email: Series[str] = pa.Field(
        str_matches=r"^[^@]+@[^@]+\.[^@]+$"
    )

    listing_id: Series[int]

    listing_city: Series[str]

    checkin_date: Series[pd.DatetimeTZDtype]
    checkout_date: Series[pd.DatetimeTZDtype]

    nights: Series[int] = pa.Field(ge=1)

    price_per_night: Series[float] = pa.Field(ge=0)

    total_price: Series[float] = pa.Field(ge=0)

    payment_status: Series[str] = pa.Field(
        isin=[
            "PENDING",
            "PAID",
        ]
    )

    review_score: Series[float] = pa.Field(
        ge=0,
        le=6,
        nullable=True,
    )

    is_cancelled: Series[bool]
