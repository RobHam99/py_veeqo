from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Tags(PyVeeqo):
    """This class implements all the tags api calls.
    """
    _ENDPOINT_KEY = "tags"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("tags",))
    def get_all_tags(self) -> Result:
        """Get a list of all tags.
        https://developers.veeqo.com/docs#/reference/tags/tag-collection/list-all-tags
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="POST", path_structure=("tags",))
    def create_a_tag(self, data: Dict = None, json: Optional[JSONType] = None) -> Result:
        """Create a new tag.
        https://developers.veeqo.com/docs#/reference/tags/tag-collection/create-a-new-tag

        Args:
            data (Dict): The data to be sent in the request body.
            json (Optional[JSONType]): The data to be sent in the request body.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="GET", path_structure=("tags", "{tag_id}"))
    def view_tag_detail(self, tag_id: int) -> Result:
        """Get details of a specific tag.
        https://developers.veeqo.com/docs#/reference/tags/tag/view-an-tag-detail

        Args:
            tag_id (int): The id of the tag.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="DELETE", path_structure=("tags", "{tag_id}"))
    def delete_tag(self, tag_id: int) -> Result:
        """Delete a specific tag.
        https://developers.veeqo.com/docs#/reference/tags/tag/delete
        
        Args:
            tag_id (int): The id of the tag.
        """
        pass
