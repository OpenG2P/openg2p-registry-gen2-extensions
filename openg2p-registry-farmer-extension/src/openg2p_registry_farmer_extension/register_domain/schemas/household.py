from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PGeoSchema,
    G2PRegisterHistorySchema, G2PGeoHistorySchema
)


class G2PRegisterSchemaHousehold(G2PRegisterBaseSchema, G2PGeoSchema):
    """
    Schema for Household register.
    Inherits fields from G2PRegisterBaseSchema and G2PGeoSchema.
    """
    # Household-specific fields only
    poverty_score: Optional[str] = None
    poverty_score_type: Optional[str] = None
    household_head: Optional[str] = None


class G2PRegisterHistorySchemaHousehold(G2PRegisterHistorySchema, G2PGeoHistorySchema):
    """
    Schema for Household history.
    Inherits fields from G2PRegisterHistorySchema and G2PGeoHistorySchema.
    """
    # Household-specific fields only
    poverty_score: Optional[str] = None
    poverty_score_type: Optional[str] = None
    household_head: Optional[str] = None

