from pydantic import BaseModel
from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaFamily(G2PRegisterSchema):

    type_of_housing: Optional[str] = None
    house_condition: Optional[str] = None
    sanitation_condition: Optional[str] = None
    water_access: Optional[str] = None
    electricity_access: Optional[str] = None

    ethnic_group: Optional[str] = None
    belong_to_protected_groups: Optional[bool] = None
    under_other_vulnerable_status: Optional[bool] = None

class G2PRegisterHistorySchemaFamily(G2PRegisterHistorySchema):

    type_of_housing: Optional[str] = None
    house_condition: Optional[str] = None
    sanitation_condition: Optional[str] = None
    water_access: Optional[str] = None
    electricity_access: Optional[str] = None
    
    ethnic_group: Optional[str] = None
    belong_to_protected_groups: Optional[bool] = None
    under_other_vulnerable_status: Optional[bool] = None