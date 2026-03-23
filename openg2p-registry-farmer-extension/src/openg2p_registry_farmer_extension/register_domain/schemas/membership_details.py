from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import FarmerClusterRoleEnum


class G2PRegisterSchemaMembershipDetails(G2PRegisterBaseSchema):
    """
    Schema for Membership Details register.
    Inherits fields from G2PRegisterBaseSchema.
    link_internal_record_id -> Farmer's internal_record_id
    """
    is_primary_cooperative_member: Optional[bool] = None
    primary_cooperative_name: Optional[str] = None
    is_cooperative_union_member: Optional[bool] = None
    cooperative_union_name: Optional[str] = None
    is_farmer_cluster_member: Optional[bool] = None
    farmer_cluster_role: Optional[FarmerClusterRoleEnum] = None


class G2PRegisterHistorySchemaMembershipDetails(G2PRegisterHistorySchema):
    """
    Schema for Membership Details history.
    Inherits fields from G2PRegisterHistorySchema.
    """
    is_primary_cooperative_member: Optional[bool] = None
    primary_cooperative_name: Optional[str] = None
    is_cooperative_union_member: Optional[bool] = None
    cooperative_union_name: Optional[str] = None
    is_farmer_cluster_member: Optional[bool] = None
    farmer_cluster_role: Optional[FarmerClusterRoleEnum] = None
