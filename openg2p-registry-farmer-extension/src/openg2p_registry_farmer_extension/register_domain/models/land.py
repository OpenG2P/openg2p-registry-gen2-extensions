from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoShape,
    G2PGeoHistory, G2PGeoShapeHistory
)
from .enums import LandOwnershipTypeEnum, LandSizeUnitEnum, CurrentLandUseEnum, FarmingTypeEnum


# All Register classes should have the prefix G2PRegister
class G2PRegisterLand(G2PRegister, G2PGeo, G2PGeoShape):
    __tablename__ = "g2p_register_lands"

    # link_internal_record_id -> Farmer's internal_record_id
    land_ownership_type: Mapped[LandOwnershipTypeEnum] = mapped_column(String, nullable=True)   # LandOwnershipTypeEnum
    certificate_storage_id: Mapped[str] = mapped_column(Text, nullable=True)
    land_size: Mapped[str] = mapped_column(String, nullable=True)
    unit: Mapped[LandSizeUnitEnum] = mapped_column(String, nullable=True)        # LandSizeUnitEnum
    soil_fertility: Mapped[str] = mapped_column(String, nullable=True)
    current_land_use: Mapped[CurrentLandUseEnum] = mapped_column(String, nullable=True)      # CurrentLandUseEnum
    farming_type: Mapped[FarmingTypeEnum] = mapped_column(String, nullable=True)          # FarmingTypeEnum
    year_of_acquisition: Mapped[int] = mapped_column(Integer, nullable=True)
    means_of_acquisition: Mapped[str] = mapped_column(String, nullable=True)  # Attribute lookup


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLand(G2PRegisterHistory, G2PGeoHistory, G2PGeoShapeHistory):
    __tablename__ = "g2p_register_history_lands"

    land_ownership_type: Mapped[str] = mapped_column(String, nullable=True)
    certificate_storage_id: Mapped[str] = mapped_column(Text, nullable=True)
    land_size: Mapped[str] = mapped_column(String, nullable=True)
    unit: Mapped[str] = mapped_column(String, nullable=True)
    soil_fertility: Mapped[str] = mapped_column(String, nullable=True)
    current_land_use: Mapped[str] = mapped_column(String, nullable=True)
    farming_type: Mapped[str] = mapped_column(String, nullable=True)
    year_of_acquisition: Mapped[int] = mapped_column(Integer, nullable=True)
    means_of_acquisition: Mapped[str] = mapped_column(String, nullable=True)
