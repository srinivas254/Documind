from app.models.llm_model import model
from langchain_core.messages import SystemMessage, HumanMessage

def llm_retrieval(context: str, query: str) -> str:

    system_message = SystemMessage(
        content="""
        You are a question-answering assistant. Answer the user's question
        using ONLY the information provided in the retrieved context.

        Rules:
        1. Use only facts explicitly supported by the context.
        2. Do not use your own knowledge or outside information.
        3. If the context does not contain enough information to answer,
           respond exactly with: "I don't know based on the provided context."
        4. Do not invent facts or make unsupported assumptions.
        5. Keep your answer clear and relevant to the question.
        """
    )

    human_message = HumanMessage(
        content=f"""
        Retrieved context:
        {context}

        User question:
        {query}
        """
    )

    messages = [system_message, human_message]

    response = model.invoke(messages)

    return response.content