from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema,
    G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema
)
from ..models.enums import DisabilityTypeEnum, DisabilitySeverityEnum, SourceOfIncomeEnum


class G2PRegisterSchemaFarmer(G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema):
    """
    Schema for Farmer register.
    Inherits fields from G2PRegisterBaseSchema, G2PPersonSchema, and G2PGeoSchema.
    """
    estimated_age: Optional[int] = None
    has_personal_phone: Optional[bool] = None
    is_disabled: Optional[bool] = None
    disability_type: Optional[DisabilityTypeEnum] = None
    disability_severity: Optional[DisabilitySeverityEnum] = None
    source_of_income: Optional[SourceOfIncomeEnum] = None
    source_of_income_other: Optional[str] = None
    language_spoken: Optional[str] = None
    national_id_masked: Optional[str] = None


class G2PRegisterHistorySchemaFarmer(G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema):
    """
    Schema for Farmer history.
    Inherits fields from G2PRegisterHistorySchema, G2PPersonHistorySchema, and G2PGeoHistorySchema.
    """
    estimated_age: Optional[int] = None
    has_personal_phone: Optional[bool] = None
    is_disabled: Optional[bool] = None
    disability_type: Optional[DisabilityTypeEnum] = None
    disability_severity: Optional[DisabilitySeverityEnum] = None
    source_of_income: Optional[SourceOfIncomeEnum] = None
    source_of_income_other: Optional[str] = None
    language_spoken: Optional[str] = None
    national_id_masked: Optional[str] = None
