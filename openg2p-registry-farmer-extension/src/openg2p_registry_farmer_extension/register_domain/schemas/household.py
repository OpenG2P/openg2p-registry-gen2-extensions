from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaHousehold(G2PRegisterSchema):

    address: Optional[str] = None
    district: Optional[str] = None
    region: Optional[str] = None
    poverty_score: Optional[float] = None
    poverty_score_type: Optional[str] = None
    household_head: Optional[str] = None


class G2PRegisterHistorySchemaHousehold(G2PRegisterHistorySchema):

    address: Optional[str] = None
    district: Optional[str] = None
    region: Optional[str] = None
    poverty_score: Optional[float] = None
    poverty_score_type: Optional[str] = None
    household_head: Optional[str] = None

