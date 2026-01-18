from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaMachinery(G2PRegisterSchema):

    machinery_type: Optional[str] = None
    count: Optional[int] = None
    equipment_source: Optional[str] = None


class G2PRegisterHistorySchemaMachinery(G2PRegisterHistorySchema):

    machinery_type: Optional[str] = None
    count: Optional[int] = None
    equipment_source: Optional[str] = None

