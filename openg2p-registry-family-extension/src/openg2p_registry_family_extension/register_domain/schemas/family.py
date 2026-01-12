from pydantic import BaseModel
from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaFamily(G2PRegisterSchema):

    ethnic_group: Optional[str] = None
    belong_to_protected_groups: Optional[bool] = None
    under_other_vulnerable_status: Optional[bool] = None

class G2PRegisterHistorySchemaFamily(G2PRegisterHistorySchema):
    
    ethnic_group: Optional[str] = None
    belong_to_protected_groups: Optional[bool] = None
    under_other_vulnerable_status: Optional[bool] = None