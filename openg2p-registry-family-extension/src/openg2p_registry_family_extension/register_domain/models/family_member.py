from sqlalchemy import String, Boolean, DateTime, Date, Float
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel
from datetime import datetime, date


# All Register classes should have the prefix G2PRegister
class G2PRegisterFamilyMember(G2PRegister):
    __tablename__ = "g2p_register_family_members"

    # internal_record_id
    # functional_record_id -> NONE
    # foundational_id -> national_id
    # link_foundational_id -> NONE
    # link_internal_record_id -> family's internal_record_id
    # master_register_id -> family register_id

    # DCI fields
    # Identifiers
    # identifier_type: Mapped[str] = mapped_column(String, nullable=True)
    # identifier_value: Mapped[str] = mapped_column(String, nullable=True)

    # Name fields
    surname: Mapped[str] = mapped_column(String, nullable=True)
    given_name: Mapped[str] = mapped_column(String, nullable=True)
    second_name: Mapped[str] = mapped_column(String, nullable=True)
    prefix: Mapped[str] = mapped_column(String, nullable=True)
    suffix: Mapped[str] = mapped_column(String, nullable=True)

    # Contacts stored as JSON arrays
    phone_numbers: Mapped[list] = mapped_column(JSONB, nullable=True)
    emails: Mapped[list] = mapped_column(JSONB, nullable=True)

    # Basic details
    sex: Mapped[str] = mapped_column(String, nullable=True)
    birth_date: Mapped[str] = mapped_column(String, nullable=True)

    # Birthplace
    birth_place_name: Mapped[str] = mapped_column(String, nullable=True)
    birth_place_lat: Mapped[float] = mapped_column(Float, nullable=True)
    birth_place_lng: Mapped[float] = mapped_column(Float, nullable=True)

    # Death details
    death_date: Mapped[str] = mapped_column(String, nullable=True)
    death_place: Mapped[str] = mapped_column(String, nullable=True)

    # Address details
    address_line1: Mapped[str] = mapped_column(String, nullable=True)
    address_line2: Mapped[str] = mapped_column(String, nullable=True)
    locality: Mapped[str] = mapped_column(String, nullable=True)
    sub_region_code: Mapped[str] = mapped_column(String, nullable=True)
    region_code: Mapped[str] = mapped_column(String, nullable=True)
    postal_code: Mapped[str] = mapped_column(String, nullable=True)
    country_code: Mapped[str] = mapped_column(String, nullable=True)

    # Plus code + geolocation
    plus_code: Mapped[str] = mapped_column(String, nullable=True)
    geo_lat: Mapped[float] = mapped_column(Float, nullable=True)
    geo_lng: Mapped[float] = mapped_column(Float, nullable=True)

    # Marital info
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
    marriage_date: Mapped[str] = mapped_column(String, nullable=True)
    divorce_date: Mapped[str] = mapped_column(String, nullable=True)

    # Parents
    # parent1_identifier_value: Mapped[str] = mapped_column(String, nullable=True)
    # parent2_identifier_value: Mapped[str] = mapped_column(String, nullable=True)

    # Social Registry Commons
    education_level: Mapped[str] = mapped_column(String, nullable=True)
    employment_status: Mapped[str] = mapped_column(String, nullable=True)
    role_in_household: Mapped[str] = mapped_column(String, nullable=True)
    relationship_with_household_head: Mapped[str] = mapped_column(String, nullable=True)

    sources_of_income: Mapped[str] = mapped_column(String, nullable=True)
    annual_income: Mapped[str] = mapped_column(String, nullable=True)
    owns_a_two_wheeler: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_a_three_wheeler: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_a_four_wheeler: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_a_cart: Mapped[bool] = mapped_column(Boolean, nullable=True)
    land_ownership: Mapped[bool] = mapped_column(Boolean, nullable=True)
    type_of_land_owned: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[str] = mapped_column(String, nullable=True)
    owns_house: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_livestock: Mapped[bool] = mapped_column(Boolean, nullable=True)

    is_head: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_pregnant_and_lactating: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_malnourished_child: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_search_text_fields(self) -> list[str]:
        """
        Return family member-specific fields for search text aggregation.
        G2PRegister fields are automatically included via event listeners.
        """
        return [
            # String fields
            self.surname or "",
            self.given_name or "",
            self.second_name or "",
            self.prefix or "",
            self.suffix or "",
            self.sex or "",
            self.birth_place_name or "",
            self.death_date or "",
            self.death_place or "",
            self.address_line1 or "",
            self.address_line2 or "",
            self.locality or "",
            self.sub_region_code or "",
            self.region_code or "",
            self.postal_code or "",
            self.country_code or "",
            self.plus_code or "",
            self.marital_status or "",
            self.marriage_date or "",
            self.divorce_date or "",
            # Non-string fields - need str() conversion
            str(self.phone_numbers) if self.phone_numbers else "",
            str(self.emails) if self.emails else "",
            str(self.birth_date) if self.birth_date else "",
            str(self.birth_place_lat) if self.birth_place_lat is not None else "",
            str(self.birth_place_lng) if self.birth_place_lng is not None else "",
            str(self.geo_lat) if self.geo_lat is not None else "",
            str(self.geo_lng) if self.geo_lng is not None else "",
            # Social Registry Commons
            self.education_level or "",
            self.employment_status or "",
            self.role_in_household or "",
            self.relationship_with_household_head or "",
            self.sources_of_income or "",
            self.annual_income or "",
            str(self.owns_a_two_wheeler) if self.owns_a_two_wheeler is not None else "",
            str(self.owns_a_three_wheeler) if self.owns_a_three_wheeler is not None else "",
            str(self.owns_a_four_wheeler) if self.owns_a_four_wheeler is not None else "",
            str(self.owns_a_cart) if self.owns_a_cart is not None else "",
            str(self.land_ownership) if self.land_ownership is not None else "",
            self.type_of_land_owned or "",
            self.land_size or "",
            str(self.owns_house) if self.owns_house is not None else "",
            str(self.owns_livestock) if self.owns_livestock is not None else "",
            str(self.is_head) if self.is_head is not None else "",
            str(self.is_disabled) if self.is_disabled is not None else "",
            str(self.is_pregnant_and_lactating) if self.is_pregnant_and_lactating is not None else "",
            str(self.is_malnourished_child) if self.is_malnourished_child is not None else "",
        ]

# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryFamilyMember(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_family_members"

    # Override all columns from G2PRegisterFamilyMemberBase to make them nullable for history
    surname: Mapped[str] = mapped_column(String, nullable=True)
    given_name: Mapped[str] = mapped_column(String, nullable=True)
    second_name: Mapped[str] = mapped_column(String, nullable=True)
    prefix: Mapped[str] = mapped_column(String, nullable=True)
    suffix: Mapped[str] = mapped_column(String, nullable=True)
    phone_numbers: Mapped[list] = mapped_column(JSONB, nullable=True)
    emails: Mapped[list] = mapped_column(JSONB, nullable=True)
    sex: Mapped[str] = mapped_column(String, nullable=True)
    birth_date: Mapped[str] = mapped_column(String, nullable=True)
    birth_place_name: Mapped[str] = mapped_column(String, nullable=True)
    birth_place_lat: Mapped[float] = mapped_column(Float, nullable=True)
    birth_place_lng: Mapped[float] = mapped_column(Float, nullable=True)
    death_date: Mapped[str] = mapped_column(String, nullable=True)
    death_place: Mapped[str] = mapped_column(String, nullable=True)
    address_line1: Mapped[str] = mapped_column(String, nullable=True)
    address_line2: Mapped[str] = mapped_column(String, nullable=True)
    locality: Mapped[str] = mapped_column(String, nullable=True)
    sub_region_code: Mapped[str] = mapped_column(String, nullable=True)
    region_code: Mapped[str] = mapped_column(String, nullable=True)
    postal_code: Mapped[str] = mapped_column(String, nullable=True)
    country_code: Mapped[str] = mapped_column(String, nullable=True)
    plus_code: Mapped[str] = mapped_column(String, nullable=True)
    geo_lat: Mapped[float] = mapped_column(Float, nullable=True)
    geo_lng: Mapped[float] = mapped_column(Float, nullable=True)
    marital_status: Mapped[str] = mapped_column(String, nullable=True)
    marriage_date: Mapped[str] = mapped_column(String, nullable=True)
    divorce_date: Mapped[str] = mapped_column(String, nullable=True)

    # Social Registry Commons
    education_level: Mapped[str] = mapped_column(String, nullable=True)
    employment_status: Mapped[str] = mapped_column(String, nullable=True)
    role_in_household: Mapped[str] = mapped_column(String, nullable=True)
    relationship_with_household_head: Mapped[str] = mapped_column(String, nullable=True)
    sources_of_income: Mapped[str] = mapped_column(String, nullable=True)
    annual_income: Mapped[str] = mapped_column(String, nullable=True)
    owns_a_two_wheeler: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_a_three_wheeler: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_a_four_wheeler: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_a_cart: Mapped[bool] = mapped_column(Boolean, nullable=True)
    land_ownership: Mapped[bool] = mapped_column(Boolean, nullable=True)
    type_of_land_owned: Mapped[str] = mapped_column(String, nullable=True)
    land_size: Mapped[str] = mapped_column(String, nullable=True)
    owns_house: Mapped[bool] = mapped_column(Boolean, nullable=True)
    owns_livestock: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_head: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_pregnant_and_lactating: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_malnourished_child: Mapped[bool] = mapped_column(Boolean, nullable=True)