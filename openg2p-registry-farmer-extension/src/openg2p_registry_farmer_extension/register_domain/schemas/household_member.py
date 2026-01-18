from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaHouseholdMember(G2PRegisterSchema):

    surname: Optional[str] = None
    given_name: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None
    marital_status: Optional[str] = None
    is_disabled: Optional[bool] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None
    occupation: Optional[str] = None
    income_level: Optional[str] = None
    education_level: Optional[str] = None


class G2PRegisterHistorySchemaHouseholdMember(G2PRegisterHistorySchema):

    surname: Optional[str] = None
    given_name: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None
    marital_status: Optional[str] = None
    is_disabled: Optional[bool] = None
    mobile_number: Optional[str] = None
    email: Optional[str] = None
    occupation: Optional[str] = None
    income_level: Optional[str] = None
    education_level: Optional[str] = None

