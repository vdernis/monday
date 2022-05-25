from monday.resources.base import BaseResource
from monday.query_joins import create_column_query


class ColumnResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_column(self, board_id, title, description, column_type):
        query = create_column_query(board_id, title, description, column_type)
        return self.client.execute(query)
