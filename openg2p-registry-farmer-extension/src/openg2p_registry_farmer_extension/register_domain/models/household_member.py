from sqlalchemy import String, Boolean, Date, Float
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory, G2PPerson, G2PGeo



# All Register classes should have the prefix G2PRegister
class G2PRegisterHouseholdMember(G2PRegister, G2PPerson, G2PGeo):
    __tablename__ = "g2p_register_household_members"
        

    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return household member-specific fields for search text aggregation.
        G2PRegister, G2PPerson, and G2PGeo fields are automatically included via event listeners.
        """
        return [
            str(self.is_disabled) if self.is_disabled is not None else "",
        ]


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHouseholdMember(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_household_members"

    # G2PPerson fields for history
    foundational_id: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    middle_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    given_name: Mapped[str] = mapped_column(String, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    birth_date: Mapped[str] = mapped_column(Date, nullable=True)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)
    email_address: Mapped[str] = mapped_column(String, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
    occupation: Mapped[str] = mapped_column(String, nullable=True)
    income_level: Mapped[str] = mapped_column(String, nullable=True)
    language_code: Mapped[str] = mapped_column(String, nullable=True)
    education_level: Mapped[str] = mapped_column(String, nullable=True)
    registration_date: Mapped[str] = mapped_column(Date, nullable=True)

    # G2PGeo fields for history
    latitude: Mapped[float] = mapped_column(Float, nullable=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=True)
    altitude: Mapped[float] = mapped_column(Float, nullable=True)
    plus_code: Mapped[str] = mapped_column(String, nullable=True)
    postal_code: Mapped[str] = mapped_column(String, nullable=True)
    country_code: Mapped[str] = mapped_column(String, nullable=True)
    geo_lowest_level_value_id: Mapped[str] = mapped_column(String, nullable=True)
    geo_code_hierarchy_json: Mapped[str] = mapped_column(JSONB, nullable=True)

    # HouseholdMember-specific fields for history
    surname: Mapped[str] = mapped_column(String, nullable=True)
    prefix: Mapped[str] = mapped_column(String, nullable=True)
    suffix: Mapped[str] = mapped_column(String, nullable=True)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)