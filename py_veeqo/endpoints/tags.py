from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Tags(PyVeeqo):
    """This class implements all the tags api calls.
    """
    _ENDPOINT_KEY = "tags"

    @PyVeeqo._endpoint_builder(method="GET")
    def get_all_tags(self) -> Result:
        """Get a list of all tags.
        https://developers.veeqo.com/docs#/reference/tags/tag-collection/list-all-tags
        """
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="POST")
    def create_a_tag(self, data: Dict = None, json: Optional[JSONType] = None) -> Result:
        """Create a new tag.
        https://developers.veeqo.com/docs#/reference/tags/tag-collection/create-a-new-tag

        Args:
            data (Dict): The data to be sent in the request body.
            json (Optional[JSONType]): The data to be sent in the request body.
        """
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="GET")
    def view_tag_detail(self, tag_id: int) -> Result:
        """Get details of a specific tag.
        https://developers.veeqo.com/docs#/reference/tags/tag/view-an-tag-detail

        Args:
            tag_id (int): The id of the tag.
        """
        return self._ENDPOINT_KEY + f"/{tag_id}"

    @PyVeeqo._endpoint_builder(method="DELETE")
    def delete_tag(self, tag_id: int) -> Result:
        """Delete a specific tag.
        https://developers.veeqo.com/docs#/reference/tags/tag/delete
        
        Args:
            tag_id (int): The id of the tag.
        """
        return self._ENDPOINT_KEY + f"/{tag_id}"
