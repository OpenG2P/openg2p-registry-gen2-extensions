from sqlalchemy import String, Boolean, DateTime, Date, Float
from sqlalchemy.orm import Mapped, mapped_column, validates
from sqlalchemy.dialects.postgresql import JSONB
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel
from datetime import datetime, date


# All Register classes should have the prefix G2PRegister
class G2PRegisterHouseholdMember(G2PRegister):
    __tablename__ = "g2p_register_household_members"
        
    # internal_record_id
    # functional_record_id -> NONE
    # foundational_id -> national_id
    # link_foundational_id -> NONE
    # link_internal_record_id -> household's internal_record_id
    # master_register_id -> household register_id

    # DCI fields
    # identifier_type: Mapped[str] = mapped_column(String, nullable=True)
    # identifier_value: Mapped[str] = mapped_column(String, nullable=True)
    surname: Mapped[str] = mapped_column(String, nullable=True)
    given_name: Mapped[str] = mapped_column(String, nullable=True)
    prefix: Mapped[str] = mapped_column(String, nullable=True)
    suffix: Mapped[str] = mapped_column(String, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    date_of_birth: Mapped[str] = mapped_column(Date, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    occupation: Mapped[str] = mapped_column(String, nullable=True)
    income_level: Mapped[str] = mapped_column(String, nullable=True)
    education_level: Mapped[str] = mapped_column(String, nullable=True)

    @validates('foundational_id', 'surname', 'given_name', 'prefix', 'suffix', 'date_of_birth', 'gender', 'mobile_number', 'email', 'marital_status', 'occupation', 'income_level', 'education_level', 'is_disabled')
    def update_search_text(self, _key: str, value: str) -> str:
        """
        Automatically update search_text whenever any searchable field is modified.
        Combines all searchable fields into a single text for trigram search.
        """
        self._populate_search_text()
        return value

    def _populate_search_text(self) -> None:
        """
        Populate search_text by combining all searchable family member fields.
        """
        searchable_fields: list[str] = [
            self.foundational_id or "",
            self.surname or "",
            self.given_name or "",
            self.prefix or "",
            self.suffix or "",
            str(self.date_of_birth) if self.date_of_birth else "",
            self.gender or "",
            self.mobile_number or "",
            self.email or "",
            self.marital_status or "",
            self.occupation or "",
            self.income_level or "",
            self.education_level or "",
            str(self.is_disabled) if self.is_disabled is not None else ""
        ]
        self.search_text = " ".join(searchable_fields).strip()

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHouseholdMember(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_household_members"

    # Override all columns from G2PRegisterHouseholdMemberBase to make them nullable for history
    # identifier_type: Mapped[str] = mapped_column(String, nullable=True)
    # identifier_value: Mapped[str] = mapped_column(String, nullable=True)
    surname: Mapped[str] = mapped_column(String, nullable=True)
    given_name: Mapped[str] = mapped_column(String, nullable=True)
    prefix: Mapped[str] = mapped_column(String, nullable=True)
    suffix: Mapped[str] = mapped_column(String, nullable=True)
    date_of_birth: Mapped[str] = mapped_column(Date, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
    occupation: Mapped[str] = mapped_column(String, nullable=True)
    income_level: Mapped[str] = mapped_column(String, nullable=True)
    education_level: Mapped[str] = mapped_column(String, nullable=True)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)