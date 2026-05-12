import pandas as pd
from word2number import w2n


def convert_cancelled(x):
    if x == "YES" or x == "Y":
        return "TRUE"
    elif x == "NO" or x == "N":
        return "FALSE"
    else:
        return x

def convert_words(x):
    try:
        return w2n.word_to_num(str(x))
    except:
        return x


def clean_data(df):
    # remove duplicate rows
    df = df.drop_duplicates()

    # remove rows with blanks
    df = df.dropna()

    # convert listingid to ints
    df["listing_id"] = df["listing_id"].astype(int)

    timeformat = "%Y-%m-%d"

    # standardize checkin and checkout datetime
    df["checkin_date"] = pd.to_datetime(df["checkin_date"], errors="coerce")
    df["checkin_date"] = df["checkin_date"].dt.strftime(timeformat)
    df = df[df['checkin_date'].notna()]

    df["checkout_date"] = pd.to_datetime(df["checkout_date"], errors="coerce")
    df["checkout_date"] = df["checkout_date"].dt.strftime(timeformat)
    df = df[df['checkout_date'].notna()]

    # convert letter nums to ints and filter out non numeric values
    df["nights"] = df["nights"].apply(convert_words)
    df["nights"] = pd.to_numeric(df["nights"])
    df = df[df["nights"] > 0]


    # replace free values with 0
    df["price_per_night"] = df["price_per_night"].replace("free", 0)

    # remove all non numeric values from price per night
    df = df[
        pd.to_numeric(df["price_per_night"], errors="coerce").notna()
    ]


    # remove all non numeric values
    df = df[
        pd.to_numeric(df["total_price"], errors="coerce").notna()
    ]

    # remove all non numeric values
    df = df[
        pd.to_numeric(df["review_score"], errors="coerce").notna()
    ]

    # filter negative numbers from review score
    df = df[df["review_score"] > 0]

    # convert payment status to uppercase
    df['payment_status'] = df['payment_status'].str.upper()

    # convert is_cancelled to boolean
    df['is_cancelled'] = df['is_cancelled'].str.upper()
    df["is_cancelled"] = df["is_cancelled"].apply(convert_cancelled)
    df["is_cancelled"] = df["is_cancelled"].map({
        "TRUE": True,
        "FALSE": False
    })

def save_clean_data(df, file_path):
    df.to_csv(file_path, index=False)