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
    household_head: Optional[str] = None
    group_size: Optional[int] = None
    num_children: Optional[int] = None
    num_female_members: Optional[int] = None
    num_male_members: Optional[int] = None
    other_land_owner: Optional[bool] = None


class G2PRegisterHistorySchemaHousehold(G2PRegisterHistorySchema, G2PGeoHistorySchema):
    """
    Schema for Household history.
    Inherits fields from G2PRegisterHistorySchema and G2PGeoHistorySchema.
    """
    household_head: Optional[str] = None
    group_size: Optional[int] = None
    num_children: Optional[int] = None
    num_female_members: Optional[int] = None
    num_male_members: Optional[int] = None
    other_land_owner: Optional[bool] = None
