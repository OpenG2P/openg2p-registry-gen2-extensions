from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, validates
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel


# All Register classes should have the prefix G2PRegister
class G2PRegisterFarmer(G2PRegister):
    __tablename__ = "g2p_register_farmers"

    # internal_record_id
    # functional_record_id -> farmer_id
    # foundational_id -> national_id
    # link_foundational_id -> NONE
    # link_foundational_register_id -> NONE
    # link_internal_record_id -> household's internal_record_id
    # link_internal_register_id -> household register_id
    name: Mapped[str] = mapped_column(String, nullable=False)
    date_of_birth: Mapped[str] = mapped_column(Date, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=False)
    district: Mapped[str] = mapped_column(String, nullable=False)
    region: Mapped[str] = mapped_column(String, nullable=False)
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)

    @validates('name', 'date_of_birth', 'gender', 'address', 'district', 'region', 'mobile_number', 'email', 'marital_status')
    def update_search_text(self, _key: str, value: str) -> str:
        """
        Automatically update search_text whenever any searchable field is modified.
        Combines all searchable fields into a single text for trigram search.
        """
        self._populate_search_text()
        return value

    def _populate_search_text(self) -> None:
        """
        Populate search_text by combining all searchable farmer fields.
        """
        searchable_fields: list[str] = [
            self.name or "",
            self.address or "",
            self.district or "",
            self.region or "",
            self.mobile_number or "",
            self.email or "",
            self.marital_status or ""
        ]
        self.search_text = " ".join(searchable_fields).strip()

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFarmer(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_farmers"

    # Override all columns from G2PRegisterFarmerBase to make them nullable for history
    name: Mapped[str] = mapped_column(String, nullable=True)
    date_of_birth: Mapped[str] = mapped_column(Date, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    district: Mapped[str] = mapped_column(String, nullable=True)
    region: Mapped[str] = mapped_column(String, nullable=True)
    mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
