 ### ⚠️⚠️⚠️ This repo is not used anymore. ⚠️⚠️⚠️
 ### The `python-provider` has been moved to the main repository for GO Feature Flag and is now available directly in the main repository [thomaspoignant/go-feature-flag](https://github.com/thomaspoignant/go-feature-flag/tree/main/openfeature/providers/python-provider)

---


# GO Feature Flag Python Provider

> ⚠️ Development is in progress ⚠️
> See the upstream [OpenFeature SDK](https://github.com/open-feature/python-sdk) for details about when a stable version of this library is possible.

GO Feature Flag provider allows you to connect to your GO Feature Flag instance.

[GO Feature Flag](https://gofeatureflag.org) believes in simplicity and offers a simple and lightweight solution to use feature flags.
Our focus is to avoid any complex infrastructure work to use GO Feature Flag.

This is a complete feature flagging solution with the possibility to target only a group of users, use any types of flags, store your configuration in various location and advanced rollout functionality. You can also collect usage data of your flags and be notified of configuration changes.

# Python SDK usage

## Install dependencies

The first things we will do is install the **Open Feature SDK** and the **GO Feature Flag provider**.

```shell
 TODO
```

## Initialize your Open Feature client

To evaluate the flags you need to have an Open Feature configured in you app.
This code block shows you how you can create a client that you can use in your application.

```python
from gofeatureflag_python_provider.provider import GoFeatureFlagProvider
from gofeatureflag_python_provider.options import GoFeatureFlagOptions
from open_feature import open_feature_api
from open_feature.evaluation_context.evaluation_context import EvaluationContext

# ...

goff_provider = GoFeatureFlagProvider(
    options=GoFeatureFlagOptions(endpoint="https://gofeatureflag.org/")
)
open_feature_api.set_provider(goff_provider)
client = open_feature_api.get_client(name="test-client")
```

## Evaluate your flag

This code block explain how you can create an `EvaluationContext` and use it to evaluate your flag.


> In this example we are evaluating a `boolean` flag, but other types are available.
>
> **Refer to the [Open Feature documentation](https://docs.openfeature.dev/docs/reference/concepts/evaluation-api#basic-evaluation) to know more about it.**

```python
# Context of your flag evaluation.
# With GO Feature Flag you MUST have a targetingKey that is a unique identifier of the user.
user_context = EvaluationContext(
                 targeting_key="d45e303a-38c2-11ed-a261-0242ac120002",
                 attributes={
                     "email": "john.doe@gofeatureflag.org",
                     "firstname": "john",
                     "lastname": "doe",
                     "anonymous": False,
                     "admin": True,
                 })

admin_flag = client.get_boolean_value(
          flag_key=flag_key,
          default_value=default_value,
          evaluation_context=ctx,
      )

if admin_flag:
  # flag "flag-only-for-admin" is true for the user
else:
  # flag "flag-only-for-admin" is false for the user
```
