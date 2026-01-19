from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaFarmer(G2PRegisterSchema):

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    is_disabled: Optional[bool] = None
    address: Optional[str] = None
    district: Optional[str] = None
    region: Optional[str] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None


class G2PRegisterHistorySchemaFarmer(G2PRegisterHistorySchema):

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    is_disabled: Optional[bool] = None
    address: Optional[str] = None
    district: Optional[str] = None
    region: Optional[str] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None

