# Audits

Types:

```python
from n8n_minus_1.1.1.types import Audit
```

Methods:

- <code title="post /audit">client.audits.<a href="./src/n8n_minus_1.1.1/resources/audits.py">generate</a>(\*\*<a href="src/n8n_minus_1.1.1/types/audit_generate_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/audit.py">Audit</a></code>

# Credentials

Types:

```python
from n8n_minus_1.1.1.types import Credential
```

Methods:

- <code title="post /credentials">client.credentials.<a href="./src/n8n_minus_1.1.1/resources/credentials/credentials.py">create</a>(\*\*<a href="src/n8n_minus_1.1.1/types/credential_create_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/credential.py">Credential</a></code>
- <code title="delete /credentials/{id}">client.credentials.<a href="./src/n8n_minus_1.1.1/resources/credentials/credentials.py">delete</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/credential.py">Credential</a></code>

## Schema

Types:

```python
from n8n_minus_1.1.1.types.credentials import SchemaRetrieveResponse
```

Methods:

- <code title="get /credentials/schema/{credentialTypeName}">client.credentials.schema.<a href="./src/n8n_minus_1.1.1/resources/credentials/schema.py">retrieve</a>(credential_type_name) -> <a href="./src/n8n_minus_1.1.1/types/credentials/schema_retrieve_response.py">object</a></code>

# Executions

Types:

```python
from n8n_minus_1.1.1.types import Execution, ExecutionList
```

Methods:

- <code title="get /executions/{id}">client.executions.<a href="./src/n8n_minus_1.1.1/resources/executions.py">retrieve</a>(id, \*\*<a href="src/n8n_minus_1.1.1/types/execution_retrieve_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/execution.py">Execution</a></code>
- <code title="get /executions">client.executions.<a href="./src/n8n_minus_1.1.1/resources/executions.py">list</a>(\*\*<a href="src/n8n_minus_1.1.1/types/execution_list_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/execution_list.py">ExecutionList</a></code>
- <code title="delete /executions/{id}">client.executions.<a href="./src/n8n_minus_1.1.1/resources/executions.py">delete</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/execution.py">Execution</a></code>

# Tags

Types:

```python
from n8n_minus_1.1.1.types import Tag, TagList
```

Methods:

- <code title="post /tags">client.tags.<a href="./src/n8n_minus_1.1.1/resources/tags.py">create</a>(\*\*<a href="src/n8n_minus_1.1.1/types/tag_create_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/tag.py">Tag</a></code>
- <code title="get /tags/{id}">client.tags.<a href="./src/n8n_minus_1.1.1/resources/tags.py">retrieve</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/tag.py">Tag</a></code>
- <code title="put /tags/{id}">client.tags.<a href="./src/n8n_minus_1.1.1/resources/tags.py">update</a>(id, \*\*<a href="src/n8n_minus_1.1.1/types/tag_update_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/tag.py">Tag</a></code>
- <code title="get /tags">client.tags.<a href="./src/n8n_minus_1.1.1/resources/tags.py">list</a>(\*\*<a href="src/n8n_minus_1.1.1/types/tag_list_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/tag_list.py">TagList</a></code>
- <code title="delete /tags/{id}">client.tags.<a href="./src/n8n_minus_1.1.1/resources/tags.py">delete</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/tag.py">Tag</a></code>

# Workflows

Types:

```python
from n8n_minus_1.1.1.types import Workflow, WorkflowList
```

Methods:

- <code title="post /workflows">client.workflows.<a href="./src/n8n_minus_1.1.1/resources/workflows/workflows.py">create</a>(\*\*<a href="src/n8n_minus_1.1.1/types/workflow_create_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/workflow.py">Workflow</a></code>
- <code title="get /workflows/{id}">client.workflows.<a href="./src/n8n_minus_1.1.1/resources/workflows/workflows.py">retrieve</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/workflow.py">Workflow</a></code>
- <code title="put /workflows/{id}">client.workflows.<a href="./src/n8n_minus_1.1.1/resources/workflows/workflows.py">update</a>(id, \*\*<a href="src/n8n_minus_1.1.1/types/workflow_update_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/workflow.py">Workflow</a></code>
- <code title="get /workflows">client.workflows.<a href="./src/n8n_minus_1.1.1/resources/workflows/workflows.py">list</a>(\*\*<a href="src/n8n_minus_1.1.1/types/workflow_list_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/workflow_list.py">WorkflowList</a></code>
- <code title="delete /workflows/{id}">client.workflows.<a href="./src/n8n_minus_1.1.1/resources/workflows/workflows.py">delete</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/workflow.py">Workflow</a></code>
- <code title="post /workflows/{id}/activate">client.workflows.<a href="./src/n8n_minus_1.1.1/resources/workflows/workflows.py">activate</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/workflow.py">Workflow</a></code>
- <code title="post /workflows/{id}/deactivate">client.workflows.<a href="./src/n8n_minus_1.1.1/resources/workflows/workflows.py">deactivate</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/workflow.py">Workflow</a></code>

## Tags

Types:

```python
from n8n_minus_1.1.1.types.workflows import WorkflowTags
```

Methods:

- <code title="put /workflows/{id}/tags">client.workflows.tags.<a href="./src/n8n_minus_1.1.1/resources/workflows/tags.py">update</a>(id, \*\*<a href="src/n8n_minus_1.1.1/types/workflows/tag_update_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/workflows/workflow_tags.py">WorkflowTags</a></code>
- <code title="get /workflows/{id}/tags">client.workflows.tags.<a href="./src/n8n_minus_1.1.1/resources/workflows/tags.py">list</a>(id) -> <a href="./src/n8n_minus_1.1.1/types/workflows/workflow_tags.py">WorkflowTags</a></code>

# Users

Types:

```python
from n8n_minus_1.1.1.types import User, UserList
```

Methods:

- <code title="get /users/{id}">client.users.<a href="./src/n8n_minus_1.1.1/resources/users.py">retrieve</a>(id, \*\*<a href="src/n8n_minus_1.1.1/types/user_retrieve_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/user.py">User</a></code>
- <code title="get /users">client.users.<a href="./src/n8n_minus_1.1.1/resources/users.py">list</a>(\*\*<a href="src/n8n_minus_1.1.1/types/user_list_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/user_list.py">UserList</a></code>

# SourceControl

Types:

```python
from n8n_minus_1.1.1.types import ImportResult
```

Methods:

- <code title="post /source-control/pull">client.source_control.<a href="./src/n8n_minus_1.1.1/resources/source_control.py">pull</a>(\*\*<a href="src/n8n_minus_1.1.1/types/source_control_pull_params.py">params</a>) -> <a href="./src/n8n_minus_1.1.1/types/import_result.py">ImportResult</a></code>
