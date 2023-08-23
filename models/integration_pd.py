from typing import Optional
from pydantic import BaseModel
from pylon.core.tools import log


class IntegrationModel(BaseModel):
    # config_file: Optional[str] = '/path/to/custom.w3af'
    # save_intermediates_to: Optional[str] = '/data/intermediates/dast'

    def check_connection(self) -> bool:
        try:
            return True
        except Exception as e:
            log.exception(e)
            return False
