from openg2p_fastapi_common.service import BaseService
from openg2p_registry_core.services import G2PRegisterDomainService

from ..services import G2PRegisterFarmerDomainService

class G2PRegisterDomainFactory(BaseService):

    g2p_register_domain_service: G2PRegisterDomainService = None
    
    def get_domain_service(self, register_mnemonic: str) -> G2PRegisterDomainService:
        if register_mnemonic.upper() == "FARMER":
            g2p_register_domain_service = G2PRegisterFarmerDomainService.get_component()
            return g2p_register_domain_service
        if register_mnemonic.upper() == "HOUSEHOLD":
            from ..services import G2PRegisterHouseholdDomainService
            g2p_register_domain_service = G2PRegisterHouseholdDomainService.get_component()
            return g2p_register_domain_service
        if register_mnemonic.upper() == "HOUSEHOLDMEMBER":
            from ..services import G2PRegisterHouseholdMemberDomainService
            g2p_register_domain_service = G2PRegisterHouseholdMemberDomainService.get_component()
            return g2p_register_domain_service
        if register_mnemonic.upper() == "LAND":
            from ..services import G2PRegisterLandDomainService
            g2p_register_domain_service = G2PRegisterLandDomainService.get_component()
            return g2p_register_domain_service
        if register_mnemonic.upper() == "LIVESTOCK":
            from ..services import G2PRegisterLivestockDomainService
            g2p_register_domain_service = G2PRegisterLivestockDomainService.get_component()
            return g2p_register_domain_service
        if register_mnemonic.upper() == "CROP":
            from ..services import G2PRegisterCropDomainService
            g2p_register_domain_service = G2PRegisterCropDomainService.get_component()
            return g2p_register_domain_service
        if register_mnemonic.upper() == "MACHINERY":
            from ..services import G2PRegisterMachineryDomainService
            g2p_register_domain_service = G2PRegisterMachineryDomainService.get_component()
            return g2p_register_domain_service