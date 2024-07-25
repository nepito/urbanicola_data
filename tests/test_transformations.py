import pandas as pd
import urbanicola_data as dt


all_sales = pd.read_csv("/workdir/tests/data/venta.csv")


def test_sales() -> None:
    row: dict = all_sales.to_dict("records")[1]
    new_row: dict = {k: [v] for k, v in row.items()}
    dt.Sales(**new_row)