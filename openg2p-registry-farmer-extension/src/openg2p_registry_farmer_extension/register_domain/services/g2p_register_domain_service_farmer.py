import logging

from openg2p_registry_core.schemas import ChangeRequestRequestPayload
from openg2p_registry_core.services import G2PRegisterDomainService

_logger = logging.getLogger("g2p-register-domain-service")


class G2PRegisterDomainServiceFarmer(G2PRegisterDomainService):
    async def validate_domain_attributes(
        self, change_request_request_payload: ChangeRequestRequestPayload
    ):
        _logger.info("Validating farmer domain attributes")
        return

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for farmer")

        keys = [
            "functional_record_id",
            "first_name",
            "last_name",
            "foundational_id",
            "middle_name",
            "given_name",
            "gender",
            "birth_date",
            "marital_status",
            "occupation",
            "education_level",
            "language_spoken",
            "source_of_income",
            "national_id_masked",
            "disability_type",
            "latitude",
            "longitude",
            "altitude",
            "plus_code",
            "address_line_1",
            "address_line_2",
            "postal_code",
            "country_code",
        ]
        search_text = []
        if extra:
            search_text.extend(extra)
        search_text.extend(
            value
            for value in ((payload.get(key) or "").strip() for key in keys)
            if value
        )

        return " ".join(search_text)

    def construct_record_name(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing record name for farmer")

        keys = ["first_name", "last_name", "functional_record_id"]
        record_name = []
        if extra:
            record_name.extend(extra)
        record_name.extend((payload.get(key) or "").strip() for key in keys)

        return " ".join(record_name).strip()
