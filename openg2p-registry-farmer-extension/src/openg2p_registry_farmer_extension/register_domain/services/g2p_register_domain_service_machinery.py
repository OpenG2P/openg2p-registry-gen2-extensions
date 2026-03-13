import logging

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas import ChangeRequestRequestPayload

_logger = logging.getLogger('g2p-register-domain-service')

class G2PRegisterDomainServiceMachinery(G2PRegisterDomainService):

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating farmer domain attributes")
        return

    def construct_record_name(self, payload: dict) -> str:
        _logger.info("Constructing record name for machinery")

        count = payload.get("count")
        machinery_type = (payload.get("machinery_type") or "").strip()
        functional_record_id = (payload.get("functional_record_id") or "").strip()
        count_text = str(count).strip() if count is not None else ""
        return " ".join(filter(None, [count_text, machinery_type, functional_record_id])).strip()
