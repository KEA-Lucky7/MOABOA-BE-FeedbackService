import logging
import os
from http.client import HTTPException

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from langchain.chat_models import AzureChatOpenAI

import app.model.dto.dto
from app.core.config import config

AZURE_OPENAI_API_KEY = config('OPENAI_API_KEY')
OPENAI_API_VERSION = '2024-02-01'
AZURE_OPENAI_ENDPOINT = config('AZURE_OPENAI_ENDPOINT')

os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_API_KEY
os.environ["AZURE_OPENAI_API_VERSION"] = OPENAI_API_VERSION
os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT


# 로거 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

chatgpt = AzureChatOpenAI(
    openai_api_version=OPENAI_API_VERSION,
    azure_deployment='moaboa-gpt',
    temperature=0.3,
    max_tokens=100
)

SYSTEM_TEMPLATE = """"
                너는 소비내역에 대해 피드백 해주는 인공지능이야
                내가 {consumptions}를 알려줄테니까 너는 나의 소비내역들의 피드백을 알려줘. 100자 이내 문장으로만 말해.
                형식은
                피드백:
                """
HUMAN_TEMPLATE = (
    '{consumptions}'
)


def create_feedback(request: app.model.dto.dto.UserConsumptions):
    # if not all([request.birthDate, request.gender, request.today]):
    #     raise HTTPException(status_code=400, detail="Missing required parameters")

    system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE)
    human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_TEMPLATE)

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            system_message_prompt,
            human_message_prompt
        ]
    )

    # chat_prompt
    result = chatgpt(
        chat_prompt.format_prompt(
            consumptions=request.consumption_history
        ).to_messages()
    )

    feedback = result.content
    logger.info("피드백 생성 완료: %s", feedback)

    return feedback