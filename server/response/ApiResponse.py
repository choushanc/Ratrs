from typing import Optional,Dict,Any
from fastapi.responses import JSONResponse
class ApiResponse(JSONResponse):
    status_code: int = 200
    result: Optional[Dict[str, Any]] = None
    code: int = 0
    msg: str = ''

    def __init__(self,
                 status_code=None,
                 code=None,
                 result=None,
                 msg=None,
                 ad:bool=False,
                 **options):
        if status_code:
            self.status_code = status_code
        if code:
            self.code = code
        if result:
            self.result = result
        if msg:
            self.msg = msg
        if ad:
            content = dict(
                status_code=self.status_code,
                Code=self.code,
                Data=self.result,
                Msg=self.msg)
        else:
            content = dict(
                status_code=self.status_code,
                code=self.code,
                result=self.result,
                msg=self.msg)
        super(JSONResponse, self).__init__(
            status_code=self.status_code,
            content=content,
            **options)
