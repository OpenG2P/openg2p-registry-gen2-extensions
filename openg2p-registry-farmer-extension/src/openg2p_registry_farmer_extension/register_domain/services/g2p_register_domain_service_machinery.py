import logging

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas.payload import ChangeRequestRequestPayload

_logger = logging.getLogger('g2p-register-domain-service')

class G2PRegisterDomainServiceMachinery(G2PRegisterDomainService):
    pass

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating farmer domain attributes")
        pass
