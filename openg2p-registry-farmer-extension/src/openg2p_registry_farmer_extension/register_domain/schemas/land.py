from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema,
    G2PRegisterHistorySchema
)


class G2PRegisterSchemaLand(G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema):
    """
    Schema for Land register.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema, and G2PGeoShapeSchema.
    """
    # Land-specific fields only
    land_tenure: Optional[str] = None
    land_size: Optional[float] = None
    measurement: Optional[str] = None


class G2PRegisterHistorySchemaLand(G2PRegisterHistorySchema, G2PGeoSchema, G2PGeoShapeSchema):
    """
    Schema for Land history.
    Inherits fields from G2PRegisterHistorySchema, G2PGeoSchema, and G2PGeoShapeSchema.
    """
    # Land-specific fields only
    land_tenure: Optional[str] = None
    land_size: Optional[float] = None
    measurement: Optional[str] = None

