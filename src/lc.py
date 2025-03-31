import time
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


def test_parameter(parameter_name, values):
    results = {}
    prompt = "Write a short poem about artificial intelligence."

    for value in values:
        print(f"Testing {parameter_name} = {value}")

        # Create model with the specific parameter value
        if parameter_name == "temperature":
            chat = ChatOpenAI(
                base_url="http://localhost:1234/v1",
                api_key="lm-studio",
                temperature=value,
                max_tokens=200,
            )
        elif parameter_name == "top_p":
            chat = ChatOpenAI(
                base_url="http://localhost:1234/v1",
                api_key="lm-studio",
                top_p=value,
                max_tokens=200,
            )
        elif parameter_name == "max_tokens":
            chat = ChatOpenAI(
                base_url="http://localhost:1234/v1",
                api_key="lm-studio",
                temperature=0.7,
                max_tokens=value,
            )

        # Measure response time
        start_time = time.time()
        response = chat.invoke([HumanMessage(content=prompt)])
        end_time = time.time()

        # Store results
        results[value] = {"response": response.content, "time": end_time - start_time}

    return results


def main():
    # Test different temperatures
    temp_results = test_parameter("temperature", [0.1, 0.5, 0.9])

    # Print results for comparison
    for temp, data in temp_results.items():
        print(f"\nTemperature: {temp}")
        print(f"Response time: {data['time']:.2f} seconds")
        print(f"Response length: {len(data['response'])} characters")
        print(f"Response: \n{data['response']}")

    # # Initialize ChatOpenAI
    # chat = ChatOpenAI(
    #     base_url="http://localhost:1234/v1",
    #     api_key="lm-studio",
    #     model="local-model",
    # )

    # # Test the model
    # response = chat.invoke(
    #     [HumanMessage(content="Explain what LangChain is in simple terms.")]
    # )
    # print("\nResponse:")
    # print(response.content)


if __name__ == "__main__":
    main()
