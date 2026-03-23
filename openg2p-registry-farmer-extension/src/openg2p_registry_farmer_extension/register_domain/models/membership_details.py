from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceMembershipDetails
from .enums import FarmerClusterRoleEnum


# All Register classes should have the prefix G2PRegister
class G2PRegisterMembershipDetails(G2PRegister):
    __tablename__ = "g2p_register_membership_details"

    # link_internal_record_id -> Farmer's internal_record_id
    is_primary_cooperative_member: Mapped[bool] = mapped_column(Boolean, nullable=True)
    primary_cooperative_name: Mapped[str] = mapped_column(String, nullable=True)
    is_cooperative_union_member: Mapped[bool] = mapped_column(Boolean, nullable=True)
    cooperative_union_name: Mapped[str] = mapped_column(String, nullable=True)
    is_farmer_cluster_member: Mapped[bool] = mapped_column(Boolean, nullable=True)
    farmer_cluster_role: Mapped[FarmerClusterRoleEnum] = mapped_column(String, nullable=True)   # FarmerClusterRoleEnum

    def get_search_text_fields(self) -> str:
        """Return membership details fields used to build search_text."""
        return G2PRegisterDomainServiceMembershipDetails().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return membership details record_name from domain service implementation."""
        return G2PRegisterDomainServiceMembershipDetails().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryMembershipDetails(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_membership_details"

    is_primary_cooperative_member: Mapped[bool] = mapped_column(Boolean, nullable=True)
    primary_cooperative_name: Mapped[str] = mapped_column(String, nullable=True)
    is_cooperative_union_member: Mapped[bool] = mapped_column(Boolean, nullable=True)
    cooperative_union_name: Mapped[str] = mapped_column(String, nullable=True)
    is_farmer_cluster_member: Mapped[bool] = mapped_column(Boolean, nullable=True)
    farmer_cluster_role: Mapped[str] = mapped_column(String, nullable=True)
