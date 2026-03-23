from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema,
    G2PRegisterHistorySchema, G2PGeoHistorySchema, G2PGeoShapeHistorySchema
)
from ..models.enums import LandOwnershipTypeEnum, LandSizeUnitEnum, CurrentLandUseEnum, FarmingTypeEnum


class G2PRegisterSchemaLand(G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema):
    """
    Schema for Land/Farm Details register.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema, and G2PGeoShapeSchema.
    link_internal_record_id -> Farmer's internal_record_id
    """
    land_ownership_type: Optional[LandOwnershipTypeEnum] = None
    certificate_storage_id: Optional[str] = None
    land_size: Optional[str] = None
    land_size_unit: Optional[LandSizeUnitEnum] = None
    soil_fertility: Optional[str] = None
    current_land_use: Optional[CurrentLandUseEnum] = None
    farming_type: Optional[FarmingTypeEnum] = None
    year_of_acquisition: Optional[int] = None
    means_of_acquisition: Optional[str] = None


class G2PRegisterHistorySchemaLand(G2PRegisterHistorySchema, G2PGeoHistorySchema, G2PGeoShapeHistorySchema):
    """
    Schema for Land/Farm Details history.
    Inherits fields from G2PRegisterHistorySchema, G2PGeoHistorySchema, and G2PGeoShapeHistorySchema.
    """
    land_ownership_type: Optional[LandOwnershipTypeEnum] = None
    certificate_storage_id: Optional[str] = None
    land_size: Optional[str] = None
    land_size_unit: Optional[LandSizeUnitEnum] = None
    soil_fertility: Optional[str] = None
    current_land_use: Optional[CurrentLandUseEnum] = None
    farming_type: Optional[FarmingTypeEnum] = None
    year_of_acquisition: Optional[int] = None
    means_of_acquisition: Optional[str] = None
