from pydantic import BaseModel
from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterSchema, G2PRegisterHistorySchema


class G2PRegisterSchemaFamilyMember(G2PRegisterSchema):

    # Identifiers
    identifier_type: Optional[str] = None
    identifier_value: Optional[str] = None

    # Name fields
    surname: Optional[str] = None
    given_name: Optional[str] = None
    second_name: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None

    # Contacts stored as JSON arrays
    phone_numbers: Optional[list] = None
    emails: Optional[list] = None

    # Basic details
    sex: Optional[str] = None
    birth_date: Optional[str] = None

    # Birthplace
    birth_place_name: Optional[str] = None
    birth_place_lat: Optional[float] = None
    birth_place_lng: Optional[float] = None

    # Death details
    death_date: Optional[str] = None
    death_place: Optional[str] = None

    # Address details
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    locality: Optional[str] = None
    sub_region_code: Optional[str] = None
    region_code: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None

    # Plus code + geolocation
    plus_code: Optional[str] = None
    geo_lat: Optional[float] = None
    geo_lng: Optional[float] = None

    # Marital info
    marital_status: Optional[str] = None
    marriage_date: Optional[str] = None
    divorce_date: Optional[str] = None

    # Parents
    parent1_identifier_value: Optional[str] = None
    parent2_identifier_value: Optional[str] = None

    # Social Registry Commons
    education_level: Optional[str] = None
    employment_status: Optional[str] = None
    role_in_household: Optional[str] = None
    relationship_with_household_head: Optional[str] = None

    sources_of_income: Optional[str] = None
    annual_income: Optional[str] = None
    owns_a_two_wheeler: Optional[bool] = None
    owns_a_three_wheeler: Optional[bool] = None
    owns_a_four_wheeler: Optional[bool] = None
    owns_a_cart: Optional[bool] = None
    land_ownership: Optional[bool] = None
    type_of_land_owned: Optional[str] = None
    land_size: Optional[str] = None
    owns_house: Optional[bool] = None
    owns_livestock: Optional[bool] = None

    is_head: Optional[bool] = None
    is_disabled: Optional[bool] = None
    is_pregnant_and_lactating: Optional[bool] = None
    is_malnourished_child: Optional[bool] = None

class G2PRegisterHistorySchemaFamilyMember(G2PRegisterHistorySchema):
    
    # Identifiers
    identifier_type: Optional[str] = None
    identifier_value: Optional[str] = None

    # Name fields
    surname: Optional[str] = None
    given_name: Optional[str] = None
    second_name: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None

    # Contacts stored as JSON arrays
    phone_numbers: Optional[list] = None
    emails: Optional[list] = None

    # Basic details
    sex: Optional[str] = None
    birth_date: Optional[str] = None

    # Birthplace
    birth_place_name: Optional[str] = None
    birth_place_lat: Optional[float] = None
    birth_place_lng: Optional[float] = None

    # Death details
    death_date: Optional[str] = None
    death_place: Optional[str] = None

    # Address details
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    locality: Optional[str] = None
    sub_region_code: Optional[str] = None
    region_code: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None

    # Plus code + geolocation
    plus_code: Optional[str] = None
    geo_lat: Optional[float] = None
    geo_lng: Optional[float] = None

    # Marital info
    marital_status: Optional[str] = None
    marriage_date: Optional[str] = None
    divorce_date: Optional[str] = None

    # Parents
    parent1_identifier_value: Optional[str] = None
    parent2_identifier_value: Optional[str] = None

    # Social Registry Commons
    education_level: Optional[str] = None
    employment_status: Optional[str] = None
    role_in_household: Optional[str] = None
    relationship_with_household_head: Optional[str] = None

    sources_of_income: Optional[str] = None
    annual_income: Optional[str] = None
    owns_a_two_wheeler: Optional[bool] = None
    owns_a_three_wheeler: Optional[bool] = None
    owns_a_four_wheeler: Optional[bool] = None
    owns_a_cart: Optional[bool] = None
    land_ownership: Optional[bool] = None
    type_of_land_owned: Optional[str] = None
    land_size: Optional[str] = None
    owns_house: Optional[bool] = None
    owns_livestock: Optional[bool] = None

    is_head: Optional[bool] = None
    is_disabled: Optional[bool] = None
    is_pregnant_and_lactating: Optional[bool] = None
    is_malnourished_child: Optional[bool] = None