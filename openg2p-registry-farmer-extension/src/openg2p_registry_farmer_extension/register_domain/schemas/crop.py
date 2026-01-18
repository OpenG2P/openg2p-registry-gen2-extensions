from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaCrop(G2PRegisterSchema):

    activity_group: Optional[str] = None
    crop_type: Optional[str] = None
    variety: Optional[str] = None
    season: Optional[str] = None
    end_use: Optional[str] = None
    irrigation: Optional[str] = None
    irrigation_water: Optional[str] = None
    fertilizer_type: Optional[str] = None


class G2PRegisterHistorySchemaCrop(G2PRegisterHistorySchema):

    activity_group: Optional[str] = None
    crop_type: Optional[str] = None
    variety: Optional[str] = None
    season: Optional[str] = None
    end_use: Optional[str] = None
    irrigation: Optional[str] = None
    irrigation_water: Optional[str] = None
    fertilizer_type: Optional[str] = None

