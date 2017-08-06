import json
from requests import get, post, put

class HueClient(object):

    def __init__(self, host, user_key):
        self.host = host
        self.user_key = user_key

    def _authed_url(self, path=None):
        norm_path = path if path else ""
        assert norm_path.startswith("/"), "Path has to start with /"
        return "http://" + self.host + "/api/" + self.user_key + norm_path

    def _set_light_state(self, light_num, state):
        url = self._authed_url("/lights/" + str(light_num)) + "/state"
        payload = json.dumps(state)
        return json.loads(put(url, data=payload).content)

    def info(self):
        """get general info"""
        return json.loads(get(self._authed_url()).content)

    def light_info(self, light_num):
        """get light info"""
        url = self._authed_url("/lights/" + str(light_num))
        return json.loads(get(url).content)

    def light_on(self, light_num):
        """turn a light on"""
        return self._set_light_state(light_num, {"on": True})

    def light_off(self, light_num):
        """turn a light off"""
        return self._set_light_state(light_num, {"on": False})
