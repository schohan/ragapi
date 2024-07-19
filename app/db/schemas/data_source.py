from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

# define source types enums
class DataSourceType(Enum):
    LOCAL_DIR=1
    S3_BUCKET=2
    GCS_BUCKET=3
    AZURE_BUCKET=4
    DROPBOX_DIR=5
    BOX_DIR=6
    
# Base data source model
class DataSourceBase(BaseModel):
    source_type: DataSourceType
    loc: str


class DataSource(DataSourceBase):
    id: str = Field(default_factory=str, alias="_id")
    roles: str = Field(default_factory=str, alias="all")

    