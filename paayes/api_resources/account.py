from __future__ import absolute_import, division, print_function

import paayes
from paayes import oauth, six
from paayes import util
from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import DeletableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import custom_method
from paayes.api_resources.abstract import nested_resource_class_methods
from paayes.six.moves.urllib.parse import quote_plus


@custom_method("reject", http_verb="post")
@nested_resource_class_methods(
    "capability",
    operations=["retrieve", "update", "list"],
    resource_plural="capabilities",
)
@nested_resource_class_methods(
    "external_account",
    operations=["create", "retrieve", "update", "delete", "list"],
)
@nested_resource_class_methods("login_link", operations=["create"])
@nested_resource_class_methods(
    "person",
    operations=["create", "retrieve", "update", "delete", "list"],
)
class Account(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "account"

    def reject(self, idempotency_key=None, **params):
        url = self.instance_url() + "/reject"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    # We are not adding a helper for capabilities here as the Account object already has a
    # capabilities property which is a hash and not the sub-list of capabilities.

    @classmethod
    def retrieve(cls, id=None, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def modify(cls, id=None, **params):
        url = cls._build_instance_url(id)
        return cls._static_request("post", url, **params)

    @classmethod
    def _build_instance_url(cls, sid):
        if not sid:
            return "/api/v1/account"
        sid = util.utf8(sid)
        base = cls.class_url()
        extn = quote_plus(sid)
        return "%s/%s" % (base, extn)

    def instance_url(self):
        return self._build_instance_url(self.get("id"))

    def persons(self, **params):
        return self.request("get", self.instance_url() + "/persons", params)

    def deauthorize(self, **params):
        params["paayes_user_id"] = self.id
        return oauth.OAuth.deauthorize(**params)

    def serialize(self, previous):
        params = super(Account, self).serialize(previous)
        previous = previous or self._previous or {}

        for k, v in six.iteritems(self):
            if (
                k == "individual"
                and isinstance(v, paayes.api_resources.Person)
                and k not in params
            ):
                params[k] = v.serialize(previous.get(k, None))

        return params
