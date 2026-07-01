from pydantic import BaseModel

class HouseData(BaseModel):
    OverallQual: int
    GrLivArea: float
    GarageCars: int
    GarageArea: float
    TotalBsmtSF: float
    FullBath: int
    YearBuilt: int
    YearRemodAdd: int
    LotArea: float
    BedroomAbvGr: int