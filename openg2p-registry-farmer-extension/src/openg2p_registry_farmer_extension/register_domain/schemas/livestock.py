from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import LivestockSystemEnum


class G2PRegisterSchemaLivestock(G2PRegisterBaseSchema):
    """
    Schema for Livestock register.
    Inherits fields from G2PRegisterBaseSchema.
    link_internal_record_id -> Land's internal_record_id (optional)
    """
    livestock_type: Optional[str] = None
    breed: Optional[str] = None
    head_count: Optional[int] = None
    livestock_system: Optional[LivestockSystemEnum] = None


class G2PRegisterHistorySchemaLivestock(G2PRegisterHistorySchema):
    """
    Schema for Livestock history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    livestock_type: Optional[str] = None
    breed: Optional[str] = None
    head_count: Optional[int] = None
    livestock_system: Optional[LivestockSystemEnum] = None
