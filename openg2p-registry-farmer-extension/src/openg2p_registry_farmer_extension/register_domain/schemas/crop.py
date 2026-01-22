from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaCrop(G2PRegisterBaseSchema):
    """
    Schema for Crop register.
    Inherits fields from G2PRegisterBaseSchema.
    """
    # Crop-specific fields only
    activity_group: Optional[str] = None
    crop_type: Optional[str] = None
    variety: Optional[str] = None
    season: Optional[str] = None
    end_use: Optional[str] = None
    irrigation: Optional[str] = None
    irrigation_water: Optional[str] = None
    fertilizer_type: Optional[str] = None


class G2PRegisterHistorySchemaCrop(G2PRegisterHistorySchema):
    """
    Schema for Crop history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    # Crop-specific fields only
    activity_group: Optional[str] = None
    crop_type: Optional[str] = None
    variety: Optional[str] = None
    season: Optional[str] = None
    end_use: Optional[str] = None
    irrigation: Optional[str] = None
    irrigation_water: Optional[str] = None
    fertilizer_type: Optional[str] = None

