from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaMachinery(G2PRegisterBaseSchema):
    """
    Schema for Machinery register.
    Inherits fields from G2PRegisterBaseSchema.
    """
    # Machinery-specific fields only
    machinery_type: Optional[str] = None
    count: Optional[int] = None
    equipment_source: Optional[str] = None


class G2PRegisterHistorySchemaMachinery(G2PRegisterHistorySchema):
    """
    Schema for Machinery history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    # Machinery-specific fields only
    machinery_type: Optional[str] = None
    count: Optional[int] = None
    equipment_source: Optional[str] = None

