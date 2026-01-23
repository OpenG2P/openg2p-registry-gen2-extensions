from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema,
    G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema
)


class G2PRegisterSchemaHouseholdMember(G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema):
    """
    Schema for HouseholdMember register.
    Inherits fields from G2PRegisterBaseSchema, G2PPersonSchema, and G2PGeoSchema.
    """
    # HouseholdMember-specific fields only
    is_disabled: Optional[bool] = None


class G2PRegisterHistorySchemaHouseholdMember(G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema):
    """
    Schema for HouseholdMember history.
    Inherits fields from G2PRegisterHistorySchema, G2PPersonHistorySchema, and G2PGeoHistorySchema.
    """
    # HouseholdMember-specific fields only
    is_disabled: Optional[bool] = None

