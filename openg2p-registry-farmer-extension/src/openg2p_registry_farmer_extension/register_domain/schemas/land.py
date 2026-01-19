from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaLand(G2PRegisterSchema):

    location: Optional[str] = None
    land_tenure: Optional[str] = None
    land_size: Optional[float] = None
    measurement: Optional[str] = None


class G2PRegisterHistorySchemaLand(G2PRegisterHistorySchema):

    location: Optional[str] = None
    land_tenure: Optional[str] = None
    land_size: Optional[float] = None
    measurement: Optional[str] = None

