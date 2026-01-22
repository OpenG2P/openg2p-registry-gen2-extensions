from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema,
    G2PRegisterHistorySchema
)


class G2PRegisterSchemaHouseholdMember(G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema):
    """
    Schema for HouseholdMember register.
    Inherits fields from G2PRegisterBaseSchema, G2PPersonSchema, and G2PGeoSchema.
    """
    # HouseholdMember-specific fields only
    is_disabled: Optional[bool] = None


class G2PRegisterHistorySchemaHouseholdMember(G2PRegisterHistorySchema, G2PPersonSchema, G2PGeoSchema):
    """
    Schema for HouseholdMember history.
    Inherits fields from G2PRegisterHistorySchema, G2PPersonSchema, and G2PGeoSchema.
    """
    # HouseholdMember-specific fields only
    is_disabled: Optional[bool] = None

