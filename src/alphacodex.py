from alphahub import AlphaHub
import os
from safe_llm_core import RunnableType

PACKAGE_NAME = "alphacodex_middle_east_nlci"
ACCESS_TOKEN = os.getenv("AZURE_DEVOPS_ACCESS_TOKEN")

alpha_hub = AlphaHub(ACCESS_TOKEN)
alphacodex_graph = alpha_hub.pull(RunnableType.CODEX_GRAPH, PACKAGE_NAME)
graph = alphacodex_graph.compile()
