from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import CropEndUseEnum


class G2PRegisterSchemaCrop(G2PRegisterBaseSchema):
    """
    Schema for Crop register.
    Inherits fields from G2PRegisterBaseSchema.
    link_internal_record_id -> Land's internal_record_id (optional)
    """
    commodity: Optional[str] = None
    planted_date: Optional[date] = None
    season: Optional[str] = None
    end_use: Optional[CropEndUseEnum] = None


class G2PRegisterHistorySchemaCrop(G2PRegisterHistorySchema):
    """
    Schema for Crop history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    commodity: Optional[str] = None
    planted_date: Optional[date] = None
    season: Optional[str] = None
    end_use: Optional[CropEndUseEnum] = None
