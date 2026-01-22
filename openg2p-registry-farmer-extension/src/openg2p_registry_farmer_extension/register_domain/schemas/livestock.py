from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaLivestock(G2PRegisterBaseSchema):
    """
    Schema for Livestock register.
    Inherits fields from G2PRegisterBaseSchema.
    """
    # Livestock-specific fields only
    livestock_type: Optional[str] = None
    count: Optional[int] = None
    livestock_system: Optional[str] = None


class G2PRegisterHistorySchemaLivestock(G2PRegisterHistorySchema):
    """
    Schema for Livestock history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    # Livestock-specific fields only
    livestock_type: Optional[str] = None
    count: Optional[int] = None
    livestock_system: Optional[str] = None

