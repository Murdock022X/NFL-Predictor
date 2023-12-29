import pandas as pd
from pathlib import Path

DataPath = Path(__file__).parent / Path("FootballData")

TemplatedFilename = "{}-data.csv"

class FootballData:

    def __init__(self, year: int):
        self.year = year

        data_path = DataPath / Path(TemplatedFilename.format(year))

        self.data = pd.read_csv(data_path)
