from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoHistory
from ..services import G2PRegisterDomainServiceHousehold


# All Register classes should have the prefix G2PRegister
class G2PRegisterHousehold(G2PRegister, G2PGeo):
    __tablename__ = "g2p_register_households"

    # Group Details
    household_head: Mapped[str] = mapped_column(String, nullable=True)
    size_of_group: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_children: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_female_members: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_male_members: Mapped[int] = mapped_column(Integer, nullable=True)
    other_land_owner: Mapped[bool] = mapped_column(Boolean, nullable=True)
    # poverty_score and poverty_score_type moved to g2p_register_poverty_scores table

    def get_search_text_fields(self) -> str:
        """Return household fields used to build search_text."""
        return G2PRegisterDomainServiceHousehold().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return household record_name from domain service implementation."""
        return G2PRegisterDomainServiceHousehold().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHousehold(G2PRegisterHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_households"

    household_head: Mapped[str] = mapped_column(String, nullable=True)
    size_of_group: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_children: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_female_members: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_male_members: Mapped[int] = mapped_column(Integer, nullable=True)
    other_land_owner: Mapped[bool] = mapped_column(Boolean, nullable=True)
