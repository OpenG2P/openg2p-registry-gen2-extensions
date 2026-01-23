from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema,
    G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema
)


class G2PRegisterSchemaFarmer(G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema):
    """
    Schema for Farmer register.
    Inherits fields from G2PRegisterBaseSchema, G2PPersonSchema, and G2PGeoSchema.
    """
    # Farmer-specific fields only
    is_disabled: Optional[bool] = None


class G2PRegisterHistorySchemaFarmer(G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema):
    """
    Schema for Farmer history.
    Inherits fields from G2PRegisterHistorySchema, G2PPersonHistorySchema, and G2PGeoHistorySchema.
    """
    # Farmer-specific fields only
    is_disabled: Optional[bool] = None

