from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class Assistant:
    """
    RAG assistant for client onboarding
    """
    
    def __init__(
        self,
        system_prompt,
        llm,
        message_history=[],
        vector_store=None,
        employee_information=None,
    ):
        self.system_prompt = system_prompt
        self.llm = llm
        self.messages = message_history
        self.vector_store = vector_store
        self.employee_information = employee_information

        self.chain = self.get_conversation_chain()

    def get_conversation_chain(self):
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_prompt),
                MessagesPlaceholder("conversation_history"),
                ("human", "{user_input}"),
            ]
        )
        llm = self.llm
        output_parser = StrOutputParser()
        chain = ({
            "retrieved_policy_information": lambda x: self.vector_store.as_retriever().invoke(x),
            "employee_information": lambda x: self.employee_information,
            "user_input": RunnablePassthrough(),
            "conversation_history": lambda x: self.messages,
        }) | prompt | llm | output_parser

        return chain
    

    def get_response(self, user_input):
        return self.chain.invoke(user_input)
