import requests

class Client:
    "Client for freelancehunt api v2"

    URL = "https://api.freelancehunt.com/v2/"

    def __init__(self, key: str, currency: str = "UAH", language: str = "ru"):
        self._key = key

        self.currency = currency
        self.language = language

    @property
    def key(self):
        raise AttributeError("Key is secret")

    @key.setter
    def key(self, value):
        self._key = value

    def _value_to_param(self, value: object) -> None:
        """Converts value to param for requests"""

        if value is None:
            return "null"

        if isinstance(value, str):
            return value

        if isinstance(value, int):
            return str(value)

        if isinstance(value, bool):
            return str(int(value))

    def get(self, url: str, headers : dict[str : object] = {}, **kwargs):
        """Get request method for freelancehunt api"""
        return requests.get(
            Client.URL + url,
            headers={**headers, "Authorization" : f"Bearer {self._key}"}, 
            params={i : self._value_to_param(j) for i, j in kwargs.items()}
        ).json()

    def get_projects(self, only_my_skills: bool = False, skill_id: list[int] = None, 
        employer_id: int = None, only_for_plus: bool = False
    ):
        params = {
            "only_my_skills" : only_my_skills,
            "skill_id" : skill_id,
            "employer_id" : employer_id,
            "only_for_plus" : only_for_plus
        }

        return self.get("projects", **params)