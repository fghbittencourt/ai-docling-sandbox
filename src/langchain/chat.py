from langchain_openai import ChatOpenAI


def get_chat(temperature=0.7, max_tokens=None):
    chat = ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return chat
