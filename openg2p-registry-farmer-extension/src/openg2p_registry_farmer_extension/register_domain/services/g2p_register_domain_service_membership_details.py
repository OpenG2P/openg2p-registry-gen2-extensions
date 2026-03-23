import logging

from openg2p_registry_core.schemas import ChangeRequestRequestPayload
from openg2p_registry_core.services import G2PRegisterDomainService

_logger = logging.getLogger("g2p-register-domain-service")


class G2PRegisterDomainServiceMembershipDetails(G2PRegisterDomainService):
    async def validate_domain_attributes(
        self, change_request_request_payload: ChangeRequestRequestPayload
    ):
        _logger.info("Validating membership details domain attributes")
        return

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for membership details")

        keys = [
            "functional_record_id",
            "record_name",
            "primary_cooperative_name",
            "cooperative_union_name",
            "farmer_cluster_role",
        ]
        search_text = []
        if extra:
            search_text.extend(
                str(value).strip() for value in extra if str(value).strip()
            )
        search_text.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(search_text).strip()

    def construct_record_name(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing record name for membership details")

        keys = ["primary_cooperative_name", "functional_record_id"]
        record_name = []
        if extra:
            record_name.extend(extra)
        record_name.extend((payload.get(key) or "").strip() for key in keys)

        return " ".join(record_name).strip()
