from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaLivestock(G2PRegisterSchema):

    livestock_type: Optional[str] = None
    count: Optional[int] = None
    livestock_system: Optional[str] = None


class G2PRegisterHistorySchemaLivestock(G2PRegisterHistorySchema):

    livestock_type: Optional[str] = None
    count: Optional[int] = None
    livestock_system: Optional[str] = None

